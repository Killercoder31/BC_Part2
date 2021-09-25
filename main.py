from block import Block
from blockchain import Blockchain
from time import time
from transaction import Transaction
from nodes import Node

bcn=Blockchain()
unverified=[]
verified=[]
host='127.0.0.1'
port=12345

n1=Node('Pluto')
n2=Node('Jupiter')
n3=Node('Titan')
connError=0
try:
    n1.connect_to_node('127.0.0.1',12344)
    n2.connect_to_node('127.0.0.1',12345)
    n3.connect_to_node('127.0.0.1',12346)
except:
    connError=1

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
        if(connError==0):
            node_return1=n1.get_verified(new_tran.to_string)
            node_return2=n2.get_verified(new_tran.to_string)
            node_return3=n3.get_verified(new_tran.to_string)
            if(node_return1=='Verified' and node_return2=='Verified' and node_return3=='Verified'):
                verified.append(new_tran)
                unverified.remove(new_tran)

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

        if(admin_choice=='1'):
            if(len(unverified)==0):
                print("No unverified transactions")
                continue
            for tran in unverified:
                print("{0}\t{1}\t{2}\t{3}".format(unverified.index(tran),tran.data,tran.amount,tran.timestamp))

            print("Please choose an option: ")
            print("1: Send all for verification (Please ensure all nodes are online")
            print("2: Remove transaction from list")
            print("3: Verify all")
            print("4: Return")
            unverified_choice=input("Select: ")

            if(unverified_choice=='1'):
                reConnError=0
                try:
                    n1.connect_to_node('127.0.0.1',12344)
                    n2.connect_to_node('127.0.0.1',12345)
                    n3.connect_to_node('127.0.0.1',12346)
                except:
                    reConnError=1
                
                if(reConnError==1):
                    print("Please ensure all nodes are active")
                    continue
                else:
                    for tran in unverified:
                        node_return1=n1.get_verified("{0},{1},{2}".format(tran.data,tran.amount,tran.timestamp))
                        node_return2=n2.get_verified("{0},{1},{2}".format(tran.data,tran.amount,tran.timestamp))
                        node_return3=n3.get_verified("{0},{1},{2}".format(tran.data,tran.amount,tran.timestamp))
                        if(node_return1=='Verified' and node_return2=='Verified' and node_return3=='Verified'):
                            verified.append(tran)
                            unverified.remove(tran)
            elif(unverified_choice=='2'):
                tran_index=input("Enter index of transaction")
                if(int(tran_index)<len(unverified)):
                    unverified.remove(unverified[int(tran_index)])
                else:
                    print("Invalid index")
                    continue
            elif(unverified_choice=='3'):
                for tran in unverified:
                    verified.append(tran)
                unverified.clear()
            else: 
                continue
            
        elif(admin_choice=='2'):
            if(len(verified)==0):
                print("No verified transactions")
                continue
            for tran in verified:
                print("{0}\t{1}\t{2}\t{3}".format(verified.index(tran),tran.data,tran.amount,tran.timestamp))
            
            print("Please choose an option: ")
            print("1: Add all to blockchain")
            print("2: Remove transaction from list")
            print("3: Return")
            verified_choice=input("Select: ")

            if(verified_choice=='1'):
                for tran in verified: 
                    bcn.add_new_block(tran.data,tran.amount,tran.timestamp)
                verified.clear()
            elif(verified_choice=='2'):
                tran_index=input("Enter index of transaction")
                if(int(tran_index)<len(verified)):
                    verified.remove(verified[int(tran_index)])
                else:
                    print("Invalid index")
                    continue
            else: 
                continue
        else:
            continue

    elif(choice == '4'):
        break
    
    else:
        print("Invalid Input.Try again")
        continue