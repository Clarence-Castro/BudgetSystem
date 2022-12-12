import os
from functions_file import functions
from total_file import total


def interface():
    global choice, budgets, func, date, delete, new_budget, old_budget
    while True:
        print("===============================")
        print("Budget Management System")
        print("===============================\n")

        print("1. Add Balance")
        print("2. Check Budget Record")
        print("3. Update Budget Record")
        print("4. Delete Record")
        print("5. Print Total Budget")
        print("6. Exit Program")

        choice = input("Input choice: ")

        if choice == "1":
            try:
                os.system('cls')
                print("====================")
                print("Add Balance")
                print("====================\n")

                budgets = int(input("Input budget: "))
                if budgets <= 0:
                    print("There's no point adding zero, try again.")
                    interface()
                else:
                    func = functions(budgets)
                    func.calcu()
                    print("Balance added!")
            except:
                print("Only integers are allowed!!")
                interface()

        elif choice == "2":
            os.system('cls')
            print("====================")
            print("Check Budget Record")
            print("====================\n")
            func = functions()
            func.read()

        elif choice == "3":
            os.system('cls')
            print("====================")
            print("Update Record\n")
            print("====================\n")

            func = functions()
            func.read()
            try:
                old_budget = input("\nInput old budget to be updated: ")
                new_budget = input("Input new budget: ")
                func.update(old_budget, new_budget)

                print("Update Complete!")
            except:
                print("Invalid input. Try again.")

        elif choice == "4":
            os.system('cls')
            func = functions()
            func.remove()

        elif choice == "5":
            os.system('cls')
            total()

        elif choice == "6":
            quit("Keep grinding, you can do it!! Bye!!")

        else:
            print("Let's do it again, shall we?")
            interface()
