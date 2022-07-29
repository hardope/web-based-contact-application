from operation import *
from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search_contact():
    if request.method == "POST":
        name = request.form.get("name")

        contact = search_contacts(name)
        if not contact:
            message = "Contact Was Not Found."
            return render_template("error.html", message=message)
        return render_template("list.html", contact=contact)
    else:
        return render_template("search.html")

@app.route("/list", methods=["GET", "POST"])
def list_contact():
    contact = list_names()
    return render_template("list.html", contact=contact)

@app.route("/new", methods=["GET", "POST"])
def create_contact():
    if request.method == "GET":
        return render_template("new.html")
    else:
        pass
    name = request.form.get("name")
    email = request.form.get("email")
    number = request.form.get("number")

    if not name or not email or not number:
        message = 'You have to input a name, number and email'
        return render_template("error.html", message=message)
    
    check = new_contact(name, number, email)

    if check == 'exists':
        message = 'Contact exists'
        return render_template("error.html", message=message)
    elif check == 'saved':
        return redirect("/")
    else:
        message = 'An unknown error occured'
        return render_template("error.html", message=message)

@app.route("/delete", methods=["GET", "POST"])
def del_contact():
    if request.method == "GET":
        return render_template("delete.html")
    else:
        pass
    name = request.form.get("name")

    if not name:
        message = "You have to input a name."
        return render_template("error.html", message=message)

    check = delete_contact(name)

    if check == "deleted":
        return redirect("/")
    else:
        message = "Contact Does Not Exist."
        return render_template("error.html", message=message)
