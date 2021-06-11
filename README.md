# 💻🔗Python Web Applications: Deploy Script as a Streamlit App
#### Finding sources of European funding repository (https://ec.europa.eu/)

Webapp: <a href="https://app-web-query-eu-funding.herokuapp.com/" target="_blank">https://app-web-query-eu-funding.herokuapp.com/</a>

We are going to develop a simple Python script to extract the database of European calls for funding and perform the search on the titles or tags of the different open calls.
To do this we connect to the database in .json format, convert the fields that interest us into dataframe, select the open calls and perform searches from keywords.  

Once the script is developed, we deploy it on a website with the Streamlit library and test it localhost.  

![Deploy Web App in localhost](/image/Web_App_localhost.gif)  

#### Deploy your Python script web app (Streamlit) on Heroku  

After testing that our European-funded search Python script works on localhost, we're going to try to deploy it to the web using Heroku.

Heroku is a cloud platform where you can build, operate and run web applications with different languages, also offers free plans to test the webapps developed.
Another advantage is that you can publish your GitHub repositories directly to Heroku which helps to keep your code and collaboration processes up to date.

For this we must include in our repository, next to the app.py where our script is executed, 3 more files:
* **Procfile** (acquisitions file): Procfile contains the code that provides the commands to indicate which files the application should run when it is opened.

* **requirements.txt** (requirements file): contains the list of packages and dependencies required to run the web application

* **setup.sh** (installation file): contains a shell script needed to configure the shell environment for our purpose  

Once we have these files in our GitHub repository, we go to our [Heroku](https://www.heroku.com/) user dashboard (previously we will have to register for free) and select "Create new app".  

![Create New App](/image/Heroku_New_app.jpg)  

Give the app a name, using a medium hyphen to separate the words, select your geographic area and you can create the app.  

![Create New App](/image/App_name.jpg)  

Once created, it can be linked to your GitHub repository, giving the corresponding permissions.

![Create New App](/image/link_Github.jpg)  

Once we link with our GitHub user, we search for the repository and connect.

![Create New App](/image/link_Github_2.jpg)  

  It is advisable to select "Enable Automatic Deploys" so that the changes that we implement in the GitHub repository are automatically moved to the webapp that we have just created.  

  ![Create New App](/image/link_Github_3.jpg)   

  Once this is done, the "Build Progress" starts in the "Activity" section and you will have to wait a few minutes for the repository to load and the webapp to be deployed. It may happen that the Build process fails for some aspect that we will have to solve by looking at the logs. For example, it is easy for us to have to indicate the specific version that we have used in the Python libraries.  

  ![Create New App](/image/Activity_logs.jpg)  

  When everything is correct, it will indicate "Build succeeded" and you can open the application to check it.

  <a href="https://app-web-query-eu-funding.herokuapp.com/" target="_blank">**https://app-web-query-eu-funding.herokuapp.com/**</a> 
