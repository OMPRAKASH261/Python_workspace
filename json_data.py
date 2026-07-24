import json

json_str =  '{"name": "OmPrakash", "isStudent": true}'
print(type(json_str))


py_obj = json.loads(json_str)
print(type(py_obj), py_obj)


py_obj = {
    "name": "Omprakash",
    "isStudent": None
}
json_str = json.dumps(py_obj)
print(type(json_str), json_str)


with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)
    print(type(py_obj))
    
data = {
    "name": "Om",
    "age": 22,
    "isTeacher": True
}
with open("data1.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)