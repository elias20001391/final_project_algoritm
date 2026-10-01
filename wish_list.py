



wish_list = []


while True:
    menu = input("1.add item 2.remove item 3.exit:")
    if menu == "3":
        print("goodbye")
        break
    while True:
        match menu:
            case "1":
                add_wish = input("enter your wish to add(enter 8888 to exit):")
                if add_wish == "8888":
                    print(wish_list)
                    break
                else:
                    wish_list.append(add_wish)
            case "2":
                remove_wish = input("enter your wish to remove(enter 8888 to exit):")
                if remove_wish == "8888":
                    print(wish_list)
                    break
                else:
                    wish_list.remove(remove_wish)
            case _:
                print("invailed")
                break