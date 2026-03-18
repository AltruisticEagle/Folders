import os
import csv
import tabulate

def main():
    initialise()
    starting_ui()
    choice = get_input()
    run_function(choice)
    
def initialise():
    if not os.path.exists("folders.csv"):
        with open ("folders.csv", "w") as file:
            fieldnames = ["subject", "at_school"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        
            request_input_folders = input ("Would you like to input your current subjects? Y/N ").strip().capitalize()
            if request_input_folders == "Y":
                input_folders()

    if not os.path.exists("schedule.csv"):
        with open ("schedule.csv", "w") as file:
            fieldnames = ["day", "p1", "p2", "p3", "p4", "p5", "p6"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            request_input_schedule = input("Would you like to input your current schedule? Y/N ").strip().capitalize()
            if request_input_schedule == "Y":
                input_schedule()

def input_schedule():
    while True:
        try:
            cycle = int(input("How many days does your schedule contain: "))
            break
        except Exception:
            print("Please enter a single number")
            continue 

    with open ("schedule.csv", "w") as file:
        fieldnames = ["day", "p1", "p2", "p3", "p4", "p5", "p6"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(cycle):
            p1 = input("Period 1 Subject: ").strip().lower().capitalize()
            p2 = input("Period 2 Subject: ").strip().lower().capitalize()
            p3 = input("Period 3 Subject: ").strip().lower().capitalize()
            p4 = input("Period 4 Subject: ").strip().lower().capitalize()
            p5 = input("Period 5 Subject: ").strip().lower().capitalize()
            p6 = input("Period 6 Subject: ").strip().lower().capitalize()
            row = {"day": i + 1, "p1": p1, "p2": p2, "p3": p3, "p4": p4, "p5": p5, "p6": p6}
            writer.writerow(row)
                         

def input_folders():
    while True:
        try:
            subject_number = int(input("How many courses do you take: "))
            break
        except Exception:
            print("Please enter a single number")
            continue 

    with open ("folders.csv", "w") as file:
        fieldnames = ["subject", "at_school"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(subject_number):
            subject = input("Subject: ").strip().lower().capitalize()
            row = {"subject": subject, "at_school": "N"}
            writer.writerow(row)



def starting_ui():
    print(
    "\nChoose to see one of the following:\n"
    "1: Your daily schedule\n"
    "2: Where is each folder\n"
    "3: change position of a folder\n"
    )

def get_input():
    functions = ["1", "2", "3"]
    while True:
        choice = input("Function: ").strip()
        if choice in functions: 
            return choice
        elif choice == "exit":
            break
        else:
            continue

def run_function(choice):
    if choice == "1":
        daily_schedule()
    elif choice == "2":
        book_places()
    elif choice == "3":
        move_book()
                
def daily_schedule():
    days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    day = input("Day: ")
    while True:
        if day not in days: 
            continue
        elif day == "exit" or day in days:
            break

    with open("schedule.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        table = []
        for row in rows: 
            if row["day"] == day:
                table.append(["1",row["p1"]])
                table.append(["2",row["p2"]])
                table.append(["3",row["p3"]])
                table.append(["4",row["p4"]])
                table.append(["5",row["p5"]])
                table.append(["6",row["p6"]])
                print(f"\n--> Day {day} Schedule:")
                print(tabulate.tabulate(table, 
                headers=["Period","Class"], 
                tablefmt="grid"))
                    
                break
    
def book_places():
    with open("folders.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        at_school = []
        at_home = []
        for row in rows:
            if row["at_school"] == "Y":
                at_school.append([len(at_school) + 1, row["subject"]])

            elif row["at_school"] == "N":    
                at_home.append([len(at_home) + 1, row["subject"]])

        print(f"\n--> At school:")
        print(tabulate.tabulate(at_school, headers=["Number", "Subject"], tablefmt="grid"))

        print(f"\n--> At home:")
        print(tabulate.tabulate(at_home, headers=["Number", "Subject"], tablefmt="grid"))

def move_book():
    while True:
        subjects = ["English", "French", "Physics", "Chemistry", "Βiology", "History", "Math"]
        change = input("Subject: ").strip().capitalize()
        if change not in subjects:
            continue
        elif change == "exit":
            break
        else:
            break

    with open("folders.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    with open("folders.csv", "w") as file:
        fieldnames = ["subject", "at_school"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            if row["subject"] == change:
                if row["at_school"] == "Y":
                    row["at_school"] = "N"
                    print(f"\n{row["subject"]} folder now at home")
                elif row["at_school"] == "N":
                    row["at_school"] = "Y"
                    print(f"\n{row["subject"]} folder now at school")
            writer.writerow(row)

if __name__ == "__main__":
    main()