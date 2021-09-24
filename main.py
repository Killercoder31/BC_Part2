from block import Block
from blockchain import Blockchain
from time import time

bcn=Blockchain()

while(1):
    print("Please select an option from the menu. Press Ctrl+Z to exit")
    print("1: Add a new transaction to the logbook")
    print("2: View blockchain")
    print("3: Exit")

    choice=int(input("Select: "))
    if(choice == 1): 
        data=input("Please enter transaction data: ")
        amount=input("Please enter amount: ")
        bcn.add_new_block(data,amount,time())
    elif(choice == 2):
        for block in bcn.blocks:
            print()
            print(block.to_string())
    else:
        break