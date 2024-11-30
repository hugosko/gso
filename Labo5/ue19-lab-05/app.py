import requests

r = requests.get("https://official-joke-api.appspot.com/random_joke")

if r.status_code == 200:
    t = r.text.split(":")
    setup = t[2]
    punchline = t[3]
    print(setup[1:-13])
    input("*Press enter to display the punchline* ")
    print(punchline[1:-6])


else:
    print(f"Erreur : statut HTTP {r.status_code}")
