	from flask import Flask, redirect , url_for
	app=Flask(__name__)

	@app.route('/admin')
	def hello_admin()
	return "hello_admin"
	
	@app.route('/guest/<guest>')
	def hello_guest(guest)
	return "hello %s" %guest
	
	@app.route('/name/<name>')
	if name == "admin"
	return redirect(url_for('hello_admin'))
	elif 
	return redirect(url_for('hello_guest',guest=name))
	
	return app
