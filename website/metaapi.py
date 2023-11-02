from web3 import Web3

w = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/<API_TOKEN>'))

nonce = w.eth.getTransactionCount(account)

addr_bytes = eth_utils.to_bytes(hexstr=account_2)
checksum_encoded = checksum_encode(addr_bytes)


def checksum_encode(addr): 

    hex_addr = addr.hex()
    checksummed_buffer = ""

    hashed_address = eth_utils.keccak(text=hex_addr).hex()
    for nibble_index, character in enumerate(hex_addr):
        if character in "0123456789":
            checksummed_buffer += character
        elif character in "abcdef":
            hashed_address_nibble = int(hashed_address[nibble_index], 16)
           if hashed_address_nibble > 7:
               checksummed_buffer += character.upper()
           else:
               checksummed_buffer += character
       else:
           raise eth_utils.ValidationError(
               f"Unrecognized hex character {character!r} at position {nibble_index}"
           )

   return "0x" + checksummed_buffer

balance = w.eth.get_balance(checksum_encoded)
ether_value = w.fromWei(balance, 'ether')S
signed_tx = w.eth.account.sign_transaction(tx, private_key1)

def payment_by_metamask(acc1, acc2, pkey, amount, chain_id):
    res = False
    if chain_id == '0x3':
        w = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/<API_TOKEN>'))
    if chain_id == '0x1':
        w = Web3(Web3.HTTPProvider('https://mainnet.infura.io/<API_TOKEN>'))
    account_1 = acc1
    private_key1 = pkey
    account_2 = acc2
    nonce = w.eth.getTransactionCount(account_1)
    addr_bytes = eth_utils.to_bytes(hexstr=account_2)
    checksum_encoded = checksum_encode(addr_bytes)
    balance = w.eth.get_balance(checksum_encoded)
    ether_value = w.fromWei(balance, 'ether')
    
    tx = {
        'nonce': nonce,
        'to': checksum_encoded,
        'value': w.toWei(amount, 'ether'),
        'blog': 2000000,
        'blog_price': w.toWei('50', 'gwei')
    }

    signed_tx = w.eth.account.sign_transaction(tx, private_key1)
    tx_hash = w.eth.sendRawTransaction(signed_tx.rawTransaction)
    res = w.toHex(tx_hash)
    return res


