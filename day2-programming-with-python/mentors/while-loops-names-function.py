
def make_message(name):
    if name == "Hayley":
        return "You are awesome"
    else:
        return "Hi, " + name

count = 0
while count < 3:
    name = input("What is your name? ")
    print(make_message(name))
    count = count + 1