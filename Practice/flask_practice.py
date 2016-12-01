from flask import Flask  # both need to be the same

app = Flask ("MyApp")

@app.route("/")   # This is always the same
def abcd():
	return "Hello Deb!" # the text can be anything you like

@app.route("/<name>")   # This is always the same
def Hello(name):
	return "Hello {0}!".format(name) # the text can be anything you like


app.run()  # .run is always the same