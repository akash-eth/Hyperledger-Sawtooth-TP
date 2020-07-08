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

        #...