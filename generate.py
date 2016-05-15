import csv
import random
import json

with open('data/last-names.csv', 'rb') as f:
    last_names = list(csv.reader(f))

capitalStrings = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
genderStrings = "MF"
emailProviders = ['gmail.com', 'hotmail.com', 'live.com', 'live.nl', 'tele2.nl', 'kpn.nl', 'vodafone.nl']
cities = ['Rotterdam', 'Utrecht', 'Delft', 'Amsterdam', 'Breda', 'Groningen', 'Schiedam', 'Rijswijk']

customers = []
for x in range(0, 10):
    customer = {}
    customer['initial'] = random.choice(capitalStrings)
    customer['gender'] = random.choice(genderStrings)
    customer['lastname'] = last_names[random.randint(0,len(last_names))][0]
    customer['postcode'] = str(random.randint(0,9999)) + random.choice(capitalStrings) + random.choice(capitalStrings)
    customer['street'] = "RandomStreet"
    customer['city'] = random.choice(cities)
    customer['housenumber'] = str(random.randint(0,100))
    customer['telephone'] = "0" + str(random.randint(0,99)) + "-" + str(random.randint(1111111,9999999)) 
    customer['mobile'] = "06-" + str(random.randint(11111111,99999999))
    customer['email'] = customer['initial'].lower() + "." + customer['lastname'].lower() + "@" + random.choice(emailProviders)
    customers.append(customer)

print customers

with open('c:/temp/out.txt', 'w') as outfile:
    json.dump(customers, outfile)