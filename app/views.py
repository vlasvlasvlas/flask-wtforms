"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    abort,
    send_from_directory,
)
from werkzeug.utils import secure_filename

# Note: that when using Flask-WTF we need to import the Form Class that we created
# in forms.py
# import forms:
from .forms import Formulario1


###
# Routing for your application.
###

# home
@app.route("/")
def home():
    """Render website's home page."""
    return render_template("home.html")


@app.route("/wtform", methods=["GET", "POST"])
def wtform():
    """Render WTForm example, main form"""

    # instancia Formulario 1
    myform = Formulario1()  # form instance

    # if POST:
    if request.method == "POST":
        print("--------> POST IN ")
        print("---> UPLOAD FOLDER " + app.config["UPLOAD_FOLDER"])

        if myform.validate_on_submit():
            # Note the difference when retrieving form data using Flask-WTF
            # Here we use myform.firstname.data instead of request.form['firstname']
            firstname = myform.firstname.data
            lastname = myform.lastname.data
            email = myform.email.data

            print("-------> TEST FIRSTNAME:", firstname)

            # attachment
            document = (
                myform.document.data
            )  # we could also use request.files['document']

            # get filename from document
            filename = secure_filename(document.filename)

            # save document in upload folder
            document.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            # setup success message
            flash("You have successfully filled out the form", "success")

            return render_template(
                "result.html",
                firstname=firstname,
                lastname=lastname,
                email=email,
                filename=filename,
            )

        flash_errors(myform)

    # if GET
    if request.method == "GET":
        return render_template("wtform.html", form=myform)


# Example route using send_from_directory
# for files that are not in the "static" folder
@app.route("/uploads/<filename>")
def get_uploaded_file(filename):
    """upload filenema"""
    root_dir = os.getcwd()

    return send_from_directory(
        os.path.join(root_dir, app.config["UPLOAD_FOLDER"]), filename
    )


###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if any validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                "Error in the %s field - %s" % (getattr(form, field).label.text, error),
                "danger",
            )


# optional: show txt file
# show attachment, must be valid with default app upload extensions
@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)


# add to headers
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


# handle error 404
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template("404.html"), 404
