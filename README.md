## Introduction

JSON Validation Service (REST) allows you to validate JSON documents against JSON Schemas.


## Installation Instructions

```
$ pip install jsonify
$ pip install flask
$ pip install json-schema
```

## Example Usage

### Start the Validation Service
```
$ python home.py
```
### POST /schema/SCHEMAID 

- Upload JSON Schema with unique `SCHEMAID`

Example 1: Upload a valid JSON Schema

#### curl  -X POST -F file=@schema_sample.json http://127.0.0.1:5000/schema/snow

Output:

```
{
  "action": "uploadSchema", 
  "id": "snow", 
  "status": "success"
}
```

Example 2: Upload invalid JSON Schema
#### curl  -X POST -F file=@schema_sample.json http://127.0.0.1:5000/schema/snow

Output:

```
{
  "action": "uploadSchema", 
  "id": "snow", 
  "message": "Invalid JSON File", 
  "status": "error"
```


### POST /validate/SCHEMAID

- Validate JSON document against JSON Schema `SCHEMAID`

Example 1: Validate a JSON file (success)
#### curl  -X POST -F file=@test.json http://127.0.0.1:5000/validate/snow
```
{
  "action": "validateDocument", 
  "id": "snow", 
  "status": "success"
}
```
Example 2: Validate a JSON file (failure -- incase the file fails validation)
#### curl  -X POST -F file=@test.json http://127.0.0.1:5000/validate/snow
```
{
  "action": "validateDocument", 
  "id": "snow", 
  "message": "u'ABC' is not of type u'number'", 
  "status": "error"
}
```


### GET /schema/SCHEMAID 

- Download JSON Schema with unique `SCHEMAID`

Example:
#### curl  -X GET http://127.0.0.1:5000/schema/snow


```
{
  "type":"object",
  "$schema": "http://json-schema.org/draft-03/schema",
  "required":false,
  "properties":{
    "address": {
      "type":"object",
      "required":true,
      "properties":{
        "city": {
          "type":"string",
          "required":true
        },
        "houseNumber": {
          "type":"number",
          "required":false
        },
        "streetAddress": {
          "type":"string",
          "required":true
        }
      }
    },
    "phoneNumber": {
      "type":"array",
      "required":false,
      "items":
      {
        "type":"object",
        "required":false,
        "properties":{
          "number": {
            "type":"string",
            "required":false
          },
          "type": {
            "type":"string",
            "required":false
          }
        }
      }
    }
  }
}
```
## Notes:

1) All the schema files are currently being uploaded to the current working directory. This can be changed as per the requirements, and we can create a dedicated directory for storing all the schemas.
2) Code needs to be refactored  as per PEP-8 standards, but as of now almost the cases are being handled.
3) Currently files cannot be uploaded using the -d flag, and the -f flag is being used. I'm  trying to debug this issue.

## Todo:
1) Add Unit tests

