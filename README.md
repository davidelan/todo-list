# TO-DO list Creator
Full-Stack Toolkit Portfolio Project(PP4) - Code Institute

View the deployed site [here.](https://davide-todo-list-ada1093e37d7.herokuapp.com/)<br>

 *TO-DO list Creator* is a website that lets you create a TO-DO list with a list of tasks. The user can create multiple tasks and give names to each one of them. The user can, for example, have a food shopping TO-DO list with items to by at the supermarket.
 The user can create an account, login in, modify and delete the TO-DO list's items. 
 It is a full-stack Django project running on Heroku.


 ![Screenshot of the preview of application](documentation/images/all_devices_mockup.jpg)<br>

## Table of contents

- [User Experience](#user-experience)
  - [User stories](#user-stories)
- [Design](#design)
  - [Wireframes](#wireframes)
  - [Imagery](#imagery)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
- [Structure](#structure)
- [Database](#database)
- [Features](#features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Programming Languages](#programming-languages)
  - [Agile](#agile)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Github Deployment](#github-deployment)
  - [Create App](#create-app)
  - [Create database](#create-database)
  - [Create the Heroku app](#create-the-heroku-app)
  - [Create an env file](#create-an-env-file)
  - [Heroku deployment settings](#heroku-deployment-settings)
  - [Set Template directory](#set-template-directory)
  - [Heroku host allow](#heroku-host-allow)
  - [Create a Procfile](#create-a-procfile)
  - [Deployment on Heroku](#deployment-on-heroku)
- [Development](#development)
  - [Fork](#fork)
  - [Clone](#clone)
- [Credits](#credits)
  - [Images](#images)
  - [Code](#code)
  - [ReadMe](#readme)
  - [Acknowledgments](#acknowledgments)


## User Experience

This project was designed using Agile methodology, utilising the Project Board and Issues sections in GitHub<br>
The Project board can be seen [here](https://github.com/users/davidelan/projects/3/views/1).


### User stories

THe TODO list creator is meant for anyone who wants to create a todo list. <br>

User Stories with their id:  <br>

- As a Site User I can view the content of the todo list so that I can read the full text. [#2](https://github.com/davidelan/todo-list/issues/2)

- As a Site User I can create an account so that I can log in into m y account. [#3](https://github.com/davidelan/todo-list/issues/3)

- As a Site Admin/Registered User I can create todo lists' Items so that I can manage my site content. [#8](https://github.com/davidelan/todo-list/issues/8)

- As a Site Admin/Registered User I can view a todo list item so that I can view my site content. [#9](https://github.com/davidelan/todo-list/issues/9)

- As a Site Admin/Registered User I can update a todo list item so that I can manage my site content. [#10](https://github.com/davidelan/todo-list/issues/10)

- As a Site Admin/Registered User I can Delete a todo list item so that I can manage my site content. [#11](https://github.com/davidelan/todo-list/issues/11)

- As a Site Admin/Registered User I can log in to my account so that I can mange todo lists' items. [#12](https://github.com/davidelan/todo-list/issues/12)

- As a Site Admin/Registered User I can log out from my account so that no one can have access to my data. [#13](https://github.com/davidelan/todo-list/issues/13)

- As a site user I can set a task box as completed so that I can focus on non-completed tasks. [#16](https://github.com/davidelan/todo-list/issues/16)

- As a Site User I can search for a task in the task list so that I view the desired task. [#17](https://github.com/davidelan/todo-list/issues/17)

- As the superuser I can access the site's administrative features so that I have access to the admin panel. [#18](https://github.com/davidelan/todo-list/issues/18)


## Design

### Wireframes

- All devices - Landing Page Wireframe

![All devices Landing Page Wireframe](documentation/images/landing_page.png)

- All devices - Registration Wireframe

![All devices Registration Wireframe](documentation/images/registration.png)

- All devices - Task List Wireframe

![All devices Task List Wireframe](documentation/images/task_list.png)


### Imagery
 
The background image was found at Pexels and was created by [Suzy Hazelwood]:(https://www.pexels.com/photo/notebook-1226398/) It was used to create the colour palette and logo. 
The background image is a picture of a ring notebook where usually people write down todo lists.



### Colour Scheme
  
I kept the color scheme very simple and I used two different shades of green, one for the main base page (login, registration, task list and task list update and deletion) and for the complition of a task.


### Typography

[Mulish](https://fonts.google.com/specimen/Mulish) was used across the whole project with the only exception of the text "Connect with us:" in the footer in which I used the standard Arial font.<br>


## Structure 

The final database schema is the representation of the two database models that were later implemented. As you can see from the image there are more fields than what were used in the project. This is becasue I started with the idea of having multiple TODO Lists which each could contain multiple taks. I would have liked to also show the user for both categories the date of creation and update. Unfortunately I realized near the submission deadline that I would not have time to implement all the ideas and I had to revert to the simplest version. 
It is my intention to proceed with the above implementation when the course has ended.

![Final Database Schema](documentation/images/erd_todo_list.jpg)<br>

## Database<br>
I used a PostgreSQL provided by Code Institute as relational database.<br>

- **FieldTypes:**<br>
  - AutoField: An integer field that automatically increments.
  - CharField: A text field with a maximum length.
  - DateTimeField: A field for storing date and time.
  - TextField: A large text field.
  - ForeignKey: A many-to-one relationship.
  - IntegerField: An integer field.
  - BooleanField: A boolean field.

- **Relationships:**<br>
  - A User has one TODO list.
  - A User can create many Tasks in the TODO list.
  - A Task belongs to the TODO list.

## Features

 - See the landing page / login page

![See landing page](documentation/images/landing_login.jpg)


- The user can create an account

![Create an Account](documentation/images/registration.jpg)


- View todo list and all its tasks

![View todo list](documentation/images/todo_list.jpg)


- The user can create or edit a task

![Edit/Update a task](documentation/images/edit_update_task.jpg)


- The user can delete a task

![Delete a task](documentation/images/delete_task.jpg)


### Future Features
Features, which I would like to implement in the future

- The main feature that I would like to implement is to have multiple todo lists. 
- I would also like to add informnation about the date of the creation and updating of the tasks.
- It would be nice to also have a priority system which would support the user in choosing the sequence of tasks to complete
- Definitely improve the look of the app and that of the landing page

# Technologies Used

Here the list technologies used to carry out the project:

- [GitPod](https://gitpod.io/) - IDE used to create the site. To build and create this project.
- [GitHub](https://github.com/) used to save and store the files for the website.
- [Git](https://git-scm.com/) used in conjunction with Gitpod to commit code to the GitHub repository.
- [Heroku](https://www.heroku.com) was used to deploy the application.
- [Code Insitute Database Maker](https://dbs.ci-dbs.net/) PostgreSQL database hosting for this project
- [Balsamiq](https://balsamiq.com/) used to create the wireframes.
- [Lucid](https://lucid.app/) used to create the Flowchart.
- [Beautifier](https://beautifier.io/) to beautify the HTML code
- [Pexels](https://www.pexels.com/) used to find a background image for the project.
- [Browserling](https://www.browserling.com/) used to test the application on different browsers. 
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools) used to check the application for responsiveness and errors. 

# Programming Languages
Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)


# Agile

In order to develop the project using the Agile methodology, the GItHub Project Board and Issues were used.

- [Project Board](https://github.com/users/davidelan/projects/3)

# Testing

Please, go to [TESTING.md](TESTING.md) to see a detailed report of the testing of the project.


# Deployment

## Github Deployment

The entire project was stored in one repository created on GitHub, which also includes sophisticated version control capabilities.
From GitPod environment the following are the commands used to commit the the project to the repository: 

In the terminal:

- git add .
- git commit -m "my descriptive commit message"
- git push

After this the relevant files are available on GitHub.


## Create App

To create a new Django project, you use the command:

django-admin startproject project_name

This command creates a new directory with the specified project_name, containing the basic structure of a Django project, including settings, URLs, and the main manage.py script.


## Create database
Create a new external database

The database used for this project was created using the Code Institute database maker:
- [CI database maker](https://dbs.ci-dbs.net/)

- Tthe database URL is sent directly to the student email.


## Create the Heroku app

 - Sign up for Heroku and accept terms of service.

 - Click the **"Create a new app"** button.

 - Give your app a name and select the region closest to you. A name must be unique.
  

### Create an env file
Create an env.py file

- Creae a file called **env.py** in order to store private information that must not be shared. The file must saved therefore in the **.gitignore file**.

- Import os library: `import os`.

- Set environment variables in the **settings.py**:
  - **DATABASE_URL** containing the a variable related to the url of the database stored in **env.py**
  - **SECRET_KEY**: containing the a variable related to the the secret key stored in **env.py**



## Heroku deployment settings

- In the **Settings** tab in the Heroku dashboard:

- Create _Config Vars_:
  - KEY: **PORT** | VALUE: **8000**.
  - KEY: **SECRET_KEY** | VALUE: **My_Secret_Key**(that can be find in env.py)
  - KEY: **DATABASE_URL** | VALUE: The database URL created with CI databse maker (that can be find in env.py)
  

 
### Set Template directory
Set the Template directory in settings.py


    `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`


    ````
    TEMPLATES = [
    {
      ...,
      'DIRS': [TEMPLATES_DIR],
      ...,
          ],
        },
      },
    ]
    ````

## Heroku host allow
Add Heroku domain to ALLOWED_HOSTS

  ````
  ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
  ````

## Create a Procfile

`web: gunicorn family_recipe.wsgi`


## Deployment on Heroku

- Click on the **"Deploy"** section on the top of the page.

- Select **GitHub** as deployment method and click the **"Connect to GitHub"** button.

- Search for the relevant GitHub repository for my project. 

- Click **"Connect"** to link up Heroku app to the GitHub repository.

- Click on **"Deploy Branch"**.



# Development 

## Fork

- In my **GitHub** repository project, [my PP4 project](https://github.com/davidelan/todo-list):

- In the top-right corner of the page, click **Fork**.

- Type some new name into the "Repository name" field to distinguish your fork from the upstream repository.

- Click **Create Fork**.

- The repository has been forked in the user account and can be developed further.


## Clone

In order to create a clone of the project:

1. Click on the code tab, left of the Gitpod tab
2. To the right of the repository name, click the clipboard icon
3. In the IED open GitBash
4. Change the working directory to the location you prefer
5. Add Git Clone with the copy of the repository name
6. Clone has been created


# Credits

## Images

- The background image was found at Pexels. The author is Suzy Hazelwood and can be found here [Suzy Hazelwood](https://www.pexels.com/photo/notebook-1226398/)


## Code

- ***My Todo List project is based on the tutorial from Desphixs [*Django To Do List App With User Registration & Login*](https://www.youtube.com/watch?v=GRz3pcU89qU)***
  - This was the main source of knowledge for the creation of the project.

- The Python tutorial on how to create a Todo List was also used a a source of inspiration and to understand the connection between the different parts of the Django project: [*Manage Your To-Do Lists Using Python and Django*](https://realpython.com/django-todo-lists/)


- These websites where also often consulted for better understanding and problem solving: <br>
  - [Google](www.google.com)
  - ***[Stack Overflow](https://stackoverflow.com/)***
  - ***The Code Insitute Slack Community***
  - [W3schools](https://www.w3schools.com/)
  - [forum djangoproject](https://forum.djangoproject.com/)
  

## ReadMe

- This README.md file was created with the inspiration of 3 different read me files:

- [*from Mark Daniel*](https://github.com/markdaniel1982/MD82-P4/blob/main/README.md)
- [*from Dajana Isbaner*](https://github.com/queenisabaer/wishlist/blob/main/README.md)
- [*from Adrian Skelton*](https://github.com/adrianskelton/adrianproject4/blob/main/README.md)

Thank you guys!!!


## Acknowledgments

- I would like to say a big thank you to my mentor Jubril Akolade who always pointed me to the right direction, for his availability and for giving me motivation throuhout hte whole project. 


- A big thanks again to all the other students in Slack that have helped me and inspired me greatly and that with their Slack contributions have helped me solve a lot issues many, many times.

- Thanks a lot to Kay Welfare for her incredible support that I get every Thursday. 

- Last but not least, a huge thanks ro my partner who has supoprted me, motivated me and put up wiht me in some frustrating moments.


**This is for educational use.**