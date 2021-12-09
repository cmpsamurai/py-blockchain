from datetime import datetime
import logging
from blockchain import Block, calculate_block_hash
from blockchain.blockchain import BlockChain


def generate_next_block(blockchain, data: str):
    pass


def create_genesis_block(data):
    genesis_block_timestamp = datetime.now().timestamp()
    genesis_block_hash = calculate_block_hash(0, "", genesis_block_timestamp,  data)

    genesis_block = Block(
        0,
        genesis_block_hash,
        "",
        genesis_block_timestamp,
        data
    )
    return genesis_block

def main():
    #genesis_block = create_genesis_block("Test Block Data 1")
    
    genesis_block = Block(
        0,
        'bc48c2c971c48f6b767b059885a51b4e753ae0928dd69b0ec0ce3ae4b6311d56',
        None,
        1638999821.017757,
        "My Genesis Block!!"
    )
    
    blockchain = BlockChain(genesis_block)
    blockchain.add_block(blockchain.generate_next_block("Test Block Data 1"))
    blockchain.add_block(blockchain.generate_next_block("Test Block Data 2"))
    blockchain.add_block(blockchain.generate_next_block("Test Block Data 3"))


    o_blockchain = BlockChain(genesis_block)
    o_blockchain.add_block(o_blockchain.generate_next_block("Test Block Data 1"))
    o_blockchain.add_block(o_blockchain.generate_next_block("Test Block Data 2"))
    o_blockchain.add_block(o_blockchain.generate_next_block("Test Block Data 3"))
    o_blockchain.add_block(o_blockchain.generate_next_block("Test Block Data 4"))


    blockchain.replace_chain(o_blockchain)

    logging.info("Is Valid Blockchain: %s", blockchain.is_valid_blockchain())
    
    



if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()