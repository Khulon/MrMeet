<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="">
    <img src="./mrmeethtml/images/logo.png" alt="Logo" width="200" height="auto">
  </a>

<h3 align="center">MrMeet</h3>

  <p align="center">
    Your one stop telebot uncle to solve your group's meetup needs
    <br />
    <a href= "https://github.com/Khulon/MrMeet" ><strong>Explore our documentation »</strong></a>
    <br />
    <br />
    <a href="https://mrmeet-1.ldogsloop.repl.co/login.php">View Demo</a>
 
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#level-of-achievement">Level of Achievement</a></li>
        <li><a href="#project-scope">Project Scope</a></li>
        <li><a href="#problem-motivation">Problem Motivation</a></li>
        <li><a href="#user-stories">User Stories</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

### Level of Achievement

<p>Gemini</p>

### Project Scope

<p>Brief: Mr.Meet,  your friendly singaporean uncle bot who helps your group to meet more easily and be that uncle to remind you of your dreaded deadlines and milestones! It is both a telegram bot and a web app for a visual overview</p>

<p> We hope to make a Telegram Bot that makes initiating and planning work or casual meetups more smooth sailing, and that can remind its users of objectives and milestones to prompt action-taking. </p>



### Problem Motivation

<p>With many modules with project work in nus, students seem to have trouble keeping track of project deadlines, group’s milestones and also have trouble with initiating meetups with project mates. </p>

<p>Taking these into account, we realised, why not take this opportunity to solve that and also make initiating meetups more efficient and fun.
</p>

<p>There are two parts to our solution.First a telegram bot with a singaporean uncle persona who produces meetup options and facilitate the project along the way.Second is a web app that helps to visualize the overview of the project that includes timeline and relevant links.
</p>

<p>With this, we can make projects not only more efficient and fun but also you’ll never miss a deadline again.</p>



### User Stories 

#### User
- [ ] As a student who has many individual deadlines and submissions to keep track of, I want to be able to keep track of my project progress and future milestones easily.

- [ ] As a student who has a very busy schedule, I want to be able to find common free times to work on projects with my group mates easily.
- [ ] As a student who is shy and awkward, especially with people I have never met, I want to be able to have someone else that will help remind my group mates of objectives that need to be done soon.
- [ ] As a person who wants to organise an event with friends, family and even colleagues, I want to be able to know which days would be best for everyone.

#### Admin
- [ ] As an admin who manages the telegram bot adn web app, I want to be able to add, update and delete any features to improve and update for better user experience.


### Project Scope

<p>The scope of our Orbital project can be broken down into 3 parts - <strong>Telegram Bot, Webapp and extensions</strong></p>
<p>Telegram Bot - <strong>Set Objectives, Meetups, Overview and Retrieving Login Details</strong></p>
<p>Webapp - <strong>User Login, Dashboard</strong></p>
<p>Extensions - <strong>Sync telegram bot and webapp, Calendar</strong></p>

#### Telegram Bot - Set Objectives and Milestones. Initiate Meetup. Overview and Retrieving Login Details

<li>
  <ol>
    <strong>Set Objectives and Milestones</strong>
    <p>Set up frontend - popup options and /objectives command to start setting up objectives.Create the flow of commands and responses for user experience</p>
  </ol>
  
  <ol>
    <strong>Initate Meetup</strong>
    <p>Find a common time for your group using the poll feature. Decided to split into three options - this week, next week and custom.</p>
  </ol>
  <ol>
    <strong>Backend Database</strong>
    <p>Set up database for objectives and login - keep track of the objectives and milestones.Create chat ID and password.Each group has one unique chat Id and password</p>
  </ol>
  <ol>
    <strong>Retrieiving Login Details</strong>
    <p>Click on /Webapp for unique chat Id and password given to each group.Convenient and easy</p>
  </ol>
  <ol>
    <strong>Singaporean Uncle Persona</strong>
    <p>User experience - incorporate singlish into the responses to make it fun</p>
  </ol>
</li>


#### Webapp - User Login, Dashboard

<li>
  <ol>
    <strong>User Login</strong>
    <p>Simple Chat Id and Login using the details from /webapp from telegram bot</p>
      
  </ol>
    <ol>
    <strong>DashBoard - Icon</strong>
    <p>MrMeet Icon to redirect to telegram Bot</p>
      
  </ol>
      <ol>
    <strong>Dashboard - Overview of Objectives</strong>
        <p>User can add or edit their objective details.Includes a popout calendar for datelines</p>
    
  </ol>
  
      <ol>
    <strong>DashBoard - Add or edit milestones </strong>
    <p>User can add or edit their milestones in each objectives.Includes a popout calendar for datelines</p>
      
  </ol>
  
    <ol>
      <strong>Logout Button</strong>
      <p>Users can logout  to the Login page.</p>
    </ol>
    </li>
  
  #### Extensions - Sync telegram bot and webapp, Calendar
  <li>
   <ol>
    <strong> Backend - Sync objectives and meetings</strong>
    <p>Objectives and Meetings are consistent between telegram bot and </p>
      
  </ol>
  <ol>
      <strong> Calendar </strong>
      <p>Users can visulaise their meetings on the calendar under the meetings tab.</p>
    </ol>
</li>

### Built With

- [MySQL](https://www.mysql.com)
- [JQuery](https://jqueryui.com/)
- [Heroku](https://www.heroku.com)
- [PopSQL](https://popsql.com)
- [Replit](https://replit.com/~)
- [TailwindCSS](https://tailwindcss.com)
- HTML, Javascript, CSS, PHP


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

<a href="https://mrmeet-1.ldogsloop.repl.co/login.php"><strong>Check out the website»</strong></a>

- [x] User Login Page
- [x] Telegram Bot - Create and edit objectives and miletones
- [x] Overview
- [X] ChatId and password ( Generating and retrieving)
- [X] Navigation bar
- [X] Webapp Objectives and Milestones frontend create and edit Feature
- [X] Sync project details to the common database
- [X] Calendar Feature

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

<p>Darren Chang - darrenchang2@gmail.com</p>
<p>Cleon Liew - cleonliew@gmail.com</p>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

<!-- ## Acknowledgments

- []()
- []()
- []()

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- [contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username-->
