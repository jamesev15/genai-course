def calculate_salary(daily_wage):
    days_worked = 30
    total_salary = daily_wage * days_worked
    return total_salary

# Example usage
daily_wage = 100  # Example daily wage
print(f"Total salary for 30 days: ${calculate_salary(daily_wage)}")


def calculate_salary_for_women(daily_wage, gender):
    days_worked = 30
    if gender.lower() == 'female':
        daily_wage *= 0.9  # Assuming a 10% reduction for women
    total_salary = daily_wage * days_worked
    return total_salary

# Example usage
daily_wage = 100  # Example daily wage
gender = 'female'
print(f"Total salary for 30 days for {gender}: ${calculate_salary_for_women(daily_wage, gender)}")