from flask import Flask,render_template,request
import requests


app = Flask(__name__,static_url_path = "/static", static_folder = "static")

@app.route('/test1')
def web1():
	return render_template("index1.html")

 
@app.route('/test2')#methods = ["POST"])
def web2():
	#latitude = request.form['Latitude']
	#longitude = request.form['Longitude']
	
	return render_template("index2.html")

@app.route('/test3',methods = ["POST"])
def web3():
	latitude = request.form['Latitude']
	longitude = request.form['Longitude']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat='+latitude+'&lon='+longitude+'&appid=f99ff9bee2ebf69b87d81068bb64b639')
	print(request.is_json)
	obj = r.text
	return obj
	
if __name__ == '__main__':
	app.run(debug = True)