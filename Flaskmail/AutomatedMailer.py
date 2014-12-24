__author__ = 'Rithesh'

# Flask-Mail example
# ===================
# This is a small sample application that provides a basic demonstration of
# Flask-Mail, and is primarily meant to be used as a module/function for larger programs.
# This app is written assuming the Email Application under use is Gmail but it can be modified
# for any other Email Application as required.(Note- The Email settings would also need to change accordingly).

# Import libraries
from flask import Flask
from flask.ext.mail import Mail, Message

# Initialize the app.
app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
	MAIL_USERNAME = '<Gmail id without the @gmail.com extension>',
	MAIL_PASSWORD = '<Password of Gmail id>',
    MAIL_DEBUG = True
	)
mail=Mail(app)

# On accessing 127.0.0.1:<port>/ a mail will be sent to the recipients mail id.
@app.route("/")
def index():
    msg = Message("Hi! Welcome to Flask Mail!", sender='<Sender Gmail id>', recipients=['<Receiver Gmail id>'])
    msg.body = "This is the email body"
    mail.send(msg)
    print "Mail sent"
    return "Sent"

if __name__ == "__main__":
    app.run()
