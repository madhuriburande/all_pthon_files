## simple example
## create dict
import json
d1={"a":1,"b":2,"c":3,"d":4}
print(type(d1))
print("dictionry=",d1)

# convert dict to json i.e conver object into json nyusing dumps
json1=json.dumps(d1)
print(type(json1))
print("In Json=",json1)

## 2.example
import json
def send_json(dict_res):
    print("convert python dictionary into json")

    json1=json.dumps(dict_res)
    print("Json1=",json1)

## create dict 
d1={
    "Name":"madhuri",
    "Salary": 100000,
    "Skills":["Python","Web developer","Testing"],
    "email":"madhuri@31gamil.com"
}
send_json(d1)
print()

## 3.another example
sampleDict = {
    "colorList": ["Red", "Green", "Blue"],
    "carTuple": ("BMW", "Audi", "range rover"),
    "sampleString": "pynative.com",
    "sampleInteger": 457,
    "sampleFloat": 225.48,
    "booleantrue": True,
    "booleanfalse": False,
    "nonevalue": None
}
print("Converting Python primitive types into JSON")
resultJSON = json.dumps(sampleDict)
print(resultJSON)

## converting Json into dictionary
import json
d1={"a":1,"b":2,"c":3,"d":4}
print(type(d1))
print("dictionry=",d1)
json1=json.dumps(d1)
print("json1=",json1)
print()

# covert json into dict
d2=json.loads(json1)
print("Convert json into dictionary:d2=",d2)
print()

## 2.example

Json_fmt= """{
    "name": "Madhuri Burande",
    "salary": 100000,
    "skills": [
        "Python full stack developer",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
"""
dict_cov=json.loads(Json_fmt)
print("Json to Dict:=",dict_cov)
