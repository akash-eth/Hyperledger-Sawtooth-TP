import sawtooth_sdk
class XoTransactionHandler:
    def __init__(self, namespace_prefix):
        self._namespace_prefix = namespace_prefix

    @property
    def family_name(self):
        return 'xo'

    @property
    def family_versions(self):
        return ['1.0']

    @property
    def encodings(self):
        return ['csv-utf8']

    @property
    def namespaces(self):
        return [self._namespace_prefix]

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