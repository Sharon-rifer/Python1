# Constant (tax rate - assumed fixed)
TAX_RATE = 0.2  # 20%

# Variables
employee_name = "Alice"
hourly_wage = 25
hours_worked = 40

# Calculate gross and net pay
gross_pay = hourly_wage * hours_worked
tax_amount = gross_pay * TAX_RATE
net_pay = gross_pay - tax_amount

# Print the results
print("Employee Name:", employee_name)
print("Hourly Wage: $", hourly_wage)
print("Hours Worked:", hours_worked)
print("Gross Pay: $", gross_pay)
print("Tax Deducted: $", tax_amount)
print("Net Pay: $", net_pay)
