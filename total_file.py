def total():
    mylines = []
    with open('budget.txt', 'r') as f:
        for myline in f:
            mylines.append(myline)

    total = 0

    for num in mylines:
        budget = int(num[22:-1])
        total += budget

        needs = total*0.5
        wants = total*0.3
        savings = total*0.2

    print("\n===========================")
    print("Budget: 50 | 30 | 20 RULE")
    print("=============================\n")
    print(f"Your total budget is: {total}")

    print(f"\nBudget for Needs: {int(needs)}")
    print(f"Budget for Wants: {int(wants)}")
    print(f"Budget for Savings: {int(savings)}")

    f.close()

