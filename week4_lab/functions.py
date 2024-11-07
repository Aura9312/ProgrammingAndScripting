def avg(ageslist:list):
    """

    :param ageslist:
    :return:
    """
    sum_ages = sum(ageslist)
    num_ages = len(ageslist)
    return sum_ages / num_ages

list_of_ages = [20,21,24,13,15,19,22]
ave_age = avg(list_of_ages)
print(f"The average age is {ave_age}")

def employee_pay():
    """
    :return: the employee pay in float in currency £
    """
    hourly_rate = float(input(f"Please enter your hourly rate, e.g. 10.59: "))
    number_hours_worked = float(input(f"please enter your number of hours worked, e.g. 21.5: "))
    emp_pay = hourly_rate*number_hours_worked
    emp_pay = f'£{emp_pay}'
    return emp_pay


# Test employee_pay code
empy_pay = employee_pay()
print(f'Employee Pay is {empy_pay}')
