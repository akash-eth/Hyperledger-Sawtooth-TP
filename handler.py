import sawtooth_sdk

class XoTransactionHandler(TransactionHandler):
    def __init__(self, namespace_prefix):
        self._namespace_prefix = namespace_prefix

    @property
    def family_name(self):
        return 'xo'
    
    @property
    def family_version(self):
        return ['1.0']
    
    @property
    def namespaces(self):
        return [self._namespace_prefix]

    def apply(self, trasaction, context):

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

    def _get_state_data(self, game_name, context):
    game_address = self._make_game_address(game_name)

    state_entries = context.get_state([game_address])

    try:
        return self._decode_data(state_entries[0].data)
    except IndexError:
        return None, None, None, None
    except:
        raise InternalError("Failed to deserialize game data.")

    def _make_game_address(self, game_name):
    prefix = self._namespace_prefix
    game_name_utf8 = game_name.encode('utf-8')
    return prefix + hashlib.sha512(game_name_utf8).hexdigest()[0:64]

    def _store_game_data(self, game_name, game_data, context):
    game_address = self._make_game_address(game_name)

    encoded_game_data = self._encode_data(game_data)

    addresses = context.set_state(
        {game_address: encoded_game_data}
    )

