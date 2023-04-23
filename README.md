# Monitoring Contract Upgrade Bot

## Description

This bot detect if a contract was upgraded.

## Supported Chains

- All supported.


## Alerts

Fires and alert when a contract creation is detected which the first four/last four chars in the contract are identical.
- MONITORING-CONTRACT-UPGRADE
  - Severity is always set to "Info" 
  - Type is always set to "Suspicious" 
  - Mention will include the upgraded contract address.

## Test Data

The agent behaviour can be verified with the following transactions:

- 0x3a0f757030beec55c22cbc545dd8a844cbbb2e6019461769e1bc3f3a95d10826 (15,000 USDT)
