import sawtooth_sdk

from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_xo.processor.handler import XoTransactionHandler

def main():

    processor = TransactionProcessor(url='tcp://localhost:4004') #this is validator's url

    handler = XoTransactionHandler()

    processor.add_handler(handler)

    processor.start()

from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory

context = create_context('secp256k1')
private_key = context.new_random_private_key()
signer = CryptoFactory(context).new_signer(private_key)

import cbor

payload = {
    'Verb': 'set',
    'Name': 'foo',
    'Value': 42}

payload_bytes = cbor.dumps(payload)

from hashlib import sha512
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader
