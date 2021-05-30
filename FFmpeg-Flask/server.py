from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

@app.route('/stream/<path:path>')
def send_stream(path):
	response = send_from_directory('stream', path)
	response.cache_control.max_age = 0
	return response

@app.route('/')
def index():
	return render_template('index.html', methods=[])
	

if __name__ == "__main__":
	app.run()
