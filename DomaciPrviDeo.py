import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")

Predmeti = ["WSIT", "DIRWS", "USI"]

class Kontakti:
    adresa = "Veljka Dugosevica 16",
    mesto = "Beograd",
    telefon = "065555421"

Kontakt = Kontakti()


payload = json.dumps({
  "id": "S71320",
  "ime": "Danilo",
  "prezime":"Lukovic",
  "smer":"Informacione tehnologije",
  "predmeti": Predmeti,
  "prosek":"6.69",
  "kontakt": [json.dumps(Kontakt.adresa), json.dumps(Kontakt.mesto), json.dumps(Kontakt.telefon)] 

})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/apiv1/pantry/ef854ed6-cd5e-423e-99d1-03a61e0ea665/basket/New_Basket", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))