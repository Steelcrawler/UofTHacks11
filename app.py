from flask import Flask, request, render_template, redirect, url_for
from cohereaifile import get_response
from ElevenLabsSpeaking import speak
import time
# Flask constructor
app = Flask(__name__, template_folder="templates") 
app.config['TEMPLATES_AUTO_RELOAD'] = True 
# A decorator used to tell the application
# which URL is associated function

outputSpongebob = []
outputSandy = []
outputPatrick = []
outputThomas = []
outputGordon = []
outputEdward = []
output = []

@app.route("/")

def index():
    return render_template("index.html", output=output)

@app.route('/spongebob', methods=["GET", "POST"])
def spongebob():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "SpongeBob")
        outputSpongebob.append({"input": input, "screenOutput": screenOutput})
        return render_template('spongebob.html', output=outputSpongebob)
    return render_template('spongebob.html')

@app.route('/sandy', methods=["GET", "POST"])
def sandy():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "Sandy")
        audioFile = speak(screenOutput, "Sandy")
        outputSandy.append({"input": input, "screenOutput": screenOutput})
        return render_template('sandy.html', output=outputSandy, audioFile=audioFile, currentTime=time.time())
    return render_template('sandy.html')

@app.route('/patricks', methods=["GET", "POST"])
def patricks():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "Patrick")
        audioFile = speak(screenOutput, "Patrick") 
        outputPatrick.append({"input": input, "screenOutput": screenOutput})
        return render_template('patricks.html', output=outputPatrick, audioFile=audioFile)
    return render_template('patricks.html')

@app.route('/thomas', methods=["GET", "POST"])
def thomas():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "Thomas")
        outputThomas.append({"input": input, "screenOutput": screenOutput})
        return render_template('thomas.html', output=outputThomas)
    return render_template('thomas.html')

@app.route('/gordon', methods=["GET", "POST"])
def gordon():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "Gordon")
        outputGordon.append({"input": input, "screenOutput": screenOutput})
        return render_template('gordon.html', output=outputGordon)
    return render_template('gordon.html')

@app.route('/edward', methods=["GET", "POST"])
def edward():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "Edward")
        outputEdward.append({"input": input, "screenOutput": screenOutput})
        return render_template('edward.html', output=outputEdward)
    return render_template('edward.html')

@app.route('/get_audio', methods=["GET", "POST"])
def get_audio():
    text = request.args.get("text")
    character = request.args.get("character")
    return speak(text=text, character=character)


if __name__ == '__main__':
    app.run(debug=True)