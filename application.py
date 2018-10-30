from flask import Flask, render_template, request

application = Flask(__name__)
application.debug = True

@application.route('/', methods=['GET'])
def homepage():
 return render_template("homepage.html")

@application.route('/generated_test', methods=['GET','POST'])
def generated_test():
 if request.method == 'POST':
 	subject = request.form['subject']
 	THE_test = make_test(subject)
 	return render_template('subject_test.html', subject=subject, test=THE_test)
 else:
 	return render_template('homepage.html')

def make_test(subject):
	subject = subject.lower()
	if subject == "cells":
		return "Question 1: Which organelle is the power house of the cell?"
	else:
		return "Our databases do not have enough information to make a test on " + subject + ". Please try a different subject."

if __name__ == "__main__":
 application.run()
