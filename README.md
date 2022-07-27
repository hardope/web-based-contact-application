# web-based-contact-application

### Steps on installation
* Download file
* Unzip file
* Save file to directory
* Open command-line
* make sure python is installed
* install flask to pip

#### Description:
This is a web based contact application that enables you to store, search, delete, list and create contacts.

## app.py:

This is my web application, It handles all the back end operations and renders the necessary html pages, also it is responsible for accessing and
entering data into the database. Also it checks for the methods employed by the page requests and reacts to them, respectively and redirects to new pages
necessary.

#### @app.route("/")

This is the home page with buttons to the other pages for delete, new contact search and list.

#### @app.route("/search")

This route renders search.html if requested with GET but takes input from the search page if requested with POST. When requested with post, the route takes the name of the contact the user must have inputed and passas it on into a function that will query the database and return the countacts that matches the users input.

#### @app.route("/list")

This route queries the database for all available contacts and displays it in the html page.

#### @app.route("/new")

This route displays the new contact page if requested via GET, But on the other hand if requested via POST it collects all data(name, number and email) inputed by user and tries to input it into the database by running SQL queries but redirects to error page if any error is encountered.

#### @app.route("/")

This route collects contact name that is inputed by the user and tries to delete it. If any error is encountered during this process, the error page is prompted to display the error details. 

## operation.py

This file contains all functions used by app.py to perform queries on the database.

#### def search_contacts(name):

This function takes an argument which is a name of a contact to be searched, the function returns a list of rows or just one row if only one matching contact is found.

#### def list_names():

This function queries the database for all contacts and returns a list of rows.

#### def new_contact(name, number, email):

This function takes three arguements(name, number, email) provided by user, then it inputs the data int the satabase using SQL queries while checking for errors and wrong input.

#### def delete_contact(name):

This function only takes name as arguement, checks the database to see if contact exists and then deletes it if it does.

 
