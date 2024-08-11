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
  - [Typography](#typography)
- [Structure](#structure)
- [Database](#database)
- [Features](#features)
- [Bugs](#bugs)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Tools](#tools)
  - [Frameworks](#frameworks)
  - [Libraries and modules](#libraries-and-modules)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Lighthouse Test](#lighthouse-test)
  - [Manual testing](#manual-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Automated Testing](#automated-testing)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Local deployment](#local-deployment)
  - [Forking this GitHub repository](#forking-this-github-repository)
  - [Clone this repository](#clone-this-repository)
  - [Create PostgreSQL using Code Institute Database Maker](#create-postgresql-using-code-institute-database-maker)
  - [Gmail](#gmail)
- [Credits](#credits)
  - [Content](#content)
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