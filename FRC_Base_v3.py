import pandas

# Functions go here
# Function for number checking
def num_checker(question, error , flo_int):
    while True:
        try:
            response = flo_int(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Function for checking strings
def string_checker(question, valid_list, num_letters):
    while True:      
        # Error message generation
        error = f"Please choose {valid_list[0]} or {valid_list[1]}"

        # Ask user for choice (and force lowercase)
        response = input(question).lower()
        
        # Runs through list and if response is an item in list (or first letter the full name is returned)
        for item in valid_list:
            # If 'first_letter' is set to yes then check the list for first letter and full strings
            if num_letters > 0:
                if response == item[:num_letters] or response == item:
                    return item
            # If 'first_letter' is set to no then only check the list for full strings
            else:
                if response == item:
                    return item

        # Output error if response not in list        
        print(error)

    print("Instructions go Here")
    print()

# Function for checking string is not blank
def not_blank(question, error):
    while True:
        response = input(question)

        if response == "":
            print(error)
            continue
        
        return response

# Function for adding currency formatting
def currency(x):
    return f"${x:.2f}" 

# Gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):
    # Set up dicts and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list ,
        "Quantity": quantity_list,
        "Price": price_list
    }

    item_name = ""
    while item_name.lower() != "xxx":

        # Get name, quantity, item
        item_name = not_blank("Item Name: ", "The component name can't be blank.")

        if item_name.lower() == "xxx":
            break
        
        if var_fixed == "fixed":
            quantity = 1
    
        else:
            quantity = num_checker("Quantity: ", "The amount must be a whole number, (More than zero)", int)

        price = num_checker("How much for a single item? $", "The price must be a number <More than 0>", float)

        print()

        # Add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)

    # Calculate out of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (Uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    # Setup DataFrame (Only cost for fixed, variable stays the same)
    if var_fixed == "fixed":
        final_expense_frame = expense_frame[['Item','Cost']]
    else:
        final_expense_frame = expense_frame

    # Clean up the table (making the index look nice)
    expense_frame_clean = final_expense_frame.to_string(index=False)

    # Return all data
    return [expense_frame_clean, sub_total]

# Function for printing expense frames
def expense_print(heading, frame, subtotal):
    print()
    print(f"--- {heading} Costs ---")
    print(frame)
    print()
    print(f"- {heading} Costs: ${subtotal:.2f} -")

# Calculates 
def profit_goal(total_costs, yes_no):
    # Set function variables
    error = "Please enter a valid profit goal."

    while True:
        # Ask for profit goal
        response = input("What is your profit goal? (e.g. $500 or 50%) ")

        # Check weather input is $ or %
        if response[0] == "$":
            profit_type = "$"
            # Get amount of profit goal
            amount = response[1:]

        elif response[-1] == "%":
            profit_type = "%"
            # Get amount of profit goal
            amount = response[:-1]

        else:
            profit_type = "unknown"
            # Set amount to response
            amount = response

        # Check amount is valid (more than 0)
        try:
            amount = float(amount)
            if amount < 0:
                print(error)
                continue
        
        except ValueError:
            print(error)
            continue

        # Predict whether user wanted $ or %
        if profit_type == "unknown" and amount >= 100:
            dollar_type = string_checker(f"Do you mean ${amount:.2f}?  ", yes_no, 1)

            # Set profit type based on user answer above
            if dollar_type == "yes" or dollar_type == "y":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = string_checker(f"Do you mean {amount}%? ", yes_no, 1)
            if percent_type == "yes" or percent_type == "y":
                profit_type = "%"
            else:
                profit_type = "$"
        
        # Return profit goal correctly
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

# Lists here
y_n_list = ["yes", "no"]

# Main Routine goes here
# Get product name
product_name = not_blank("Product Name: ", "The product name can't be blank.")
    
# Get variable costs
print("--- Variable Costs Data ---")
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Ask if user has fixed costs
print()
have_fixed = string_checker("Do you have fixed costs to calculate? ", y_n_list, 1)

# Get fixed costs
if have_fixed == "yes" or have_fixed == "y":
    print()
    print("--- Fixed Costs Data ---")
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0
    pass

# Find Total Costs
all_costs = variable_sub + fixed_sub

# Ask user for profit goal
print()
profit_target = profit_goal(all_costs, y_n_list)

# Calculate recommended price

# Write data to file

# The Printer
variable_print = expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes" or have_fixed == "y":
    fixed_print = expense_print("Fixed", fixed_frame, fixed_sub)
else:
    pass
print()
print(f"Total Costs: ${all_costs:.2f}")
print()
print(f"Profit Target: ${profit_target:.2f}")
print(f"Total Sales: ${all_costs + profit_target:.2f}")