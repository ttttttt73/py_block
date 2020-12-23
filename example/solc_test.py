import time
from web3 import Web3, HTTPProvider
from solcx import compile_source


contract_source_code = '''
contract Greeter {
    string public greeting;
    function Greeter() {
        greeting = 'Hello';
    }
    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }
    function greet() constant returns (string) {
        return greeting;
    }
}
'''

compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:Greeter']

print(contract_interface['abi'])
# print(contract_interface['bin'])
