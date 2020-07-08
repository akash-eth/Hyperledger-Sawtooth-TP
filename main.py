import sawtooth_sdk

from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_xo.processor.handler import XoTransactionHandler

def main():

    processor = TransactionProcessor(url='tcp://localhost:4004') #this is validator's url

    handler = XoTransactionHandler()

    processor.add_handler(handler)

    processor.start()
    