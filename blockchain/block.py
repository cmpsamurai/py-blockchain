import hashlib
from dataclasses import dataclass

@dataclass
class Block:
    index: int
    hash: str
    prev_hash: str
    timestamp: int
    data: str

    def calculate_block_hash(self) -> str:
        return calculate_block_hash(
            self.index,
            self.prev_hash,
            self.timestamp,
            self.data
        )
    def __str__(self) -> str:
        return "Block[idx=%d, contentSize=%d, hash[:8]=%s]" % (
            self.index,
            len(self.data),
            self.hash[:8]
        )
    
def calculate_block_hash(index: int, prev_hash: str, timestamp: int, data: str) -> str:
    m = hashlib.sha256()
    payload = "%s%s%s%s" % (
        index,
        prev_hash,
        timestamp,
        data
    )
    m.update(payload.encode("utf8")) 
    return m.hexdigest()

