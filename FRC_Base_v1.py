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

# Main Routine goes here
# Get product name
product_name = not_blank("Product Name: ", "The product name can't be blank.")
    
# Get variable costs
print("--- Variable Costs Data ---")
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Get fixed costs
print()
print("--- Fixed Costs Data ---")
fixed_expenses = get_expenses("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]

# Find Total Costs

# Ask user for profit goal

# Calculate recommended price

# Write data to file

# The Printer
print()
print("--- Variable Costs ---")
print(variable_frame)
print()
print(f"Variable Costs: ${variable_sub:.2f}")
print()

print("--- Fixed Costs ---")
print(fixed_frame)
print()
print(f"Fixed Costs: ${fixed_sub:.2f}")
print()