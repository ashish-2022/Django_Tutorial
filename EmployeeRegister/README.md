ashirodkar@quartz Django_Projects]$ django-admin startproject EmployeeRegister  


[ashirodkar@quartz Django_Projects]$ find .  
.
./EmployeeRegister  
./EmployeeRegister/manage.py  
./EmployeeRegister/EmployeeRegister  
./EmployeeRegister/EmployeeRegister/__init__.py  
./EmployeeRegister/EmployeeRegister/settings.py  
./EmployeeRegister/EmployeeRegister/urls.py  
./EmployeeRegister/EmployeeRegister/wsgi.py  
[ashirodkar@quartz Django_Projects]$  

[ashirodkar@quartz Django_Projects]$ cd EmployeeRegister/  
[ashirodkar@quartz EmployeeRegister]$ ls  
EmployeeRegister  manage.py  
[ashirodkar@quartz EmployeeRegister]$ python manage.py startapp webapp  
[ashirodkar@quartz EmployeeRegister]$ find .  
.  
./manage.py  
./EmployeeRegister  
./EmployeeRegister/__init__.py  
./EmployeeRegister/settings.py  
./EmployeeRegister/urls.py  
./EmployeeRegister/wsgi.py  
./EmployeeRegister/__init__.pyc  
./EmployeeRegister/settings.pyc  
./webapp  
./webapp/__init__.py  
./webapp/admin.py  
./webapp/apps.py  
./webapp/models.py  
./webapp/tests.py  
./webapp/views.py  
./webapp/migrations  
./webapp/migrations/__init__.py  
[ashirodkar@quartz EmployeeRegister]$  


Create model for your webapp in webapp/models.py  


[ashirodkar@quartz EmployeeRegister]$ python manage.py makemigrations  
Migrations for 'webapp':  
  webapp/migrations/0001_initial.py  
    - Create model employees  
[ashirodkar@quartz EmployeeRegister]$  

[ashirodkar@quartz EmployeeRegister]$ python manage.py migrate  
Operations to perform:  
  Apply all migrations: admin, auth, contenttypes, sessions, webapp  
Running migrations:  
  Applying contenttypes.0001_initial... OK  
  Applying auth.0001_initial... OK  
  Applying admin.0001_initial... OK  
  Applying admin.0002_logentry_remove_auto_add... OK  
  Applying contenttypes.0002_remove_content_type_name... OK  
  Applying auth.0002_alter_permission_name_max_length... OK  
  Applying auth.0003_alter_user_email_max_length... OK  
  Applying auth.0004_alter_user_username_opts... OK  
  Applying auth.0005_alter_user_last_login_null... OK  
  Applying auth.0006_require_contenttypes_0002... OK  
  Applying auth.0007_alter_validators_add_error_messages... OK  
  Applying auth.0008_alter_user_username_max_length... OK  
  Applying sessions.0001_initial... OK  
  Applying webapp.0001_initial... OK  
[ashirodkar@quartz EmployeeRegister]$  


[ashirodkar@quartz EmployeeRegister]$ python manage.py createsuperuser  
Username (leave blank to use 'ashirodkar'): django  
Email address:  
Password:  
Password (again):  
Superuser created successfully.  
[ashirodkar@quartz EmployeeRegister]$  

[ashirodkar@quartz EmployeeRegister]$ python manage.py runserver xx.xx.xx.xxx:8000  

At this point we can add remove users using admin page.  

Write Serializers webapp/serializers.py  
Next write Views in webapp/views.py  


