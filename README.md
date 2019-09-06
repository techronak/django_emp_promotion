# Task 1

###Created Porject and app:
####perquisites:

* django-admin startproject captech
* django-admin startapp capfrontech
* pip install Django==2.2.1
* pip install  djangorestframework==3.10.2
* pip install  mysqlclient==1.4.4*
* mysql workbentch 
* configuration capfrontech application with captech project.

#### Using databse
* mysql database

#### Task 1 databases

created database in models representing databases and
using by makemigrations and  Migrate Models datanase:

* python manage.py makemigrations
* python manage.py migrate

[0001: employees],
[0002: departments],
[0003: dept_emp],
[0004: Titles],
[0005: Salaries],

Serializers: They're used to convert the data sent in a HTTP request to a Django object and a Django object to a valid response data.

Now, here we can nested two types: First is used nested serializer and second is entring by using admin panel.

### Nested Serializer Example:

we can see in **employee_hireSerializer**  how can i nested models in Serializer.
and we can go also django admin panel:

Username: admin
password: admin123

we can put our values.

Now redirect our response in Post Api.

#### we are using genric view It will create redirect our api on post.

import module: from rest_framework import generics

** Insert 1000 + employee data 

Insert data used inside populate_capfrontech.py 

#### Fake library

### Run:

python: populate_capfrontech.py 



Task 2: insert and populate data.



 
