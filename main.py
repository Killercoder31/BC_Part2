from block import Block
from blockchain import Blockchain
from time import time
from transaction import Transaction
from nodes import Node

bcn=Blockchain()
unverified=[Transaction]
verified=[Transaction]
host='127.0.0.1'
port=12345

n1=Node('Pluto')
n2=Node('Jupiter')
n3=Node('Titan')
n1.connect_to_node('127.0.0.1',12344)
n2.connect_to_node('127.0.0.1',12345)
n3.connect_to_node('127.0.0.1',12346)

while(1):
    print("Please select an option from the menu: ")
    print("1: Add a new transaction to the logbook")
    print("2: View blockchain")
    print("3: Admin controls")
    print("4: Exit")

    choice=input("Select: ")
    if(choice == '1'): 
        data=input("Please enter transaction data: ")
        amount=input("Please enter amount: ")
        new_tran=Transaction(data,amount,time())
        unverified.append(new_tran)
        node_return1=n1.get_verified(new_tran.to_string)
        node_return2=n2.get_verified(new_tran.to_string)
        node_return3=n3.get_verified(new_tran.to_string)
        if(node_return1=='Verified' and node_return2=='Verified' and node_return3=='Verified'):
            bcn.add_new_block(new_tran.data,new_tran.amount,new_tran.timestamp)

    elif(choice == '2'):
        for block in bcn.blocks:
            print()
            print(block.to_string())

    elif(choice == '3'):
        password=input("Please enter admin password: ")
        if(password!="Uranus"):
            print("Incorrect password")
            continue
        print("Please choose an option: ")
        print("1: View unverified transactions")
        print("2: View verified transactions")
        admin_choice=input("Select: ")
        continue

    elif(choice == '4'):
        break
    
    else:
        print("Invalid Input.Try again")
        continue