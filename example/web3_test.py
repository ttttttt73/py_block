from web3 import Web3, HTTPProvider
import time
from logzero import logger


rpc_url = "http://localhost:8545"
w3 = Web3(HTTPProvider(rpc_url))
w3.geth.personal.unlockAccount(w3.eth.accounts[0], "password", 0)

contract = w3.eth.contract(abi=,
        bytecode=,
        bytecode_runtim=
        )

tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0]})

w3.miner.start(2)
time.sleep(5)
w3.miner.stop()

contract_instance = contract(contrat_address)


def deploy(contract_file_name, contract_name):
    compiled_sol = compile_files([contract_file_name])
    interface = compiled_sol[f'{contract_file_name}:{contract_name}')
    contract = w3.eth.contract(abi=interface['abi'], bytecode=interface['bin'], bytecode_runtime=interface['bin-runtime'])




def uplaod(ins, filehash, filename, filesize, owner):
    logger.info("Call upload")
    logger.info(f"{owner}, {filehash}, {filename}, {filesize}")
    transaction = ins.transact({"from": w3.eth.accounts[0]})
    tx_hash = transaction.upload(owner, filehash, filename, filesize)
    logger.info(f"Wait Uploading: {tx_hash}")
    w3.miner.start(2)
    time.sleep(5)
    w3.miner.stop()
    logger.info("Finish Uploading")


def get_file_info(ins, filehash):
    logger.info("Call get_file_info")
    logger.debug(filehash)
    file_info = ins.call().getFileInfo(filehash)
    logger.debug(file_info)
    return file_info


def check_file_exist(ins, filehash):
    logger.info("Call check_file_exist")
    logger.debug(filehash)
    is_exist = ins.call().checkExist(filehash)
    logger.debug(is_exist)
    return is_exist
