import os
from flask import Flask, abort, request, send_from_directory, jsonify, render_template, redirect, make_response, url_for, Response
import sys
from flask_cors import CORS, cross_origin
import os
import json
import time
import datetime
execution_path = os.getcwd()

app = Flask(__name__, template_folder=".")
CORS(app)

@app.route("/", methods= ['GET','POST'])
@cross_origin()
def homepage(): # Redirecting to home page
    return render_template("index.html")

@app.route("/get_json", methods= ['GET','POST']) # Receives loaded file name and requests JSON file 
def get_json():
    data = request.get_data('user_input')
    data = str(data, 'utf-8')

    return json_file

@app.route("/<path:path>")
@cross_origin()
def static_dir(path):
    file_name = request.get_data('json_input')
    #print(f"This is the path: {path} and this is file_name {file_name}")
    return send_from_directory(".", path)


@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=8080)



