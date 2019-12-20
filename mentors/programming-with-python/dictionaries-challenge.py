pets = {
    "Remus": ["dog", 5, True],
    "Izzy": ["cat", 12, True],
    "Archie": ["dog", 12, True],
    "Tuna": ["cat", 15, True],
    "Socks": ["cat", 3, False],
    "Biscuit": ["dog", 1, False],
    "Rory": ["dog", 7, True],
    "Polly": ["budgie", 23, False]
}

for name, info in pets.items():
    if info[2]:
        microchipped = 'is microchipped.'
    else:
        microchipped = 'is not microchipped.'
    print(name + ' is a ' + info[0] + ', is '+ str(info[1]) + ' years old and ' + microchipped)