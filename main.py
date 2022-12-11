import time
import requests
from web3 import Web3
import json as js
import undetected_chromedriver as uc
from pprint import pprint
from eth_account.messages import encode_defunct
from check_mail import check_mail1 as cm
import threading

# Option
number_of_threads = 1  # Кол-во потоков


def confirm_mail(mail1, pasw1, _from1):
    driver = uc.Chrome()
    page = cm(mail1, pasw1, _from1)[0]
    print(page)
    driver.get(page)
    time.sleep(7)
    driver.close()
    driver.quit()


def main():
    while keys_list and mail_list:
        RPC = 'https://polygon-rpc.com'
        privatekey = keys_list.pop(0)
        contract_adr = Web3.toChecksumAddress('0xBc2Cf251Cf812Ca54BB5289001d4B09f0967D659')
        contract_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"newRoyaltyRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"newRoyaltyBps","type":"uint256"}],"name":"DefaultRoyalty","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prevOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"platformFeeRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"platformFeeBps","type":"uint256"}],"name":"PlatformFeeInfoUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"}],"name":"PrimarySaleRecipientUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"royaltyRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"royaltyBps","type":"uint256"}],"name":"RoyaltyForToken","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"mintedTo","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenIdMinted","type":"uint256"},{"indexed":false,"internalType":"string","name":"uri","type":"string"},{"indexed":false,"internalType":"uint256","name":"quantityMinted","type":"uint256"}],"name":"TokensMinted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"signer","type":"address"},{"indexed":true,"internalType":"address","name":"mintedTo","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenIdMinted","type":"uint256"},{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"address","name":"royaltyRecipient","type":"address"},{"internalType":"uint256","name":"royaltyBps","type":"uint256"},{"internalType":"address","name":"primarySaleRecipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint128","name":"validityStartTimestamp","type":"uint128"},{"internalType":"uint128","name":"validityEndTimestamp","type":"uint128"},{"internalType":"bytes32","name":"uid","type":"bytes32"}],"indexed":false,"internalType":"struct ITokenERC1155.MintRequest","name":"mintRequest","type":"tuple"}],"name":"TokensMintedWithSignature","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"burnBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"getDefaultRoyaltyInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPlatformFeeInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"getRoyaltyInfoForToken","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_defaultAdmin","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"string","name":"_contractURI","type":"string"},{"internalType":"address[]","name":"_trustedForwarders","type":"address[]"},{"internalType":"address","name":"_primarySaleRecipient","type":"address"},{"internalType":"address","name":"_royaltyRecipient","type":"address"},{"internalType":"uint128","name":"_royaltyBps","type":"uint128"},{"internalType":"uint128","name":"_platformFeeBps","type":"uint128"},{"internalType":"address","name":"_platformFeeRecipient","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"string","name":"_uri","type":"string"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"mintTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"address","name":"royaltyRecipient","type":"address"},{"internalType":"uint256","name":"royaltyBps","type":"uint256"},{"internalType":"address","name":"primarySaleRecipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint128","name":"validityStartTimestamp","type":"uint128"},{"internalType":"uint128","name":"validityEndTimestamp","type":"uint128"},{"internalType":"bytes32","name":"uid","type":"bytes32"}],"internalType":"struct ITokenERC1155.MintRequest","name":"_req","type":"tuple"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"mintWithSignature","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextTokenIdToMint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"platformFeeRecipient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"primarySaleRecipient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"salePrice","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"royaltyAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"saleRecipientForToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_uri","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_royaltyRecipient","type":"address"},{"internalType":"uint256","name":"_royaltyBps","type":"uint256"}],"name":"setDefaultRoyaltyInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newOwner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_platformFeeRecipient","type":"address"},{"internalType":"uint256","name":"_platformFeeBps","type":"uint256"}],"name":"setPlatformFeeInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_saleRecipient","type":"address"}],"name":"setPrimarySaleRecipient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_bps","type":"uint256"}],"name":"setRoyaltyInfoForToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"uri","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"to","type":"address"},{"internalType":"address","name":"royaltyRecipient","type":"address"},{"internalType":"uint256","name":"royaltyBps","type":"uint256"},{"internalType":"address","name":"primarySaleRecipient","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"uint256","name":"pricePerToken","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint128","name":"validityStartTimestamp","type":"uint128"},{"internalType":"uint128","name":"validityEndTimestamp","type":"uint128"},{"internalType":"bytes32","name":"uid","type":"bytes32"}],"internalType":"struct ITokenERC1155.MintRequest","name":"_req","type":"tuple"},{"internalType":"bytes","name":"_signature","type":"bytes"}],"name":"verify","outputs":[{"internalType":"bool","name":"","type":"bool"},{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'
        _mail = mail_list.pop(0)
        mail = _mail.split(':')[0]
        pasw = _mail.split(':')[1]
        web3 = Web3(Web3.HTTPProvider(RPC))
        account = web3.eth.account.privateKeyToAccount(privatekey)
        address_wallet = account.address
        url = 'https://mirror-api.com/graphql'
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en;q=0.9',
            'content-length': '411',
            'content-type': 'application/json',
            'origin': 'https://earnalliance.mirror.xyz',
            'referer': 'https://earnalliance.mirror.xyz/',
            'sec-ch-ua': 'Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        }
        try:
            json1 = {
                'operationName': 'SubscriptionSigningMessage',
                'query': 'query SubscriptionSigningMessage($email: String, $projectAddress: String!, $walletAddress: String!, $type: SubscriptionSigningMessageEnumType) {\n  subscriptionSigningMessage(\n    email: $email\n    projectAddress: $projectAddress\n    walletAddress: $walletAddress\n    type: $type\n  )\n}\n',
                'variables': {
                    'email': mail,
                    'projectAddress': address_wallet,
                    'type': 'LINK_EMAIL',
                    'walletAddress': address_wallet
                }
            }
            res = requests.post(url=url, json=json1, headers=headers)
            jres = js.loads(res.text)
            msg = jres['data']['subscriptionSigningMessage']
            message = encode_defunct(text=msg)
            signed_message = web3.eth.account.sign_message(message, private_key=privatekey)
            signatur = Web3.toHex(signed_message.signature)

            json2 = {
                'operationName': 'LinkEmail',
                'query': "mutation LinkEmail($email: String!, $walletAddress: String!, $signedMessage: String!, $signature: String!) {\n  linkEmail(\n    email: $email\n    walletAddress: $walletAddress\n    signedMessage: $signedMessage\n    signature: $signature\n  ) {\n    ...emailVerificationDetails\n    __typename\n  }\n}\n\nfragment emailVerificationDetails on EmailVerificationType {\n  _id\n  maskedEmail\n  verificationStatus\n  __typename\n}\n",
                'variables': {
                    'email': mail,
                    'signature': signatur,
                    'signedMessage': msg,
                    'walletAddress': address_wallet
                }
            }
            requests.post(url=url, json=json2, headers=headers)
            json3 = {
                'operationName': 'SubscriptionSigningMessage',
                'query': "query SubscriptionSigningMessage($email: String, $projectAddress: String!, $walletAddress: String!, $type: SubscriptionSigningMessageEnumType) {\n  subscriptionSigningMessage(\n    email: $email\n    projectAddress: $projectAddress\n    walletAddress: $walletAddress\n    type: $type\n  )\n}\n",
                'variables': {
                    'projectAddress': '0x6f03368258FF86141956d11aCdBEA13aA4076CB5',
                    'type': 'SUBSCRIBE',
                    'walletAddress': address_wallet
                }
            }
            res = requests.post(url=url, json=json3, headers=headers)
            jres = js.loads(res.text)
            msg = jres['data']['subscriptionSigningMessage']
            message = encode_defunct(text=msg)
            signed_message = web3.eth.account.sign_message(message, private_key=privatekey)
            signatur = Web3.toHex(signed_message.signature)

            json4 = {
                'operationName': 'Subscribe',
                'query': "mutation Subscribe($projectAddress: String!, $walletAddress: String!, $signedMessage: String!, $signature: String!, $source: String) {\n  subscribe(\n    projectAddress: $projectAddress\n    walletAddress: $walletAddress\n    signedMessage: $signedMessage\n    signature: $signature\n    source: $source\n  ) {\n    ...emailVerificationDetails\n    __typename\n  }\n}\n\nfragment emailVerificationDetails on EmailVerificationType {\n  _id\n  maskedEmail\n  verificationStatus\n  __typename\n}\n",
                'variables': {
                    'projectAddress': '0x6f03368258FF86141956d11aCdBEA13aA4076CB5',
                    'signature': signatur,
                    'signedMessage': msg,
                    'sourse': 'SubscribeNav',
                    'walletAddress': address_wallet
                }
            }
            res = requests.post(url=url, json=json4, headers=headers)
            jres = js.loads(res.text)
            pprint(jres)
            time.sleep(10)
            confirm_mail(mail, pasw, 'hello@mirror.xyz')
            json5 = {
                'operationName': 'SubscriberEditionSignature',
                'query': "query SubscriberEditionSignature($projectAddress: String, $walletAddress: String, $editionAddress: String, $tokenId: Int, $dryRun: Boolean) {\n  subscriberEditionSignature(\n    projectAddress: $projectAddress\n    walletAddress: $walletAddress\n    editionAddress: $editionAddress\n    tokenId: $tokenId\n    dryRun: $dryRun\n  ) {\n    signedPayload\n    result\n    __typename\n  }\n}\n",
                'variables': {
                    'dryRun': False,
                    'editionAddress': '0xBc2Cf251Cf812Ca54BB5289001d4B09f0967D659',
                    'projectAddress': '0x6f03368258FF86141956d11aCdBEA13aA4076CB5',
                    'tokenId': 0,
                    'walletAddress': address_wallet
                }
            }
            res = requests.post(url=url, json=json5, headers=headers)
            jres = js.loads(res.text)
            pprint(jres)
            to = Web3.toChecksumAddress(address_wallet)
            royaltyRecipient = '0x0000000000000000000000000000000000000000'
            royaltyBps = 0
            primarySaleRecipient = '0x0000000000000000000000000000000000000000'
            tokenId = 0
            uri = ''
            quantity = 1
            pricePerToken = 0
            currency = '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
            validityStartTimestamp = 0
            strk = jres['data']['subscriberEditionSignature']['signedPayload']
            q = strk.find('uid')
            vid = strk[q+6:q+72]
            p = strk.find('signature')
            signaturr = strk[p+12:p+144]
            z = strk.find('mintEndTime')
            validityEndTimestamp_ = strk[z+40:z+50]
            validityEndTimestamp = Web3.toInt(hexstr=validityEndTimestamp_)
            contract = web3.eth.contract(address=contract_adr, abi=contract_abi)
            contract_txn = contract.functions.mintWithSignature((
                to, royaltyRecipient, royaltyBps, primarySaleRecipient, tokenId,
                uri, quantity, pricePerToken, currency, validityStartTimestamp,
                validityEndTimestamp, vid), signaturr).buildTransaction({
                        'gasPrice': web3.eth.gasPrice,
                        'nonce': web3.eth.getTransactionCount(address_wallet)
                 })
            signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=privatekey)
            tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'\n>>> https://polygonscan.com/tx/{web3.toHex(tx_hash)}', flush=True)
        except Exception as ex:
            print(f'\n>>> Ошибка | {ex} |')
            print(f'\n    {address_wallet}')


if __name__ == '__main__':
    print(f'\n============================================ Wiedzmin.eth =============================================')
    print(f'\nSubscribe to us : https://t.me/developercode1')
    print(f'\nПоддержи автора : 0xaC5d3F9f74c77821B624EC0830481E0608974fF7')
    with open("private_keys.txt", "r") as f:
        keys_list = [row.strip() for row in f]
    with open("mail.txt", "r") as f:
        mail_list = [row.strip() for row in f]
    for i in range(number_of_threads):
        thred = threading.Thread(target=main).start()
