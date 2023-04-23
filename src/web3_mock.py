from hexbytes import HexBytes

CONTRACT = '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11'


class Web3Mock:
    def __init__(self):
        self.eth = EthMock()
        self.eth = EthMock()

    def filter_log(self, abi, address):
        return [address]


class EthMock:
    def __init__(self):
        self.contrat = ContratMock()

    def chain_id(self):
        return 1

    def get_code(self, address: str):
        if address == CONTRACT:
            return HexBytes('0x03087766bf68e78671d1ea436ae087da74a12761dac020011a9eddc4900bf13b')
        else:
            return HexBytes('0x03087766bf68e78671d1ea436ae087da74a12761dac020011a9eddc4900bf13b')


class ContratMock:
    def __init__(self):
        self.functions = FunctionsMock()

    def __call__(self, address, *args, **kwargs):
        return self


class FunctionsMock:
    def __init__(self):
        self.return_value = None

    def call(self, *_, **__):
        return self.return_value
