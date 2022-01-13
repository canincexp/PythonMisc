import json

data = '''
{
    "name": "Can",
    "phone": {
        "type": "intl",
        "number":"+905555555555"
        },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
