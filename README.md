Django App

A IDE and the docker app is required to run this.

This app can be run through any IDE that can run the python language

A login page should be presented upon entering.

Register create a username and login


To run the Django development server, type the command python manage.py runserver in your terminal of the Django project and hit enter. If everything is okay with your project, 
Django will start running the server at localhost port 8000 (localhost:8000) and then you have to navigate to that link in your browser. While the server is running, 
Django will print out in real-time all the actions that are taking place on the site. More than that, Django also offers more methods to customize the way the server will be running, for example, 
it allows you to change the port and IP address of the server, or prevent the server from reloading after some change has been done in the Project’s code. That’s what we will explore in the sections to come.

Use pip install -r requirements.txt to install requirements lised in requirement.txt.

Use docker desktop or docker play ground to run dockerfile or image, in docker playground run CMD 

to build webpage:
docker build -t django . 

tag = latest

to pull the webpage:
docker pull keenanhansrajh/django:tag

to run on desktop:
docker run -d -p 80:80 keenanhanrajh/django


