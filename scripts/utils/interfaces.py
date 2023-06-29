from brownie import interface

from scripts.utils.constants import (
    DEPOSIT_CONTRACT,
    DAWN_DEPOSIT_SECURITY_MODULE,
    DAWN_DEPOSIT,
    DAWN_DEPOSIT_NODE_MANAGER,
)
from scripts.utils.variables import WEB3_CHAIN_ID, ACCOUNT
DepositContractInterface = interface.DepositContract(DEPOSIT_CONTRACT[WEB3_CHAIN_ID], owner=ACCOUNT)

DawnDepositSecurityModuleInterface = interface.DawnDepositSecurityModule(
    DAWN_DEPOSIT_SECURITY_MODULE[WEB3_CHAIN_ID], owner=ACCOUNT)
DawnDepositInterface = interface.DawnDeposit(DAWN_DEPOSIT[WEB3_CHAIN_ID], owner=ACCOUNT)
DawnDepositNodeManagerInterface = interface.DawnDeposit(DAWN_DEPOSIT_NODE_MANAGER[WEB3_CHAIN_ID], owner=ACCOUNT)
