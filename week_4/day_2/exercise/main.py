name = input("What is your name? ")
city = input("Where are you from? ")
experience = input("Describe your professional experience and list past employment: ")
education = input("Please list the universities you attended: ")
degrees = input("Please list the degrees you hold: ")
references = input("Please list your references: ")


html= f'''<!DOCTYPE html>
<html>
<head>
	<title>CV</title>
</head>
<body>
<div class="row">
    <div class= "col 4">
<h3>My name is {name}</h3>
<p>I am from {city}</p>
<p>I worked at {experience}</p>
<p>I studied at {education}</p>
<p>I have degrees in {degrees}</p>
<p>My references: {references}</p>
</div>
</div>
</body>
</html>'''

file = open('CVclient.html', 'w')
file.write(html)
file.close()