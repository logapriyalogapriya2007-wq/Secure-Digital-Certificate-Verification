import hashlib
import json
from datetime import datetime


class Block:

    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.create_hash()

    def create_hash(self):

        text = (
            str(self.index)
            + self.timestamp
            + json.dumps(self.data, sort_keys=True)
            + self.previous_hash
        )

        return hashlib.sha256(text.encode()).hexdigest()


class Blockchain:

    def __init__(self):
        self.chain = [self.genesis_block()]

    def genesis_block(self):

        return Block(
            0,
            {"message": "Genesis Block"},
            "0"
        )

    def add_block(self, data):

        previous_hash = self.chain[-1].hash

        block = Block(
            len(self.chain),
            data,
            previous_hash
        )

        self.chain.append(block)

        return block

    def find_certificate(self, certificate_id):

        for block in self.chain:

            if block.data.get("certificate_id") == certificate_id:
                return block

        return None

    def verify_chain(self):

        for i in range(1, len(self.chain)):

            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.create_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True


blockchain = Blockchain()