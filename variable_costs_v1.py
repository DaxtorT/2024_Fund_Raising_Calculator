import pandas

# Functions go here
# Function for checking numbers are valid
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

# Main Routine goes here
# Set up dicts and lists
item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list ,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data
product_name = not_blank("Product Name: ", "The product name can't be blank.")

# Loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()
    # Get name, quantity, item
    item_name = not_blank("Item Name: ", "The component name can't be blank.")

    if item_name.lower() == "xxx":
        break

    quantity = num_checker("Quantity: ", "The amount must be a whole number, (More than zero)", int)

    price = num_checker("How much for a single item? $", "The price must be a number <More than 0>", float)

    # Add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# Calculate out of each component
variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

# Find sub total
variable_sub = variable_frame['Cost'].sum()

# Currency Formatting (Uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# The Mighty Printer
print(variable_frame)
print()