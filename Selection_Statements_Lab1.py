
# ===============================
# Selection Statements - Lab 1
# ===============================

# 1. Banking – Suspicious Transaction Detection
def suspicious_transaction():
    amount = float(input("Enter transaction amount: "))
    account_age = int(input("Enter account age in months: "))
    international = input("Is transaction international? (yes/no): ").lower()

    if amount > 200000 and account_age < 6 and international == "yes":
        print("Transaction Flagged for Manual Verification")
    else:
        print("Transaction is Normal")


# 2. Income Tax Calculator
def income_tax_calculator():
    income = float(input("Enter annual income: "))
    age = int(input("Enter age: "))

    exemption = 300000 if age >= 60 else 250000
    tax = 0

    if income <= exemption:
        tax = 0
    elif income <= 500000:
        tax = (income - exemption) * 0.05
    elif income <= 1000000:
        tax = (income - 500000) * 0.20 + (500000 - exemption) * 0.05
    else:
        tax = (income - 1000000) * 0.30 + 500000 * 0.20 + (500000 - exemption) * 0.05

    print("Total Tax:", tax)


# 3. E-commerce Discount Engine
def ecommerce_discount():
    cart_value = float(input("Enter cart value: "))
    membership = input("Enter membership (Silver/Gold/Platinum): ").lower()
    festival = input("Is it festival season? (yes/no): ").lower()

    discount = 0

    if cart_value > 5000:
        discount = 10

    if membership == "silver":
        discount = max(discount, 5)
    elif membership == "gold":
        discount = max(discount, 15)
    elif membership == "platinum":
        discount = max(discount, 20)

    if festival == "yes":
        discount = max(discount, 25)

    final_amount = cart_value - (cart_value * discount / 100)
    print("Discount Applied:", discount, "%")
    print("Final Payable Amount:", final_amount)


# 4. University Admission Eligibility
def university_admission():
    percentage = float(input("Enter 12th percentage: "))
    maths = input("Did you study Mathematics? (yes/no): ").lower()
    exam_score = int(input("Enter entrance exam score: "))

    if percentage < 75:
        print("Rejected: Less than 75% in 12th")
    elif maths != "yes":
        print("Rejected: Mathematics not studied")
    elif exam_score < 80:
        print("Rejected: Entrance exam score below 80")
    else:
        print("Congratulations! Admission Approved")


# 5. Loan Approval System
def loan_approval():
    credit_score = int(input("Enter credit score: "))
    income = float(input("Enter monthly income: "))
    existing_loan = float(input("Enter existing loan amount: "))

    if credit_score < 600:
        print("Loan Rejected: Low credit score")
    elif 600 <= credit_score < 750:
        if income < 30000 and existing_loan > 500000:
            print("Loan Rejected: Income low & high existing loan")
        else:
            print("Loan Under Further Review")
    else:
        print("Loan Approved")


if __name__ == "__main__":
    print("Select Program (1-5):")
    print("1. Suspicious Transaction")
    print("2. Income Tax Calculator")
    print("3. E-commerce Discount")
    print("4. University Admission")
    print("5. Loan Approval")

    choice = int(input("Enter choice: "))

    if choice == 1:
        suspicious_transaction()
    elif choice == 2:
        income_tax_calculator()
    elif choice == 3:
        ecommerce_discount()
    elif choice == 4:
        university_admission()
    elif choice == 5:
        loan_approval()
    else:
        print("Invalid Choice")
