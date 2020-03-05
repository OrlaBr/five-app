
# FIVE


‘FIVE’ is a wellness website/app focused on children and young teens that suffer from anxiety and stress. A much simpler format than current wellness apps, with the focus on the users own self-prescribed forms of ‘mindfulness’. Too many apps come with pre-prescribed ‘meditation’ routines that are an adults idea of what would be good for young teens, rather than creating an app that teens can use and edit themselves to suit their own personal needs.
The principles behind the design are based on a simple ‘task manager app’, the user can input, edit, delete and personalise mindfulness routines that work. The inspiration for FIVE came from the 5 steps of a simple yet effective grounding exercise. Seeing many routies come in ‘5’ steps, 5 breaths, etc, I created FIVE as a simple app for young teens.
The site was built using Gitpod, Github and Heroku. 

You can see the deployed Heroku site here: https://five-5.herokuapp.com/

------

## Table of Contents:
1. [Project outline](#project-outline)
2. [User Experience](#user-experience)
3. [Design](#design)
4. [Features](#features)
5. [Technologies](#technologies)
6. [Testing](#testing) 
7. [Deployment](#deployment)
8. [Future Development](#future-development)
9. [Credits](#credits)
10. [Acknowledgements](#Acknowledgements)

***

## Project Outline
This website/app deploys all my course learning to date with the Code Institute. The elements I used in creating this website, are all practical techniques I have been learning, working through the Data Centric modules of the Full Stack Developer Bootcamp.

***

## User Experience

### Research:
I carried out some research on creating apps for children and teens, and found lots of great websites and articles, (links and further reading below).
 - https://www.toptal.com/designers/interactive/guide-to-apps-for-children
 - https://www.invisionapp.com/inside-design/building-apps-for-children/
 - https://www.uxmatters.com/mt/archives/2014/07/design-for-kids-digital-products-for-playing-and-learning.php

 <img src="ux/kid-toptal.jpg" height="300" title="graphic with drawing of child and points about kids using apps">
 (graphic from toptal article, link above)

 Learning outcomes include using clean design with bright colours, simplicity. Obvious consistency across the design, a reason to use the app, let them be able to make mistakes, and easily fix them. A learning process through using the app.

### User Stories:
The app is a simple mindfulness app, that focuses more on storing information, then giving information. Children that suffer from anxiety are regularly taught exercises in grounding, and breathing, to help calm them down. By the time they get to be young teens, they have not just forgotten the steps of these exercises, they don’t want to do silly ‘children’s exercises’, and they certainly don’t want to listen to an adult, in particular their parents nagging them about remembering to do their grounding exercises. This app is for them. 

_For the Generic User:_

I designed this app with a particular type of user in mind. A young teen, who suffers from anxiety.  They are old enough to have a mobile phone and are fairly tech savvy, particularly when it comes to apps. They are old enough to almost hate their parents, and not want to listen to them, or any other adult talk about anxiety. They could have suffered from anxiety for years, or are newly anxious, they have been taught grounding and breathing exercises and are sick to death of adults talking about ‘mindfulness’. However much they hate ‘mindfulness’, they know it can work, however, in the heat of the moment, they tend to forget the exercises, and hate feeling vulnerable and asking for help. (Just like adults, this app can be used by adults too.)

Potential use of the app:
 - Use the calming grounding and breathing exercises to help soothe anxious feelings
 - Personalize the app, using it as a safe place to store mindfulness exercises that they know work
 - Use the app to store random lists of things they find funny, that make them smile.The very act of getting the phone out, and using the app, could be a first step in helping relieve the anxiety.

Practical use of the app. The user:
- Can read and use the exercises already submitted
- Can edit the existing categories and add/or delete new personalized ones
- Can edit existing exercises and and add/or delete new  personalized ones
 
_For the Developer:_

As a developer, I wanted to create a fully responsive app, using CRUD operations manipulate data, to get, post and store information from a database
 - This website would help me practice my new coding skills, develop logic and understanding of data centric application.
 - Development of coding skills using programming languages, frameworks and databases, to ways to create a website that is simple, extremely user friendly, with easy navigation, and yet capable of being a useful function website. To misquote William Morris
“Have nothing in your phone that you do not know to be useful, or believe to be beautiful.”
 - The design for this website/app was mobile first. It was designed to be a phone application, while still functioning on larger screens.

 [image on mobile and desktop]

----

## Design

#### Strategy & Scope:
The website is designed to have a minimal and clean interface, using bright clean colours. A landing welcome page, with a series of linked pages for the different actions which include retrieving, iterating, editing, adding and deleting information.

_Style:_
 - Design - minimalist, clean design
 - Fonts - I used Google Fonts to personalize the text. 
 - Color Scheme - The color scheme is simple, and kept to a minimum to ensure full eligibility. 
[add image of colour scheme]

_Structure, Skeleton & Surface:_
Keeping the pyramid of interface success, 'user - utility- usability',  from my last project, and my user story in mind, simplicity and ease of use were the most important design elements, when creating the wireframe and mock up. Keeping images to a minimum, with simple explanations of how to use the site, with a very deliberate colour scheme and simple fonts. 

_Wireframing:_

I created a wireframe for this website using Balsamiq
[thumbnail image of wireframe]
Link to PDF of wireframe

_Detailed mockup:_

I used Canva to create a more detailed mockup of the website, in mobile and desktop view
<img src="ux/five-landing-page.jpg" height="300" title="graphic of landing page of five app">

 - PDF of desktop app mockup -- PDF of <img src="https://github.com/OrlaBr/five-app/blob/master/ux/five-mockup.pdf" alt="pdf mockup of five app desktop layout">

<img src="ux/mobile-mock-up.jpg" height="300" title="graphic of mobile landing page of five app"><img src="ux/mobile-mock-up2.jpg" height="300" title="graphic of mobile adding entry section of five app">


 - PDF of desktop app mockup -- PDF of <img src="https://github.com/OrlaBr/five-app/blob/master/ux/five-mobile-mockup.pdf" alt="pdf mockup of five app mobile layout">

_Database Schema:_

I used Canva to create the database schema of the app

<img src="ux/five-database-schema.jpg" height="300" title="databases schema">


[Back to Top](#table-of-contents)

----

## Features 


#### Existing Features
 - Opens on a landing page
 - Series of html files created and linked in a logical format
 - Connected to MongoDB database
 - Links to a html page with a sample of records with the option to add or edit records 
 - User is able to view the existing data - ‘Our 5’
 - User is able to add/edit categories records ‘Add new Category’’
 - User is able to add/edit names of records ‘ Add your own 5’
 - User is able to edit/delete a record entry ‘Edit Five’
 - User is able to see all entries including their own ‘Our 5’
 - User is able to read about the app ‘About’
 - User can navigate the app using the top nav bar on large screens and hamburger toggle side navbar

 
 ----

## Technologies
- Programming languages: 
    - HTML5 - used to build the foundation of the app and includes links to Materialize, Materialize JS, CSS, and Google Fonts.
    - CSS3 - styling
    - Javascript - interactive functionality to run Materialize framework
    - Python - backend functionality connecting html pages, Flask with the cloud database.
 - CSS Framework: <a href="https://materializecss.com/">Materialize</a>
 - Code Editor: <a href="https://gitpod.com">Gitpod</a> ~ I used Gitpod to build the full website. 
 - Web Application: <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a>
 - Database  <a href="https://www.mongodb.com/">MongoDB</a> 
 - Hosting: 
            * <a href="https://github.com">Github</a> ~ Github is where I am hosting my deployed static website
            * <a href="https://www.heroku.com/">Github</a> ~ Heroku is where I am hosting my deployed dynamic website
 

*Other web applications used:*

- <a href="https://www.canva.com/">Canva<a/> - to create a detailed mock-up
- <a href="https://www.adobe.com/">Adobe Photoshop<a/> - to edit the photographs
- <a href="https://fonts.google.com/">Google Fonts<a/> - stylesheet linked to customize fonts


---
## Building	

#### Website Build
Before starting to build the app in Gitpod, I needed to create a new database in MongoDb. I created the database 'five-app' and started a collection. By doing this before starting the app build, through the MongoDB cloud interface, it gave me something to work with when creating the data retrieval in the html pages. After setting up the database, I created a collection of categories and tasks. The categories would hold the tasks, the tasks would hold a name and description. Once I had my pages and connections set up, it was then easy to add data to the database from Gitpod

```{"_id":{"$oid":"5e54de3e1c9d44000065f8dd"},
"category_name":"Grounding"
"task_name":"5 Senses",
"task_description":" 5 things you see, 4 things you hear, 3 things you smell, 2 things you can touch, 1 thing you taste"}
```

The website was built using Gitpod. I relied heavily on Code Institute tutorials in creating the basic build, following the principles of the task manager app. One of the reasons I followed the tutorials again, was to make sure I understood them fully, especially in relation to using Python and Flask. The functionality of my website is the same as a task manager app, in relation to CRUD operations. Once I had the basic functionality working, I was able to personalize it to suit my project.

#### Sections Build

Starting with Python, I created a py file. I then created a series of html pages that would perform the CRUD operations that I wanted the user to be able to do, following my database schema and mockups. I used environmental variables to connect to my MongoDB database, to hide my password.

Once I had the basic operations of the data manipulation working I created a html file, and using Flask and Python, built up the website with the necessary html files. I styled the pages initially with standard Materialize CSS formatting.

Once I had the functionality of the site, and all the CRUD operations in place, I started personalizing the styling of the site, using CSS. Working initially from the base.html file, and then working through each html file to create the uniformity I wanted.
