import requests

params = {
  "api_key": "fec742c1-c846-4343-a9f1-91c729acd0",

  }
r = requests.get('https://reqres.in/api/users?page=1')
print(r.text)

# This bit of code will write the result of the query to output.csv

with open('output.csv', 'w+') as f:
    f.write(r.text)