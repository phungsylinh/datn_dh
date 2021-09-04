#from chatbot import chatbot
from chat import get_response
import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route("/")
def home():
    now = datetime.datetime.now()
    if (now.minute < 10):
        time = str(now.hour)+":0"+str(now.minute)
    else:
        time = str(now.hour)+":"+str(now.minute)
    return render_template("index.html",time = time)
    #return render_template("index.html",headline = "Hello world!")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    #userText = request.args.get('msg').encode('utf8')
    return get_response(userText)


if __name__ == "__main__":
    #app.run()
    app.run(debug=False, threaded=False)