import requests

# iegust linku uz api (man nav api key bet lai demonstretu ka izmantotu noslepumus)
with open('/home/config.txt', 'r') as file:
    api_endpoint = file.read().strip()

#ar get mes pieprasam json atbildi
headers = {
    "Accept": "application/json"
}

#veic pieprasijumu
response = requests.get(api_endpoint, headers=headers)


if response.status_code == 200: #ja status ir 200 veiksmigi izdevas
    joke_data = response.json() #iegust joku json formata
    print("Joke:", joke_data["joke"]) #izprinte joku
else:
    print("Failed to retrieve a dad joke.")
