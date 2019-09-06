from rest_framework import serializers, fields
from .models import *


class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = dept_emp
        fields = '__all__'

class titlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = ('emp_no', 'title', 'from_date')



class salariesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Salaries
        fields = ( 'emp_no','salary', 'from_date', 'to_date')




class employee_hireSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    employees_salaries = salariesSerializer(many = True, read_only=True)
    employees_department = departmentSerializer(many = True, read_only=True)
    employees_title = titlesSerializer(many = True, read_only=True)



    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = employees
        fields = ( 'birth_date', 'emp_no', 'first_name', 'last_name', 'gender',  'hire_date', 'employees_salaries', 'employees_department', 'employees_title')
     


