from block import Block
from time import time

class Blockchain():
    def __init__(self):
        self.blocks=[]
        self.set_genesis_block()

    def set_genesis_block(self):
        data="Dexter no Blockchain"
        prev_hash='0'*64
        genesis_block=Block(data,0,time(),prev_hash)
        self.blocks.append(genesis_block)

    def get_last_hash(self):
        last_block=self.blocks[-1]
        last_hash=last_block.hash
        return (last_hash)
    
    def add_new_block(self,data,amount,timestamp):
        prev_hash=self.get_last_hash()
        new_block=Block(data,amount,timestamp,prev_hash)
        self.blocks.append(new_block)