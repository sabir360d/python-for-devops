def print_tables():
    while True:
        
        try:
            user_input = int(input("Enter the table number: "))
        except ValueError:
            print("Invalid input. Please enter a number. ")
            continue

            
        for i in range(1, 11):
            c = user_input * i
            print(f"{user_input} x {i} = {c}")
    

        choice = input("Do you want another table? (y/n):").lower()
        if choice == "n": # break the loop
            print("Thank you!")
            break
        else:
            continue # continue the loop


print_tables() # call the function
            