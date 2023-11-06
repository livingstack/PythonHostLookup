#!/host_lookup/bin/python3

from flask import Flask
import platform

hostname = platform.node()
hoststring = "The hostname of the server you're running on is : " + hostname

app = Flask(__name__)
@app.route("/")
def index():
	return(hoststring)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)



