Lumate
======

Real Lumate project

1.)
-Save pair key from amazon to directory (I used the home directory)

-From terminal use command:
	ssh -i key-name-here ubuntu@whatever.compute.amazonaws.com

2.)
-From terminal (now that you are ssh'd in)
	sudo apt-get install git-core

3.)
-From terminal :
	sudo apt-get install python-pip

4.)
-From terminal :
	sudo pip install django

5.)
-From terminal :
	sudo apt-get update
	sudo apt-get upgrade // This one takes a little bit
	sudo apt-get install postgresql

	// Switch to superuser
	sudo su - postgres
	
	// Create new users
	createuser django_login // Then answer y for superuser

	// To get into Postgres shell
	psql

	// Give the users passwords
	alter user postgres with password 'postgres'
	alter user django_login with password 'password'
	

	// Create Database
	CREATE DATABASE django_db OWNER django_login ENCODING 'UTF8';

	// Then quit
	\q

	// Edit main control file
	sudo vim /etc/postgresql/9.1/main/pg_hba.conf

	hit i to start insert mode

	// Under #Database administrative login by Unix domain socket, add
	local	all 		django_login				trust

	esc to exit insert mode
	then :wq to (write (save) and quit)

	// Allow localhost
	sudo vim /etc/postgresql/9.1/main/postgresql.conf

	hit i to start insert mode

	// Under CONNECTIONS AND AUTHENTICATION
	// # - Connection Settings -
	uncomment listen_addresses = 'localhost'

	esc to exit insert mode
	then :wq to (write (save) and quit)

	// Restart the database server
	sudo service postgresql restart
6.) Getting Postgre to work with django
	// Install python-psycopg2
	From terminal :
	sudo apt-get install python-psycopg2


7.) Create the project
	// Verify that you have django installed and running
	python -c "import django; print(django.get_version())"

	// If that works fine then create the project
	django-admin.py startproject project_name

	// Navigate to edit settings
	cd project_name/project_name
	sudo vim settings.py

	// Edit the settings
	// Append the Engine
	'ENGINE': 'whatever.posgresql_psycopg2',
	'NAME' : 'django_db',
	'USER' : 'django_login',
	'PASSWORD' : 'password',

8.) Sync the database
	cd ../
	python manage.py syncdb
	//Create a superuser
	mine was 
	user: connor
	email: cmm863@mst.edu
	password: *******

9.) Run the server successfully to port 80
	sudo python manage.py runserver 0.0.0.0:80
	
10.) Install South to edit models and table schematics
