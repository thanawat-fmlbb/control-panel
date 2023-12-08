import requests
from time import sleep
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

def request(user_id, item_id, quantity):
    data = {
        "user_id": user_id,
        "item_id": item_id,
        "quantity": quantity
    }
    return requests.post(f"http://{url}/order", json=data)

def auto():
    print("Setting up db data.")
    requests.get(f"http://{url}/backdoor/setup")
    
    print("Automating tests...")
    sleep(2)
    print("Testing regular order...")
    request(1,1,1)
    sleep(2)

    print("Testing timeout order... (this will take 30sec)") 
    request(3,1,1)
    sleep(2)

    print("Testing insufficient funds...")
    request(2,1,1)
    sleep(2)

    print("Testing insufficient inventory...")
    request(1,2,1)
    

    print("Basic tests done.")
    print("Please check the .")

if __name__ == '__main__':
    auto()