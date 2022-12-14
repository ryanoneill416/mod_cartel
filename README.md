<a id="top" href="https://mod-cartel.herokuapp.com/" target="_blank"><img src="static/images/mc-mainscriptpurple-removebg-preview.png"></a>
<h2>The car meet-up that never sleeps! Join the community and connect with like-minded individuals globally ;)</h2><br>


<h1 id="contents">Table of Contents</h1>

- [Intro](#intro)
 - [User Experience - UX](#user-experience)
   - [User Stories](#user-stories)
   - [Agile Methodology](#agile-methodology)
   - [The Scope](#the-scope)
- [Design](#design)
   - [Colours](#colours)
   - [Typography](#typography)
   - [Media](#media)
   - [Database Schema](#database-schema)
   - [Wireframes](#wireframes)
- [Features](#features)
   - [Home Page](#home-page)
   - [Desktop Navigation](#desktop-navigation)
   - [Mobile Navigation](#mobile-navigation)
   - [Add Build Functionality](#add-build)
   - [Member Showcase](#showcase)
   - [Build Details](#build-details)
   - [Build Comments Section](#build-comments-section)
   - [My Garage](#my-garage)
   - [Future Features](#future-features)
- [Technology](#technology)
   - [Languages](#languages)
   - [Frameworks / Libraries / Programs](#frameworks)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

<h1 id="intro">Project Intro</h1>

This is my fourth portfolio project as part of my Full-Stack Software Development Diploma. Mod Cartel is a social app for car enthusiasts to connect with and inspire others with the cars they've built. The app allows users to post the cars they've built, as well as like, comment and save the builds that have been posted by other members of the community. Users have full CRUD functionality and can manage their cars in their dedicated 'My Garage' page.

<a href="https://mod-cartel.herokuapp.com/" target="_blank"><h2>Check it out for yourself here!</h2></a><br><br>

<img src="docs/readme_images/responsiveness.png">

<h1 id="user-experience">User Experience Design</h1>

<h2 id="user-stories">User Stories</h2>

As an unauthenticated user, I can:

- Navigate around the application and efficiently view all application content in a pleasant manner.
- Use the call-to-action on the homepage or the navigation link to become a member.
- View all posted member builds in the 'Showcase' as well as the 'Trending Builds'.
- I can view the build details in full.
- I can view how many likes a build has gotten.
- I can view all comments made on a specific build.
- I can use the footer to join the community social media pages and the secondary navigation links.

As an authenticated user, I can:

- Perform all of the same tasks that an unauthenticated user can.
- I can quickly post a new build by the call-to-action on the home page.
- I can like and unlike member builds.
- I can comment on posted builds.
- I can delete the comments I have made on a posted build.
- I can save and unsave member builds.
- I can view the save builds in the 'Showcase' in the 'Saved Builds' tab.
- I can utilise the 'My Garage Page'.
- I can edit existing builds to ensure they are up to date with reality.
- I can delete builds that I no longer want to showcase.

As a superuser / staff member, I can:

- Perform all of the previously mentioned tasks above.
- I can delete any comments that have been made in the application itself.
- I can delete posted builds.
- I can edit posted builds.
- I can edit comments that have been posted.
- I can mark a build as featured so it will show in the 'Member Spotlight' section of the homepage.
- I can add a featured excerpt to a featured post if I wish for this to be displayed when the build is highlighted.

<h2 id="agile-methodology">Agile Methodology</h2>

Agile methodology was used in planning the development of Mod Cartel. This was done through a project kanban board embodying a prioritisation model which can be found <a href="https://github.com/users/ryanoneill416/projects/5" target="_blank">Mod Cartel User Stories</a>

Issues were used to create User Stories that were deemed one of the following: Needs to have, Should have, Could have. Each User Story had a clear title and action.

3 'Could Have' features were not implemented due to time constraints and the feautured not having an effect on the required assessment criteria. These were in relation to an additional 'Events' page where events would be posted and organised by staff. Each would allow commenting and registration up to a certain number of capacity.

<h2 id="the-scope">The Scope</h2>

- To provide users with a pleasant and efficient experience when using the Mod Cartel application.
- To provide users with a visually appealing domain which is intuitive and follows convention.
- To provide an application with a dedicated focus and target audience.
- To provide permissions for members to access additional functionality such as posting, commenting, liking and saving content.
- To provide an application where non authenticated users can still use it effictively in exploring what it has to offer, not being behind a mandatory sign-up roadblock.
- To provide a space for members to manage their own builds as well as save other builds they are inspired by for future easy visitation.

<a href="#top">Back to Table of Contents</a>

<h1 id="design">Design</h1>

<h2 id="colours">Colours</h2>

- I opted for a dark themed application utilizing a linear path of very dark to light grey background colours(#121212 - #181818 - #191919 - #282828).
- The chosen application accent color is a shade of lilac, this is used for various elements such as the main logos, various transition effects, horizontal rules and buttons etc. (#d383f8).
- Font color was pure white (#ffff), used in conjunction with varying opacities in order to differentiate importance of text.

<h2 id="typography">Typography</h2>

- The typography used was installed using Google Fonts.
- Headings are using the 'Bebas Neue' font.
- General bodies of text are using 'Montserrat'.
- 'Sans-serif' is being used as a fall-back option if Google Fonts fails to load in unforeseen circumstance.

<h2 id="media">Media</h2>

- All images used in the application are from both <a href="https://unsplash.com/">Unsplash</a> and <a href="https://www.pexels.com/">Pexels</a>.
- The Mod Cartel logos and branding are custom created by myself :)
- The database schema and wireframes were made using <a href="https://balsamiq.cloud/">Balsamiq</a>.

<h2 id="database-schema">Database Schema</h2>

![Database Schema](docs/database_schema/DB%20Schema.png)

<h2 id="wireframes">Wireframes</h2>

<a href="https://github.com/ryanoneill416/mod_cartel/blob/main/docs/wireframes/Desktop%20Home.png" target="_blank">Home Page Wireframe (Desktop)</a>

<a href="https://github.com/ryanoneill416/mod_cartel/blob/main/docs/wireframes/Desktop%20Showcase.png" target="_blank">Showcase Page Wireframe (Desktop)</a>

<a href="https://github.com/ryanoneill416/mod_cartel/blob/main/docs/wireframes/Mobile%20Home.png" target="_blank">Home Page Wireframe (Mobile)</a>

<a href="https://github.com/ryanoneill416/mod_cartel/blob/main/docs/wireframes/Mobile%20Showcase.png" target="_blank">Showcase Page Wireframe (Mobile)</a>

<h1 id="#features">Features</h1>

<h2 id="home-page">Home Page</h2>

- The landing page is the applications first impression on the user. It is designed to grab their attention, portray its purpose and be easily digestible.

<img src="docs/readme_images/home-page-1.png">
<img src="docs/readme_images/home-page-2.png">

<h2 id="desktop-navigation">Desktop Navigation</h2>

- The applications navigation is found at the top of the page, it has a tinted transparent background and sticks to the top of the user's screen for ease of navigation.
- It holds the links for 'Home', 'Showcase' and 'My Garage'(Only if user logged in).
- The far right contains a 'Sign Up' / 'Login' option if not logged in, and 'Logout' if logged in.

<img src="docs/readme_images/desktop-nav.png">

<h2 id="mobile-navigation">Mobile Navigation</h2>

- The applications mobile navigation sits within a burger menu, illuminating and animating to reveal the same navigation links.
- This is done to encompass design responsiveness principles.

<img src="docs/readme_images/mobile-nav.png">

<h2 id="add-build">Add Build Functionality</h2>

- The applications 'Add Build' functionality allows authenticated members to post their own builds to the database.
- Once the form is completed successfully, this build will be added to 'The Showcase'.
- It will also then appear in members own 'My Garage' page, where it can be edited and deleted.

<img src="docs/readme_images/add-build-page.png">

<h2 id="showcase">Member Showcase</h2>

- The 'Showcase' page is where all of the builds posted by community members are found.
- The 'Showcase' page has three filters with the 'All Builds' filter being selected by default.
- The 'Trending Builds' filter will reveal the top 6 liked member builds at that moment in time.
- The 'Saved Builds' filter is only visible to authenticated members and serves as a means of storing the builds the member has saved.
- Each build has it's own card outlining the build, while also acts as a call-to-action to access the 'Build Detail' page of that build.
- The 'Showcase' page is paginated by 6 to allow for large and clear showcasing of community builds.

<img src="docs/readme_images/showcase-1.png">
<img src="docs/readme_images/showcase-2.png">

<h2 id="build-details">Build Details Page</h2>

- The applications 'Build Detail' page provides an inside look into the user build beyond picture, make and model.
- It is the page where members can like, comment and save builds within the community.
- It details the following about each build 'Overview', 'Specifications' as well as 'Plans/Recommendations'.
- This insures future members can use this page as inspiration for their own and they can understand what was required of the build itself.
- it is on this page that members can post comments giving feedback or to ask questions etc.

<img src="docs/readme_images/build-details-1.png">

<h2 id="build-comments-section">Build Comments Section</h2>

- The comment section allows all Mod Cartel members to engage with a members posted build.
- Comments posted have an option of deletion for the creator of the comment.
- Users with admin roles or staff functionality have the deletion option for all comments.
- This alleviates the time it would take to use the admin panel solely to do so.

<img src="docs/readme_images/comment-section.png">

<h2 id="my-garage">My Garage</h2>

- The 'My Garage' page is exclusive to authenticated users.
- This page features an 'Add Build' call to action and a place where all of the users posted builds are stored.
- Users can use this page to post a new build.
- Users can edit their builds to amend mistakes and/or update the current status of their build.
- Users can also delete their builds if they no longer want it to exist.

<img src="docs/readme_images/my-garage-1.png">
<img src="docs/readme_images/my-garage-2.png">

<h2 id="future-features">Future Features</h2>

- Fully functional events page allowing users to comment on, like and register for IRL community events worldwide.
- Implementation of social login allowing users ease of registration using their existing social accounts.
- Password reset functionality before and after logging in.
- Implementation of a store for merchandise when I have the knowledge of implementing such a feature.
- Scope for a real mobile application to be built, and for this to be a larger project I'm interested in doing to further my studies and knowledge.

<a href="#top">Back to Table of Contents</a>

<h1 id="technology">Technology</h1>

<h2 id="languages">Languages</h2>

- [HTML 5](https://en.wikipedia.org/wiki/HTML/)
- [CSS 3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

<h2 id="frameworks">Frameworks / Libraries / Programs</h2>

- [Git](https://git-scm.com/)<br>
   Used for version control alongside GitHub.
- [GitHub](https://github.com/)<br>
   Used in conjunction with Gitpod as the code editor, to store the project and utilise git version control.
- [Heroku](https://id.heroku.com)<br>
   Used to deploy and host the finished product.
- [Cloudinary](https://cloudinary.com/)<br>
   Used as cloud based storage, storing any submitted media in the deployed application.
- [ElephantSQL](https://www.elephantsql.com/)<br>
   Used to host the PostgreSQL database for the application.
- [W3C - HTML](https://validator.w3.org/)<br>
   Used to validate all HTML code.
- [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   Used to validate all CSS code.
- [CI PEP8 Testing](https://pep8ci.herokuapp.com/)<br>
   Used to validate all Python code.
- [Google Fonts](https://fonts.google.com/)<br>
   Used to provide the fonts used in application styling.
- [Bootstrap](https://getbootstrap.com/)<br>
   Used to aid implementation of styling and responsiveness.
- [Fontawesome](https://fontawesome.com/)<br>
   Used to implement effective icons.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   Used during the development to debug and test responsiveness.
- [Balsamiq](https://balsamiq.com/)<br>
   Used to build both the database schema diagram and design wireframes.

<a href="#top">Back to Table of Contents</a>

<h1 id="testing">Testing</h1>

View the results of automated testing, code validation and others [here](TESTING.md).

<h1 id="deployment">Deployment</h1>

<h2>Heroku's Hosting Service</h2>

1. Log in or create an account at [Heroku](https://id.heroku.com).
2. On the homepage you select the 'New' button and then select 'Create New App' from the drop-down.
3. Give your app a unique name and choose your relevant region.
4. In the 'Settings' tab of your app select 'Reveal Config Vars'.
5. Add a value for 'SECRET_KEY' connecting to your django environment.
6. Add a value for 'DATABASE_URL' connecting to your postgreSQL database.
7. Add a value for 'ClOUDINARY_URL' connecting to cloudinary's cloud hosting service for media.
8. Proceed down to the 'Buildpack' section and select 'Add buildpack' before choosing Python and 'Save Changes'.
9. Back at the top of the page select the 'Deploy' tab.
10. Select GitHub as preferred deployment method, confirm connecting to Github if not automatic.
11. Connect to your relevant repository on GitHub.
12. You can now select either 'Automatic Deployment' for deployment on every push to GiHub or 'Manual Deployment' for only when you press this button.

<h2>Final Deployment</h2>

1. Create a runtime.txt `python-3.8.13`.
2. Ensure a procfile is created with the following `web: gunicorn projectnamehere.wsgi`.
3. Ensure DEBUG = False in settings.py.

<h2>To Clone</h2>
You can clone this project by executing the following:

1. Open this project on GitHub [here](https://github.com/ryanoneill416/mod_cartel).
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click clipboard in order to copy.
3. Once selected, the forked project will be in your repositories.
4. Open up a new terminal.
5. Adjust the current directory to be the location you wish the cloned directory to be.
6. Type 'git clone' and paste the URL copied above in step 2.
7. Hit 'Enter' and the project will be successfully cloned.

<h2>To Fork</h2>

1. Open this project on GitHub [here](https://github.com/ryanoneill416/mod_cartel).
2. The fork button is found at the top of the page.
3. The forked project will be in your repositories.

<a>Back to Table of Contents</a>

<h1 id="credits">Credits</h1>

- All images used in the application are from both <a href="https://unsplash.com/">Unsplash</a> and <a href="https://www.pexels.com/">Pexels</a>.
- I learned how to test a required image field on GitHub <a href="https://gist.github.com/drillbits/5432699">here</a>.
- The following were used as reference and research tools during development:
   - [W3Schools - Python](https://www.w3schools.com/python/)
   - [Stack Overflow](https://stackoverflow.com/)
- Shoutout to my mentor [Adegbenga Adeye](https://www.linkedin.com/in/adegbenga-adeye-psm-i-14003635/) for his guidance on my approach to both design and implementation :)
