from block import Block
from blockchain import Blockchain
from time import time
from transaction import Transaction
from nodes import Node

# bcn serves as the logical blockchain in the app
# the transactions once inputed are divided into two pools unverified and verified 
# a transaction first is assigned to the unverified pool. From there if all nodes are active and they form consensus then it is verified.
# It can also be verified manually by Dexter the admin by using his special access password or removed by him on suspicion of tampering or if refunded.
# Once verified the transaction can be added to blockchain by using admin special access by Dexter
bcn=Blockchain()
unverified=[]
verified=[]

# the three nodes are initialised and a connection is attempted 
host='127.0.0.1'
port=12345
n1=Node('Pluto')
n2=Node('Jupiter')
n3=Node('Titan')
connError=0

# if connection cannot be made the app runs in offline mode and does not verify any transactions by consensus. Once the nodes are online 
# the superuser can batch process them to be verified by consensus or can manually verify and add to the verified pool
try:
    n1.connect_to_node('127.0.0.1',12344)
    n2.connect_to_node('127.0.0.1',12345)
    n3.connect_to_node('127.0.0.1',12346)
except:
    connError=1


while(1):
    print("Please select an option: ")
    print("1: Add a new transaction to the logbook\t2: View blockchain\t3: Admin controls\t4: Exit")
    choice=input("Select: ")
    print("\n\n")

    # the new transaction is compiled by using details given by user and computing timestamp and added to the unverified pool 
    # if all nodes are found to be online it is batched for verification else it sits in the unverified pool for superuser intervention
    if(choice == '1'): 
        data=input("Please enter transaction data: ")
        amount=input("Please enter amount: ")
        print("\n\n")
        new_tran=Transaction(data,amount,time())
        unverified.append(new_tran)

        # if the nodes are not connected a connection is retried and if error persists the transaction is ignored
        if(connError==1):
            n1.close_conn()
            n2.close_conn()
            n3.close_conn()
            connError=0
            try:
                n1.connect_to_node('127.0.0.1',12344)
                n2.connect_to_node('127.0.0.1',12345)
                n3.connect_to_node('127.0.0.1',12346)
            except:
                connError=1
        if(connError==0):
            node_return1=n1.get_verified(new_tran.to_string)
            node_return2=n2.get_verified(new_tran.to_string)
            node_return3=n3.get_verified(new_tran.to_string)
            if(node_return1=='Verified' and node_return2=='Verified' and node_return3=='Verified'):
                verified.append(new_tran)
                unverified.remove(new_tran)

    # displays the complete blockchain as of that moment 
    elif(choice == '2'):
        for block in bcn.blocks:
            print()
            print(block.to_string())

    # Admin superuser access to the application. Note this part can only be accessed by Dexter with a password required for authentication
    elif(choice == '3'):
        password=input("Please enter admin password('Uranus'): ")
        print()
        if(password!="Uranus"):
            print("Incorrect password")
            continue

        # once the user is authenticated he can view the transactions currently lying in either the verified or unverified pool
        # each choice opens a sub-menu presenting further options to edit said pools
        print("Please select an option: ")
        print("1: View unverified transactions\t2: View verified transactions")
        admin_choice=input("Select: ")
        print("\n\n")

        if(admin_choice=='1'):
            if(len(unverified)==0):
                print("No unverified transactions")
                continue
            for tran in unverified:
                print("{0}\t{1}\t{2}\t{3}".format(unverified.index(tran),tran.data,tran.amount,tran.timestamp))

            # sub-menu that lists options to deal with the unverified pool of transactions
            print("Please choose an option: ")
            print("1: Send all for verification (Please ensure all nodes are online)\t2: Remove transaction from list\t3: Verify all\t4: Return")
            unverified_choice=input("Select: ")
            print("\n\n")

            # if the transactions are sent for re-verification connection with all nodes is restarted and if found online transactions are processed by them 
            # if not they are ignored 
            if(unverified_choice=='1'):
                reConnError=0
                n1.close_conn
                n2.close_conn
                n3.close_conn
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

            # in case a transaction has to be removed 
            elif(unverified_choice=='2'):
                tran_index=input("Enter index of transaction")
                if(int(tran_index)<len(unverified)):
                    unverified.remove(unverified[int(tran_index)])
                else:
                    print("Invalid index")
                    continue

            # in case a transaction is manually verified by superuser
            elif(unverified_choice=='3'):
                for tran in unverified:
                    verified.append(tran)
                unverified.clear()
            
            # to return 
            elif(unverified_choice=='4'):
                continue

            # for invalid inputs
            else: 
                continue
            

        # in case the superuser chooses to see the verified pool     
        elif(admin_choice=='2'):
            if(len(verified)==0):
                print("No verified transactions")
                continue
            for tran in verified:
                print("{0}\t{1}\t{2}\t{3}".format(verified.index(tran),tran.data,tran.amount,tran.timestamp))
            
            print("Please choose an option: ")
            print("1: Add all to blockchain\t2: Remove transaction from list\t3: Return")
            verified_choice=input("Select: ")
            print("\n\n")

            # if the verified transactions are added to the blockchain-implemented logbook by the user
            if(verified_choice=='1'):
                for tran in verified: 
                    bcn.add_new_block(tran.data,tran.amount,tran.timestamp)
                verified.clear()

            # incase a transaction has to be removed from the verified transactions
            elif(verified_choice=='2'):
                tran_index=input("Enter index of transaction")
                if(int(tran_index)<len(verified)):
                    verified.remove(verified[int(tran_index)])
                else:
                    print("Invalid index")
                    continue

            # to return and cases of invalid input
            else: 
                continue
        else:
            continue

    # ends the program
    elif(choice == '4'):
        break

    # to handle invalid input
    else:
        print("Invalid Input.Try again")
        continue