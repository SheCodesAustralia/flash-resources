from microbit import *

boat1 = Image("05050:" "05050:" "05050:" "99999:" "09990")
boat2 = Image("00000:" "05050:" "05050:" "05050:" "99999")
boat3 = Image("00000:" "00000:" "05050:" "05050:" "05050")
boat4 = Image("00000:" "00000:" "00000:" "05050:" "05050")
boat5 = Image("00000:" "00000:" "00000:" "00000:" "05050")
boat6 = Image("00000:" "00000:" "00000:" "00000:" "00000")
all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]

FISH = Image("00900:""09909:""99999:""09909:""00900")

DASH = Image("00000:""00000:""99999:""00000:""00000")


while True:
    if button_a.is_pressed():
        for x in range(4):
            display.show(FISH)
            sleep(200)
            display.clear()
            sleep(200)
    if button_b.is_pressed():
        for x in range(4):
            display.show(all_boats, delay=200)
            sleep(200)
            display.clear()
            sleep(200)
    else:
        display.show(DASH)
        sleep(200)
        display.clear()
        sleep(1000)




    #if button_a.is_pressed():
     #   display.show(Image.HEART)
    #elif button_b.is_pressed():
     #   display.show(all_boats, delay = 200)
    #else:
     #   display.scroll("press button")

display.clear()
