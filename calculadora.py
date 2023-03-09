import time
import os

result = 0
num2 = 0
a = 0

while num2 != "esc":
    if a == 0:
        num = input("Numero 1: ")
    
    if a > 0:
        num = result

    operation = input("Ingrese operacion: ")
    num2 = input("Numero 2: ")

    if num2 == "esc":
        os.system("cls")
        print(result)
        break

    print("--------------\n")
    result = eval(f"{num} {operation} {num2}")
    print(result)
    time.sleep(1)
    os.system('cls')
    print(result)
    a+=1

        

