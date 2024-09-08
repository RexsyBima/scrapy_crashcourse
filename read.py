import json

with open("output.json", "r") as f:
    data = json.load(f)

# print(type(data), data[0], type(data[0]))

dictionary = {"name": "John", "age": 30, "city": "New York"}


def greet(**kwargs):
    for k in kwargs.items():
        print(k)


greet(**dictionary)
