
### Approach For Reordering -

Here I have considered taking a very simple approach which would work fine for a few thousand entries but it would scale linearly as the number of records increase.

On each reorder operation I am taking the current position of item and the new position, at the backend I am gettting a sorted queryset bby position and then generating a map of position of all items, placing the reordered item in it's correct postion and incrementing the position of all the items below it.

Finally updating the same in database using bulk update operation.

All this logic is wrapped in transaction to avoid any conflicts when we move to multiuser scenario since more than one user could be reording at the same time.

### Multiple Users
If the multiple users are allowed to have there own order of items then we would need to move the position key to a new model and have user id, card id and position.

The reordering would work the same way but filter on the logged in user only. The listing API would return the sorted list based on current user.

Other than this I don't forsee any challenge as such since we have already applied trasaction to avoid any conflicts

Login would also be required in case we decide to have a different order for each user

### Scaling to millions of users
Based on the data that we gather we can focus on optimising reads or writes. At the moment it lookes like the data is going to be read more often than data getting reordered or added. SO for that case we should implement caching using redis or memcache

Later if needed position can be moved to redis itself and that way the reordering operation would be much faster

### *Tool , Technologies and Version*
Python>3.6
Django=4.1

Postman Documentation - https://documenter.getpostman.com/view/22874068/VUqmvJv4



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
