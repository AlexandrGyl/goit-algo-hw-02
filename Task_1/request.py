'''
Програма для імітації черги в банку

'''
import queue
import random
import time

k = int(input("Веедіть кількість заявок якібудуть сьогодні оброблено: "))
request_queue = queue.Queue()
unique_request = set()

def generate_request():
    while True:
        request_id = random.randint(1, k)
        if request_id not in unique_request:
            unique_request.add(request_id)
            print(f"Створено заявку із ID: {request_id}")
            request_queue.put(request_id)
            break
        if len(unique_request) == k:
            print("Всі заявки на сьогодні вичерпано")
            return False
    return True

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробляється заявка з ID: {request_id}")

        time.sleep(random.uniform(0.5, 2.0))
        print (f"Завка з ID: {request_id} оброблено")
    else:
        print ("Черга пуста")

def main():
    count_request = 0
    while count_request < k:
        if not generate_request():
            break
        if not process_request():
            count_request += 1
        time.sleep(1)  # Затримка між ітераціями

    print("Всі заявки на сьогодні вичерпано.")

                 

if __name__ == "__main__":
    main()


        

