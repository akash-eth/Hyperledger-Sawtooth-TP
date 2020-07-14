def apply(self, transaction, context):
    signer, game_name, action, space = \
        self._unpack_transaction(transaction)

    board, state, player1, player2 = \
        self._get_state_data(game_name, context)

    updated_game_data = self._play_xo(
        board, state,
        player1, player2,
        signer, action, space
    )

    self._store_game_data(game_name, updated_game_data, context)

def _unpack_transaction(self, transaction):
    header = transaction.header
    signer = header.signer

    try:
        game_name, action, space = self._decode_data(transaction.payload)
    except:
        raise InvalidTransaction("Invalid payload serialization")

    return signer, game_name, action, space