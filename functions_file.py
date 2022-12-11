from datetime import datetime
now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class functions:
    def __init__(self, budget=0):
        self.budget = budget

    def calcu(self):
        f = open("budget.txt", "a")
        f.write(f"{dt_string} / {self.budget}\n")
        f.close()

    def read(self):
        f = open("budget.txt", "r")
        lines = f.readlines()
        if len(lines) == 0:
            print("Text file is empty. Add something.")
        else:
            for line in lines:
                print("[", lines.index(line)+1, "]" + line.strip("\n"))
            f.close()

    def update(self, old_budget, new_budget):
        f = open("budget.txt", "r")
        lines = f.read()
        lines = lines.replace(old_budget, new_budget, 1)
        f.close()

        f = open("budget.txt", "w")
        f.write(lines)
        f.close()

    def remove(self):
        print("====================")
        print("Delete Record")
        print("====================\n")
        func = functions()
        func.read()
        try:
            delete_line = int(input("Input line you want to delete: "))
            with open('budget.txt', 'r') as f:
                lines = f.readlines()

                ptr = 1

                with open('budget.txt', 'w') as fw:
                    for line in lines:

                        if ptr != delete_line:
                            fw.write(line)
                        ptr += 1
            print("Deleted successfully")

        except:
            print("Error. Please try again.")
