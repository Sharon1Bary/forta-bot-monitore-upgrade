from src.web3_mock import CONTRACT, Web3Mock

import src.agent


class TestSocialEngContractBot:

    def test_returns_finding(self):

        mock_tx_event = Web3Mock()
        mock_tx_event.to = CONTRACT

        src.agent.handle_transaction(mock_tx_event)
        findings = src.agent.handle_transaction(mock_tx_event)
        assert len(findings) == 1



