#unpacking the transactions:
def _unpack_transaction(self, transaction):
    header = transaction.header
    signer = header.signer

    try:
        game_name, action, space = self._decode_data(transaction.payload)
    except:
        raise InvalidTransaction("Invalid payload serialization")

    return signer, game_name, action, space