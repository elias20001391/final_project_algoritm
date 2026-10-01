

import random


mavane = ["autoban","sorat_gir","cheragh_red","gharrah"]


while True:
    mavane_shanci = random.choice(mavane)
    print(mavane_shanci)
    driver_tec = input("""
enter '1' for eist ya kahesh sorat
enter '2' for harekat
enter '3' for harekat be rast
enter '4' for harekat be chap

enter your chose:""")
    match driver_tec:
        case "1":
            if mavane_shanci == "sorat_gir" or mavane_shanci == "cheragh_red":
                print("safe")
            else:
                print("you lose")
                break
        case "2":
            if mavane_shanci == "autoban" or mavane_shanci == "gharrah":
                print("safe")
            else:
                print("you lose")
                break
        case "3":
            if mavane_shanci == "gharrah" :
                print("safe")
            else:
                print("you lose")
                break
        case "4":
            if mavane_shanci == "gharrah" :
                print("safe")
            else:
                print("you lose")
                break

        case _:
            print("invailed")
                
    
    
    