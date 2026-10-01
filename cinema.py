



films = ["film_1","film_2","film_3","film_4","film_5"]


while True:
    menu = input("1.buy a ticket 2.exit:")
    match menu:
        case "1":
            film_person_chose = input("""
film 1 : 200t
film 2 : 300t  (20% takhfif)
film 3 : 150t
film 4 : 250t  (10% takhfif)
film 5 : 100t 

enter your choice(just enter a number):""")
            while True:
                match film_person_chose:
                    case "1":
                        number = int(input("how many:"))
                        price = 200 * number
                        print("you shoud pay:",round(price),"t")
                        break
                    case "2":
                        number = int(input("how many:"))
                        price = (300 * number) * 0.8
                        print("you shoud pay:",round(price),"t")
                        break
                    case "3":
                        number = int(input("how many:"))
                        price = 150 * number
                        print("you shoud pay:",round(price),"t")
                        break
                    case "4":
                        number = int(input("how many:"))
                        price = (250 * number) * 0.9
                        print("you shoud pay:",round(price),"t")
                        break
                    case "5":
                        number = int(input("how many:"))
                        price = 100 * number
                        print("you shoud pay:",round(price),"t")
                        break
                    case _:
                        print("invailed")
                        break
        case "2":
            print("goodbye")
            break
        case _:
            print("invailed")