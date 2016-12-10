from flask import Flask, render_template, request
app = Flask(__name__)
import os
import yelpapi

@app.route("/")
def index():
	location = request.values.get('location')
	search_term = request.values.get('search_term')
	if location and search_term:
		businesses = yelpapi.get_businesses(location, search_term)
	else:
		businesses = None
	return render_template('index.html', businesses=businesses)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)