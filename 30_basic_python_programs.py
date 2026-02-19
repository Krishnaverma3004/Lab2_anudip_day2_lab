
# =============================
# 10 Iteration Programs
# =============================

# 1. Print numbers 1 to 10
for i in range(1, 11):
    print("1 to 10:", i)

# 2. Print even numbers 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print("Even:", i)

# 3. Sum of first 10 numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum of first 10 numbers:", total)

# 4. Factorial of 5
fact = 1
for i in range(1, 6):
    fact *= i
print("Factorial of 5:", fact)

# 5. Multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# 6. Reverse numbers from 10 to 1
for i in range(10, 0, -1):
    print("Reverse:", i)

# 7. Count digits in number
num = 12345
count = 0
while num > 0:
    num //= 10
    count += 1
print("Digit count:", count)

# 8. Print square of numbers 1 to 5
for i in range(1, 6):
    print("Square:", i*i)

# 9. Print odd numbers 1 to 15
for i in range(1, 16):
    if i % 2 != 0:
        print("Odd:", i)

# 10. Fibonacci series (first 5 terms)
a, b = 0, 1
for i in range(5):
    print("Fibonacci:", a)
    a, b = b, a + b


# =============================
# 10 Selection Statement Programs
# =============================

# 11. Check positive, negative or zero
x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# 12. Check even or odd
y = 7
if y % 2 == 0:
    print("Even")
else:
    print("Odd")

# 13. Largest of two numbers
a, b = 15, 20
if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

# 14. Largest of three numbers
a, b, c = 5, 9, 3
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 15. Check leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 16. Check voting eligibility
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# 17. Check character is vowel
ch = 'a'
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 18. Grade calculation
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# 19. Check divisible by 5 and 11
num = 55
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")

# 20. Check smallest of two numbers
a, b = 4, 9
if a < b:
    print("Smallest:", a)
else:
    print("Smallest:", b)


# =============================
# 10 Arithmetic Operator Programs
# =============================

# 21. Addition
print("Addition:", 10 + 5)

# 22. Subtraction
print("Subtraction:", 10 - 5)

# 23. Multiplication
print("Multiplication:", 10 * 5)

# 24. Division
print("Division:", 10 / 5)

# 25. Modulus
print("Modulus:", 10 % 3)

# 26. Exponentiation
print("Power:", 2 ** 3)

# 27. Floor Division
print("Floor Division:", 10 // 3)

# 28. Area of rectangle
length, width = 10, 5
print("Area of rectangle:", length * width)

# 29. Simple Interest
p, r, t = 1000, 5, 2
si = (p * r * t) / 100
print("Simple Interest:", si)

# 30. Average of three numbers
a, b, c = 10, 20, 30
avg = (a + b + c) / 3
print("Average:", avg)
