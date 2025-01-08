import queue
from collections import deque

def palindrom(row: str):
    row = row.lower().replace(" ", "")

    dq = deque(row)
    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return print ("Рядок не є паліндромом")
    return print ("Рядок є паліндромом")

user_input = input("Введіть рядок: ")

palindrom(user_input)


