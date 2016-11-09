import os
import json
from flask import request, redirect, Flask, url_for, jsonify
from werkzeug.utils import secure_filename
import jsonschema
UPLOAD_FOLDER = os.getcwd()
from flask import send_from_directory

app = Flask(__name__)

@app.route('/schema/<schema_id>', methods =['GET', 'POST'])
def api_root(schema_id):
	if request.method == 'POST':
		f = request.files['file'] 
		SchemaFile = schema_id + ".json"
		f.save(secure_filename(SchemaFile)) #save the file locally for processing
		schemadata = open(SchemaFile).read() #load schemadata

		try:
			json.loads(schemadata) #load the schema file
		except ValueError:
			return jsonify(action="uploadSchema", id = schema_id, status="error", message ="Invalid JSON File") #report ValueError

		try:
			jsonschema.Draft4Validator(json.loads(schemadata)) #check whether JSON schema conforms to Draft4standards
			return jsonify(action="uploadSchema", id = schema_id, status="success")

		except jsonschema.SchemaError as e:
			return jsonify(action="uploadSchema", id = schema_id, status="error", message ="Invalid JSON") #JSON didn't comply/error

	if request.method == 'GET':
		try:
			#files are currently located in our current working directory
			return send_from_directory(directory=os.getcwd(), filename=schema_id+'.json')
		except:
			return jsonify(action="downloadSchema", id=schema_id, status="error", message="Schema not found")



@app.route('/validate/<schema_id>', methods = ['POST'])
def apinew_root(schema_id):
	if request.method == 'POST':
		f = request.files['file']
		JSONFile = request.files['file'].filename + '.json'
		f.save(secure_filename(JSONFile))
		schema_file = schema_id + ".json"
		try:
			schemadata = open(schema_file).read()
			try:
				jsondata = open(JSONFile).read()
			except:
				return jsonify(action="validateDocument", id=schema_id, status="error", message="Invalid JSON")
			jsonschema.validate(json.loads(jsondata), json.loads(schemadata))
		except jsonschema.ValidationError as e:
			return jsonify(action="validateDocument", id=schema_id, status="error", message=e.message)
		except jsonschema.SchemaError as e:
			return jsonify(action="validateDocument", id=schema_id, status="error", message=e)
		else:
			return jsonify(action="validateDocument", id=schema_id, status="success")

if __name__ == '__main__':
    app.run()