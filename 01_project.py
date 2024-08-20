import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = -1
youstr = input("enter your choice: ")
youDict = {"s": 1, "w": -1 , "g": 0}
reverseDict = {1:"snake", -1: "water" , 0: "gun"}

you = youDict[youstr]

# by now we have 2 numbers (variable), you and computer
print(f"you choose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == -1 and you == -1):
    print("draw")
    
    
else:
    
   if(computer == -1 and you == 1):
    print("you win")
   elif(computer == -1 and you == 0):
    print("you lose")

   if(computer == 1 and you == -1):
    print("you lose")
   elif(computer == 1 and you == 0):
    print("you win")

   if(computer == 0 and you == -1):   
    print("you win")
   elif(computer == 0 and you==1):
    print("yoou lose")
    
   else:
       print("something went wrong")