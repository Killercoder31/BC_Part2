from hashlib import sha256

# a block class acts as the basic building block of the blockchain-implemented logbook 

class Block():

    # a block is initialised with transaction data/remarks, the amount that is associated, the timestamp and the hash of the previous block
    # the hash for the block is calculated using python hashlib sha256
    def __init__(self,data,amount,timestamp,previous_block_hash):
        self.data=data
        self.amount=amount
        self.timestamp=timestamp
        self.prev_block_hash=previous_block_hash
        self.calculate_valid_hash()
    
    # a generated hash is considered valid if it has '3' zeros int the starting in its 64-bit hex representation of its 256-bit binary sha256 encrypted code
    def is_hash_valid(self,hash):
        return (hash.startswith('0'*3))
    
    # function to generate a valid hash that satisfies above condition by incrementing nonce and repeatedly trying out combinations 
    def calculate_valid_hash(self):
        hash=''
        nonce=0

        while(not self.is_hash_valid(hash)):
            temp=self.to_string()+str(nonce)
            hash=sha256(temp.encode()).hexdigest()
            nonce+=1
        
        self.hash=hash
    
    # returns string representation of the block 
    def to_string(self):
        return "{0}\t{1}\t{2}\t{3}".format(self.data,self.amount,self.timestamp,self.prev_block_hash)