## Introduction

JSON Validation Service (REST) allows you to validate JSON documents against JSON Schemas.


## Installation Instructions

```
$ pip install jsonify
$ pip install flask
$ pip install json-schema
```

## Example Usage

### POST /schema/SCHEMAID 

- Upload JSON Schema with unique `SCHEMAID`

Example:

curl  -X POST -F file=@schema_sample.json http://127.0.0.1:5000/schema/snow

Output:

```
{
  "action": "uploadSchema", 
  "id": "snow", 
  "status": "success"
}
```


### POST /validate/SCHEMAID

- Validate JSON document against JSON Schema `SCHEMAID`



#### curl  -X POST -F file=@test.json http://127.0.0.1:5000/validate/snow
```
{
  "action": "validateDocument", 
  "id": "snow", 
  "status": "success"
}
```

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
