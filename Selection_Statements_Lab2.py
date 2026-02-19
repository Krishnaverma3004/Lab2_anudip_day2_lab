
# ===============================
# Selection Statements - Lab 2
# ===============================

# 1. Electricity Bill Calculator
def electricity_bill():
    units = int(input("Enter units consumed: "))
    senior = input("Are you a senior citizen? (yes/no): ").lower()

    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = units * 7
    else:
        bill = units * 10

    if senior == "yes":
        bill *= 0.9

    print("Total Electricity Bill:", bill)


# 2. Smart Login System
def smart_login():
    correct_username = "admin"
    correct_password = "1234"
    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login Successful")
            return
        else:
            attempts += 1
            print("Invalid credentials")

    print("Account Locked due to 3 failed attempts")


# 3. Hospital Emergency Triage
def hospital_triage():
    age = int(input("Enter age: "))
    heart_rate_abnormal = input("Heart rate abnormal? (yes/no): ").lower()
    severe_injury = input("Severe injury? (yes/no): ").lower()

    if heart_rate_abnormal == "yes" or severe_injury == "yes":
        print("Category: Critical")
    else:
        condition = input("Condition moderate? (yes/no): ").lower()
        if condition == "yes" and age > 65:
            print("Category: Upgraded to Critical")
        elif condition == "yes":
            print("Category: Moderate")
        else:
            print("Category: Normal")


# 4. Salary Increment System
def salary_increment():
    rating = int(input("Enter performance rating (1-5): "))
    experience = int(input("Enter years of experience: "))
    attendance = float(input("Enter attendance percentage: "))

    if rating >= 4 and experience >= 5 and attendance >= 90:
        increment = 20
    elif rating >= 3:
        increment = 10
    else:
        increment = 5

    print("Increment Percentage:", increment, "%")


# 5. ATM Withdrawal System
def atm_withdrawal():
    balance = float(input("Enter account balance: "))
    withdraw = float(input("Enter withdrawal amount: "))
    atm_cash = float(input("Enter ATM available cash: "))

    if withdraw > balance:
        print("Insufficient Account Balance")
    elif withdraw > 50000:
        print("Exceeds Daily Withdrawal Limit")
    elif withdraw > atm_cash:
        print("ATM has insufficient cash")
    else:
        print("Withdrawal Successful")


if __name__ == "__main__":
    print("Select Program (1-5):")
    print("1. Electricity Bill")
    print("2. Smart Login")
    print("3. Hospital Triage")
    print("4. Salary Increment")
    print("5. ATM Withdrawal")

    choice = int(input("Enter choice: "))

    if choice == 1:
        electricity_bill()
    elif choice == 2:
        smart_login()
    elif choice == 3:
        hospital_triage()
    elif choice == 4:
        salary_increment()
    elif choice == 5:
        atm_withdrawal()
    else:
        print("Invalid Choice")
