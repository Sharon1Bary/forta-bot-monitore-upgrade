from forta_agent import get_json_rpc_url
from web3 import Web3
from web3.providers.rpc import HTTPProvider

import dataclasses


@dataclasses.dataclass
class BotHelper:
    def __init__(self):
        self.w3 = Web3(HTTPProvider(get_json_rpc_url()))
        self.contract_address: str = '0x41545f8b9472D758bB669ed8EaEEEcD7a9C4Ec29'

        self.upgrade_abi: str = '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address",' \
                                '"name":"implementation","type":"address"}],"name":"Upgraded","type":"event"}'

    def get_w3(self):
        return self.w3
