import requests  # Importē pieprasījumu (requests) bibliotēku, lai izmantotu HTTP pieprasījumus

api_endpoint = "https://icanhazdadjoke.com/"  # Definē API galapunktā, kur mēs saņemsim jokus
headers = {
    "Accept": "application/json"  # norādot, ka pieprasījums pieņems JSON atbildes formātā
}

# Veic GET pieprasījumu uz API galapunktu ar definētajiem headers
response = requests.get(api_endpoint, headers=headers)

# Pārbauda, vai saņemtais atbildes statusa kods ir 200 
if response.status_code == 200:
    joke_data = response.json()  # Izgūst datus no atbildes JSON formātā
    print("Joke:", joke_data["joke"])  # Izdrukā iedoto joku
else:
    print("Failed to retrieve a dad joke.")  # Ja neizdevās iegūt joku, izdrukā kļūdas ziņojumu
