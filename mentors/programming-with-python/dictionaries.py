pets = {
    "Remus": "Border Collie",
    "Izzy": "Miniature Schnauzer",
    "Archie": "Miniature Schnauzer",
    "Tuna": "British Longhair",
    "Socks": "Dwelf",
    "Biscuit": "Beagle",
    "Rory": "Corgi"
}

for name, breed in pets.items():
    print(name, "is a", breed)


pets["Boston"] = "Pomeranian"

print(pets["Boston"])

pets["Boston"] = "Golden Retriever"

print(pets["Boston"])