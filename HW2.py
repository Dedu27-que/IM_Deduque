cart = {
    0: "underwear",
    1: "tank top",
    2: "jacket"
}

print("You have", len(cart), "items in the cart")

while True:
    choice = input("\nWhat would you like to do [C]hange [R]emove [D]isplay [S]earch ? ").upper()

    if choice == "D":
        print("\nDisplaying Values")
        print("Key\tValue")
        for k, v in cart.items():
            print(k, "\t", v)

    elif choice == "S":
        item = input("Enter item to search: ")
        found = False
        for k, v in cart.items():
            if v.lower() == item.lower():
                print("Found", v, "item")
                found = True
                break
        if not found:
            try:
                key = int(item)
                if key in cart:
                    print("Found", cart[key], "item")
                else:
                    print("I'm sorry, not in the cart")
            except:
                print("I'm sorry, not in the cart")

    elif choice == "R":
        key = input("Enter key to remove: ")
        if key.isdigit():
            key = int(key)
            if key in cart:
                print("The key", key, "with value", cart[key], "has been deleted")
                del cart[key]
            else:
                print("Key not found")
        else:
            print("Key not found")

    elif choice == "C":
        key = input("Enter key to change: ")
        if key.isdigit():
            key = int(key)
            if key in cart:
                print("Found", cart[key], "item")
                new_value = input("Enter new value: ")
                cart[key] = new_value
            else:
                print("I'm sorry, not in the cart")
        else:
            print("Invalid key")

    elif choice == "*":
        print("Bye")
        break

    else:
        print("Invalid choice, try again.")
