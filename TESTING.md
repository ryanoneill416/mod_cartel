<h1 id="top">Mod Cartel Testing Documentation</h1>

Back to the [README](README.md)

<h1 id="contents">Contents</h1>

- [Automated Unit Testing Results](#automated-testing-results)
- [HTML Validation](#html-validation)
- [CSS Validation](#css-validation)
- [Python Validation - PEP8](#python-validation)
- [Lighthouse](#lighthouse)
- [Console Results](#console-results)
- [Bugs / Issues](#bugs)

<h2 id="automated-testing-results">Automated Unit Testing Results</h2>

<h3>Automated testing coverage is at 92%</h3>

<img src="docs/testing_images/modcartel-testing-coverage.png">

- This can be improved upon for sure and is something which I aim to come back to in future and tackle, however I am aware coverage over 90% is considered industry standard.
- You can locate all of the test files written <a href="https://github.com/ryanoneill416/mod_cartel/tree/main/webapp/tests">here</a>.

<h2 id="html-validation">HTML Validation</h2>

All html code passes validation with no errors, you can see each result below:

<h3>Index.html</h3>

<img src="docs/testing_images/index-and-base-html.png">

<h3>Showcase.html</h3>

<img src="docs/testing_images/showcase-html.png">

<h3>Build_detail.html</h3>

<img src="docs/testing_images/build-detail-html.png">

<h3>My-garage.html</h3>

<img src="docs/testing_images/my-garage-html.png">

<h2 id="css-validation">CSS Validation</h2>

All CSS code passes validation with no errors, you can see each result below:

<img src="docs/testing_images/css-validation.png">

<h2 id="python-validation">Python Validation - PEP8</h2>

All python code passes pep8 validation with no errors, you can see each result below:

<h3>Admin.py</h3>

<img src="docs/testing_images/admin-pep8.png">

<h3>Apps.py</h3>

<img src="docs/testing_images/apps-pep8.png">

<h3>Forms.py</h3>

<img src="docs/testing_images/forms-pep8.png">

<h3>Models.py</h3>

<img src="docs/testing_images/models-pep8.png">

<h3>Urls.py</h3>

<img src="docs/testing_images/urls-pep8.png">

<h3>Views.py</h3>

<img src="docs/testing_images/views-pep8.png">

<h2 id="lighthouse">Lighthouse</h2>

- Lighthouse score can be improved upon and is at my highest priority when it comes to future updates/ implementations.
- The nature of the lower scores is a result of image resizing for the carousel and header images as the same image is adjusted for all screen size.
- The score is also negatively effected by file types uploaded by members.
- To remedy this in future, I already have plans to make a sole mobile version of this application to learn mobile development thoroughly, however I will adjust the image model to convert images automatically to webp.
- Due to time constraints and the need to do extra learning exploring these methodologies, the score is left with room to improve.

<img src="docs/testing_images/lighthouse-1.png">
<img src="docs/testing_images/lighthouse-2.png">