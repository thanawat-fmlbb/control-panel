import requests
url = "127.0.0.1:8000"

available_items = {
    # regular item (should have infinite stock)
    1: "Thing", 

    # has 0 stock --> for testing insufficient stock
    2: "Empty Thing", 

    3: "Another thing",
}

test_users = {
    "1": "urmom", # infinite money
    "2": "mr.broke", # no money
    "3": "johndoe", # timeout at delivery
}


if __name__ == '__main__':
    print("Setting up...", end='  ')
    response = requests.get(f"http://{url}/backdoor/setup")
    print("Done!")

    print('Control Panel running...')
    while True:
        try:
            command = input(">>> ")
            if command == 'exit' or command == 'e' or command == 'quit' or command == 'q':
                print("Control Panel exited.")
                break
            elif command == "reset":
                response = requests.get(f"http://{url}/backdoor/setup")
                print("Reverted db info to default.")
            elif command == "request" or command == "r":
                print("Crafting request...")
                print("Available Test Users: ")
                for user in test_users:
                    print(f"{user} - {test_users[user]}")
                username = input("UserID (or new Username): ")

                user_id = None
                address = None
                
                if username not in test_users.keys():
                    user_id = None
                    address = input("Address: ")
                else:
                    user_id = username
                    username = test_users[username]

                print("Available Items: ")
                for item in available_items:
                    print(f"{item} - {available_items[item]}")
                item_id = input("Item (id): ")
                quantity = input("Quantity: ")

                data = {
                    "username": username,
                    "user_id": user_id,
                    "address": address,
                    "item_id": item_id,
                    "quantity": quantity
                }
                response = requests.post(f"http://{url}/order", json=data)
                print("Request sent. Response:")
                print(response.text)
        except Exception as e:
            print("Error: ", e)
        except KeyboardInterrupt:
            print("\nControl Panel exited.")
            break
