from django.contrib import admin
from .models import employees, departments, dept_emp, Titles, Salaries



# Register your models here.
admin.site.register(employees)
admin.site.register(departments)
admin.site.register(dept_emp)
admin.site.register(Titles)
admin.site.register(Salaries)

