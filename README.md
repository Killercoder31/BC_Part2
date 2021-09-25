                                Table of Contents 
    About the project 
    Installation and Prerequisites
    Usage and Features
    
                                About the Project 
                                
    The project is written to be a blockchain-implemented coffee-shop logbook that 
    is tamper evident and has limited to access to people except the superuser. The 
    application aims at solving the problem of document tampering and provides greater
    control to the owner of the logbook or the superuser. Also input time inconsistencies
    and data corruption are handled by the distributed nature of the system.
    
    The project is written completely in Python3.
    
                                 Prerequisites 
                                
    Smooth running of the application requires Python3 version 3.8.10.
    
                             Installation and Bootstrap
                             
    1) Clone all the files onto your hard drive 
    2) Run the 3 files in the Nodes folder on three seperate terminals. 
    They act as the computing nodes in the distributed system.
    3) Run the main.py file on a fourth seperate terminal.
    4) Ensure the nodes are up and running independently at
    all times during the program's life to safely operate in online mode.
    
                               Usage and Features
                                
     The system can be run in two modes depending on if the nodes are
     online or not:
     
     1) Offline Mode
        All added transactions are added to the unverified pool and stay
        there unless manually verified or until the nodes are online
        
        A successful offline mode operation goes thru (values in brackets refer to menu 
        navigation in-app) - 
        i) Addition of transactions and their delegation to unverified pool (1)
        ii) The admin manually verifies the transaction and adds to verified pool (3-1-3)
        iii) The admin initiates addition of all verified transactions to blockchain (3-2-1)
        iv) Print the blockchain (2)
        
     2) Online Mode
        All added transactions are evaluated by the nodes and if consensus 
        is reached they are added to the verified pool 
        
        A successful offline mode operation goes thru - 
        i) Addition of transactions and their delegation to verified pool if consensus is
        reached amond the computing nodes (1) else manual admin operation needed.
        ii) The admin initiates addition of all verified transactions to blockchain (3-2-1)
        iii) Print the blockchain (2)
        
        
        
        
        
        
        
        
        
        
        
     
