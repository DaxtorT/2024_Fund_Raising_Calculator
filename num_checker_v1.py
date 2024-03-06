def num_checker(question, flo_int):
    if flo_int == float:
        error = "Please enter a number (May include decimals)"
    elif flo_int == int:
        error = "Please enter a number (No decimals)"

    while True:
        try:
            response = flo_int(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main Routine goes here
get_int = num_checker("How many do you need? ", int)

get_cost = num_checker("How much does it cost? ", float)