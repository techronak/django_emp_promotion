from django.db import models
# Create your models here.




class employees(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField(null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField(null=True)
    groups = models.ManyToManyField('Titles')

    def __str__(self):
        return "{}".format(self.first_name)


class departments(models.Model):
    class Meta:
        unique_together = (('dept_no', 'dept_name'),)
    dept_no = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=40, null=True)

class dept_emp(models.Model):
    emp_no = models.ForeignKey(employees, on_delete=models.CASCADE, related_name='employees_department')
    dept_no = models.ForeignKey(departments, on_delete=models.CASCADE)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)


class Titles(models.Model):
    emp_no = models.ForeignKey(employees, on_delete=models.CASCADE, related_name='employees_title')
    title = models.CharField(max_length=50, null=True)
    from_date = models.DateField(primary_key=True)

class Salaries(models.Model):
    emp_no = models.ForeignKey(employees, on_delete=models.CASCADE, related_name='employees_salaries')
    salary = models.IntegerField(primary_key=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)