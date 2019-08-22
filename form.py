#!/usr/local/bin/python3

import cgi, cgitb

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
weight = form.getvalue('height')
height = form.getvalue('weight')
email = form.getvalue('email')

if form.getvalue('facebook'):
    facebook_flag = 'ON'
else:
    facebook_flag = 'OFF'
if form.getvalue('twitter'):
    twitter_flag = 'ON'
else: 
    twitter_flag = 'OFF'
if form.getvalue('email'):
    email_flag = 'ON'
else: 
    emai_flag = 'OFF'
if form.getvalue('text'):
    text_flag = 'ON'
else:
    text_flag = 'OFF'
if form.getvalue('lifestyle'):
    lifestyle = form.getvalue('lifestyle')
else: 
    lifestyle = 'Not Set'
if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else: 
    text_content = "Not Entered"
    
print("Content-type: text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("</head>")
print ("<body>")

print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
print ("<h2> Your height is : %s</h2>" % (height))
print ("<h2> Your weight is : %s</h2>" % (weight))
print ("<h2> Your email is : %s</h2>" % (email))
print ("<h2> CheckBox Facebook is : %s</h2>" % facebook_flag)
print ("<h2> CheckBox Twitter is : %s</h2>" % twitter_flag)
print ("<h2> CheckBox Email is : %s</h2>" % email_flag)
print ("<h2> CheckBox TextMessage is : %s</h2>" % text_flag)
print ("<h2> Selected Lifestyle is %s</h2>" % lifestyle)
print ("<h2> Entered Goal is %s</h2>" % text_content)

print ("</body>")
print ("</html>")





