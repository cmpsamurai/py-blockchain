from datetime import datetime
from . import Block, calculate_block_hash

import logging 

class BlockChain:
    def __init__(self, genesis_block):
        self.blocks = [genesis_block]

    def add_block(self, block: Block):
        # Allow adding block only if Genesis Block or valid block
        if len(self.blocks) == 0 or self.is_valid_block(block, self.get_latest_block()):
            self.blocks.append(block)


    def generate_next_block(self, data:str):
        previous_block = self.get_latest_block()
        next_index = previous_block.index + 1
        next_timestamp = datetime.now().timestamp()
        new_block_hash = calculate_block_hash(next_index, previous_block.hash, next_timestamp, data)
        new_block = Block(
            next_index,
            new_block_hash,
            previous_block.hash,
            next_timestamp,
            data
        )
        return new_block


    def is_valid_block(self, block: Block, previous_block: Block):
        # Check block index
        if previous_block.index + 1 != block.index:
            logging.error("Invalid link between %d -> %d:", previous_block, block)
            return False

        # Check previous block hash equls block hash
        if previous_block.hash != block.prev_hash:
            logging.error("Invalid stored previous hash for block: %s", block)
            return False

        # Check block hash
        if block.calculate_block_hash() != block.hash:
            logging.error("Invalid hash for block: %s", block)
            return False
        return True


    def is_valid_blockchain(self):
        logging.info("Checking integrity of Blockchain: %s", self)
        # Blockchain is invalid if it doesn't have a Genesis block.
        if len(self.blocks)  == 0:
            logging.error("Invalid Blockchain with length: %d", len(self.blocks))
            return False

        # Validate chain
        for idx in range(1, len(self.blocks)):
            logging.info("Checking integrity of Block: %s", self.blocks[idx])
            if not self.is_valid_block(self.blocks[idx], self.blocks[idx - 1]):
                logging.error("Checking integrity of Blockchain: %s failed!!.", self)
                return False
        
        # Blockchain is valid
        logging.info("Blockchain: %s is valid!", self)
        return True


    def length(self) -> int:
        return len(self.blocks)
    
    def get_genesis_block(self) -> Block:
        return self.blocks[0]


    def replace_chain(self, other_chain):
        if self.get_genesis_block() != other_chain.get_genesis_block():
            logging.error("Received blockchain with invalid Genesis block: %s", other_chain)
        elif other_chain.is_valid_blockchain() and other_chain.length() > self.length():
            logging.error("Received blockchain: %s is valid. Replacing current blockchain with received blockchain", other_chain)
            self.blocks = other_chain.blocks
        else:
            logging.error("Received invalid blockchain: %s", other_chain)


    def get_latest_block(self)-> Block:
        return self.blocks[-1]

    def __str__(self) -> str:
        return "Blockchain[genesis[:8]=%s, size=%d]" % (
            self.get_genesis_block().hash[:8],
            self.length()
        )