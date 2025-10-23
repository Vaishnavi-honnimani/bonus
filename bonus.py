

salary = float(input("Enter your salary: ₹"))
bonus = salary * 0.10
total_salary = salary + bonus
tax = total_salary * 0.05
final_salary = total_salary - tax

print(f"Original Salary: ₹{salary}")
print(f"Bonus (10%): ₹{bonus}")
print(f"Salary after Bonus: ₹{total_salary}")
print(f"Tax Deducted (5%): ₹{tax}")
print(f"Final Salary after Tax: ₹{final_salary}")
