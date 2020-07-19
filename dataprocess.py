#unpacking the transactions:
def _unpack_transaction(self, transaction):
    header = transaction.header
    signer = header.signer

    try:
        game_name, action, space = self._decode_data(transaction.payload)
    except:
        raise InvalidTransaction("Invalid payload serialization")

    return signer, game_name, action, space

    #correcting the game data processing:
    def _get_state_data(self, game_name, context):
    game_address = self._make_game_address(game_name)

    state_entries = context.get_state([game_address])

    try:
        return self._decode_data(state_entries[0].data)
    except IndexError:
        return None, None, None, None
    except:
        raise InternalError("Failed to deserialize game data.")

    #making game data address:
    def _make_game_address(self, game_name):
    prefix = self._namespace_prefix
    game_name_utf8 = game_name.encode('utf-8')
    return prefix + hashlib.sha512(game_name_utf8).hexdigest()[0:64]

    #storing the game data:
    def _store_game_data(self, game_name, game_data, context):
    game_address = self._make_game_address(game_name)

    encoded_game_data = self._encode_data(game_data)

    addresses = context.set_state(
        {game_address: encoded_game_data}
    )

    if len(addresses) < 1:
        raise InternalError("State Error")