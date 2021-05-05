from flask import Flask
from flask import request

app = Flask(__name__,
						static_url_path='',
						static_folder='templates',
						template_folder='templates'
						)

from flask import render_template
from datetime import datetime


@app.context_processor
def inject_now():
	return {'now': datetime.utcnow()}

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/analyze_by_tweet', methods=['POST'])
def tweetAnalyze():
	print(request.method)
	print(request.form, request.args, request.values)
	res = request.form.get('content')
	return 'Your pasted tweet is : {}'.format(res)

@app.route('/analyze_by_csv', methods=['POST'])
def csvAnalyze():
	res = request.form.get('content')
	return 'Your uploaded csv is : {}'.format(res)

@app.route('/analyze_by_date', methods=['POST'])
def dateAnalyze():
	startDate = request.form.get('startDate')
	endDate = request.form.get('endDate')
	print(request.form, request.args, request.values)
	return 'Start, end dates : {} ==> {}'.format(startDate, endDate)

@app.route('/about')
def about():
	return 'About page, will finish later'


@app.route('/help')
def help():
	return 'Help page, will finish later'

if __name__ == "__main__":
	app.run(debug=True)
