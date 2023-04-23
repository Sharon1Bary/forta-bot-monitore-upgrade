from forta_agent import get_json_rpc_url, Finding, FindingType, FindingSeverity
from web3 import Web3
from web3.providers.rpc import HTTPProvider
from hexbytes import HexBytes

import logging

logger = logging.getLogger(__name__)


def is_contract(address):
    code = w3.eth.get_code(Web3.to_checksum_address(address))
    return code != HexBytes('0x')


# Return Contract bytes.
def calc_contract_address(address):
    return bytes.fromhex(address[2:].lower())


# Add to Finding.
def add_to_fining(findings: list):
    findings.append(Finding({
        'name': "Monitoring Contract Upgrade Bot",
        'description': f'A contract ({contract_address}) was upgraded',
        'alert_id': "MONITORING-CONTRACT-UPGRADE",
        'severity': FindingSeverity.Info,
        'type': FindingType.Suspicious,
        'metadata': {
            'account': contract_address,
            '': ''
        }
    }))


# Compare between 2 bytecode and trigger if detect changing .
def compare_bytes(byte_from, byte_contrat):
    if byte_from != byte_contrat:
        return True
    else:
        return False


def handle_transaction(transaction_event):
    findings = []

    try:
        # Get list of Upgrade events. (based on contact and Upgrade abi) if there is it can point on upgrade.
        # This is not a strong condition, however it can point on the change.
        if len(transaction_event.filter_log(upgrade_abi, contract_address)) > 0:
            add_to_fining(findings)

        if w3.is_connected():
            # Check if the transaction address is a contract.
            if is_contract(transaction_event.to):
                # Check if the transaction_event contract equals to the contract we are monitoring and, get the
                # transaction_contract code byte and our contract byte code and, check if was upgraded by bytes.
                if transaction_event.from_ == contract_address and \
                        compare_bytes(calc_contract_address(transaction_event.from_),
                                      calc_contract_address(contract_address)):
                    add_to_fining(findings)
    except Exception as e:
        print(e)
    return findings


contract_address = '0x41545f8b9472D758bB669ed8EaEEEcD7a9C4Ec29'
upgrade_abi = '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"}'
w3 = Web3(HTTPProvider(get_json_rpc_url()))
