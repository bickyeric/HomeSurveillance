from flask import Flask
from flask_ask import Ask, question, statement
import os

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/', methods=['POST'])
def index():
	return "hi there, how ya doin?"

@ask.launch
def start_skill():
	welcome =  "Hai Bicky? have a nice day"
	return statement(welcome)

@ask.intent("YesIntent")
def yes():
	print os.popen(" ssh pi@192.168.100.5 'source ~/.profile && workon cv && python ./opencv/objectdetect/face_recognition/examples/facerec_droidcam.py &' ").read()

	return statement("this is yes intent")

@ask.intent("NoIntent")
def no():
	print os.popen(" ssh pi@192.168.100.5 'pkill python' ").read()
	return statement("this is no intent")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)