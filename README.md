### *Tool , Technologies and Version*


Postman Documentation - https://documenter.getpostman.com/view/22874068/VUqmvJv4



Python>3.6
Django=4.1


### *Step for setup and Run the file*

1. Make folder
	
		mkdir folder_name

2. Go to folder
	
		cd folder_name

2. Clone code from github 


3. Make environemt

		virtualenv env

4. Activate environment

		a. env\Script\activate # for window

		b. source env/bin/activate #for mac and ubuntu

5. Install all requirement

		pip install -r requirements.txt

6. Migrate project for propagating changes we make to our models 

		python manage.py migrate

7. Create a User

		python manage.py createsuperuser --username user --email user@example.com

8. Generate a Token, It will be needed for running API

		python manage.py drf_create_token user

9. Run project

		python manage.py runserver