# Functions go here
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

def profit_goal(total_costs, yes_no):
    # Set function variables
    error = "Please enter a valid profit goal."

    while True:
        # Ask for profit goal
        response = input("What is your profit goal (e.g. $500 or 50%)")

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
            amnount = response

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
            dollar_type = string_checker(f"Do you mean ${amount:.2f}. i.e. {amount:.2f} dollars? ", yes_no, 1)

            # Set profit type based on user answer above
            if dollar_type == "yes" or dollar_type == "y":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = string_checker("Do you mean {amount}%? ", yes_no, 1)
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


# Main Routine goes here
all_costs = 200

y_n_list = ["yes", "no"]

# Loop for quick testing
for item in range(0, 6):
    profit_target = profit_goal(all_costs, y_n_list)
    print(f"Profit Target: ${profit_target:.2f}")
    print(f"Total Sales: ${all_costs + profit_target:.2f}")
    print()