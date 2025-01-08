'''
Програма для імітації черги в банку

'''
import queue
import random
import time

request_queue = queue.Queue()

def generate_requeste():
    request_id = random.randint(1, 100)
    print(f"Створено заявку із ID: {request_id}")
    request_queue.put(request_id)

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Ообробляється заявка з ID: {request_id}")

        time.sleep(random.uniform(0.5, 2.0))
        print (f"Завка з ID: {request_id} оброблено")
    else:
        print ("Черга пуста")

def main():
    while True:
        generate_requeste()
        process_request()
        time.sleep(1)

if __name__ == "__main__":
    main()


        

