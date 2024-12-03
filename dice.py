import random

while True:
   random_number=random.randint(1,6)
   a=input("to roll the dice press enter: ")
   if a!="q":
    print("number is",random_number)
    continue
   else:
      break
