from faker import Faker
import json  # To create a json file                 
from random import randint  # For student id 
from django.core.serializers.json import DjangoJSONEncoder


fake = Faker()


def input_data(x):
    # dictionary 
    employee_data = {}
    for i in range(0, x):
        employee_data[i] = {}
        employee_data[i]['emp_no'] = randint(1, 1000)
        employee_data[i]['birth_date'] = fake.date_of_birth()
        employee_data[i]['first_name'] = fake.first_name()
        employee_data[i]['last_name'] = fake.last_name()
        employee_data[i]['gender'] = fake.profile('M')
        employee_data[i]['hire_date'] = fake.past_datetime()
    print(employee_data)

    # dictionary dumped as json in a json file 
    with open('employees.json', 'w') as fp:
        json.dump(employee_data, fp, sort_keys=True, indent=1, cls=DjangoJSONEncoder)


def main():
    # Enter number of students 
    number_of_employees = 1000  # For the above task make this 100
    input_data(number_of_employees)


main()