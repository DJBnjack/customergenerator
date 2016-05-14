import csv
import random

with open('data/last-names.csv', 'rb') as f:
    last_names = list(csv.reader(f))

capitalStrings = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

customers = []
for x in range(0, 10):
    customer = {}
    customer['lastname'] = last_names[random.randint(0,len(last_names))]
    customer['postcode'] = str(random.randint(0,9999)) +  random.choice(capitalStrings) + random.choice(capitalStrings)
    customer['housenumber'] = str(random.randint(0,100))
    customer['telephone'] = "0" + str(random.randint(111111111,999999999))
    customer['mobile'] = "06-" + str(random.randint(11111111,99999999))
    customers.append(customer)

print customers