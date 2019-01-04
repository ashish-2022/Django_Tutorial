# Django_Tutorial

C:\Software_Development\Django_REST_framework>mkdir RestApiSample

C:\Software_Development\Django_REST_framework>ls
RestApiSample

C:\Software_Development\Django_REST_framework>cd RestApiSample

C:\Software_Development\Django_REST_framework\RestApiSample>ls

C:\Software_Development\Django_REST_framework\RestApiSample>django-admin startproject RestApiSample .

C:\Software_Development\Django_REST_framework\RestApiSample>ls
RestApiSample  manage.py

C:\Software_Development\Django_REST_framework\RestApiSample>cd RestApiSample

C:\Software_Development\Django_REST_framework\RestApiSample\RestApiSample>ls
__init__.py  settings.py  urls.py  wsgi.py

C:\Software_Development\Django_REST_framework\RestApiSample\RestApiSample>django-admin startapp quickstart

C:\Software_Development\Django_REST_framework\RestApiSample\RestApiSample>ls
__init__.py  quickstart  settings.py  urls.py  wsgi.py

C:\Software_Development\Django_REST_framework\RestApiSample\RestApiSample>cd quickstart

C:\Software_Development\Django_REST_framework\RestApiSample\RestApiSample\quickstart>ls
__init__.py  admin.py  apps.py  migrations  models.py  tests.py  views.py


C:\Software_Development\Django_REST_framework\RestApiSample>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
    
  
C:\Software_Development\Django_REST_framework\RestApiSample>python manage.py createsuperuser
Username (leave blank to use 'ashish'): django
Email address: ashish.shirodkar@outlook.com
Password:
Password (again):
Superuser created successfully.

C:\Software_Development\Django_REST_framework\RestApiSample>

