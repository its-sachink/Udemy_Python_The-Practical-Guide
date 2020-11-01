import functools
#import hashlib as hl
import json
from collections import OrderedDict
from hash_utils import hash_string_256, get_hash_of_block

"""
Add a new transaction value:
    tx_data = get_transaction_value()
        --> if add_transaction(recipient,tx_amount=amount):
            --> if verify_transaction(transaction):
                --> sender_balance = get_balance(transaction['sender'])
                    return sender_balance > transaction['amount']
                    --> return amount_recieved - amount_send

Mine a block:
    --> hash_of_block = get_hash_of_block(last_block)
        --> Get a reward
            --> commit the reward and hash_of_block

So basically while adding itself we are verifying, checking balance and then adding to the open_transaction chain
While mining we are just committing the open_transaction to the global block_chain list
"""

MINIG_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
}

# Initialize the genesis block first
blockchain = [genesis_block]
open_transactions = []
owner = 'Sachin'
participants = {owner}


def save_data():
    '''
    Using json.dumps we are converting the Python List to JSON format and then writing it to the file.
    We will save the data when we
        1: Mining a block
        2: Whenever we are adding a new transaction
    '''
    with open('blockchain.txt',mode='w') as f:
        f.write(json.dumps(blockchain))
        f.write('\n')
        f.write(json.dumps(open_transactions))


def get_transaction_value():
    tx_recipient = input('Enter the name of a Recipient :')
    tx_amount = float(input('Enter the value of transaction :'))
    return tx_recipient, tx_amount

# def get_hash_of_block(block):
#     # return '-'.join([str(block[key]) for key in block])
#     '''
#     json.dumps will convert the python dictionary to the string type
#     encode to encode to utf8 binary format
#     hexdigest to convert the binary encode to human readable hexadecimal format
#     :param block:
#     :return:
#     '''
#     return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

def is_valid_proof(transactions, last_block_hash, proof):
    guess = (str(transactions) + str(last_block_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2]=='00'

def proof_of_work():
    last_block = blockchain[-1]
    last_hash = get_hash_of_block(last_block)
    proof = 0
    while not is_valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof



'''
illustration purpose tx_sender
list_of_list = [ [1,2,3,4], [6,7,8,9] [10,11,12,13] [14,15,16,17]]
nums = [ [num for num in items if num%2 == 0]for items in list_of_list ]
nums
[[2, 4], [6, 8], [10, 12], [14, 16]]
Demo for below function relate to tx[0]
'''
def get_balance(participant):
    """ We are also considering the open non-committed transactions here while calculating the sender balance
    """
    tx_commited_by_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in
                             blockchain]
    open_tx_by_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    total_send_amount = tx_commited_by_sender
    total_send_amount.append(open_tx_by_sender)

    '''
    Using functools here, with following syntax.
    >>> from functools import reduce
    >>> numbers = [1, 2, 3, 4]
    >>> reduce(lambda a, b: a + b, numbers)
    10

    Also we are using a ternary operator.
    Use tx_sum + tx_amt[0] if if len(tx_amt) > 0 else use Zero(0)
        tx_sum + tx_amt[0] if len(tx_amt) > 0 else 0
    '''
    amount_send = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
                                   total_send_amount, 0)
    # total_send_amount = 0
    # for tx in total_send_amount:
    #     if len(tx) > 0:
    #         amount_send += tx[0]

    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in
                    blockchain]
    amount_recieved = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
                                       tx_recipient, 0)

    # amount_recieved = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_recieved += tx[0]
    return amount_recieved - amount_send


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(tx_recipient, tx_sender=owner, tx_amount=1.0):
    # transaction = {
    #     'sender': tx_sender,
    #     'recipient': tx_recipient,
    #     'amount': tx_amount
    # }
    transaction = OrderedDict([('sender', tx_sender), ('recipient', tx_recipient), ('amount', amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(tx_recipient)
        participants.add(tx_sender)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hash_of_block = get_hash_of_block(last_block)
    proof = proof_of_work()
    # we are excluding the reward_transaction from proof_of_work()
    # reward_transaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINIG_REWARD
    # }
    reward_transaction = OrderedDict([('sender', 'MINING'),('recipient', owner),('amount', MINIG_REWARD)])
    # Copying open transaction just in case the open transaction fails, we should not loose open transactions chain
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hash_of_block,
        'index': len(blockchain),
        'transactions': copied_transactions,
        'proof': proof
    }
    blockchain.append(block)
    save_data()
    return True


def print_blockchain():
    for block in blockchain:
        print('Outputting the Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    print(blockchain)
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        print(block)
        if block['previous_hash'] != get_hash_of_block(blockchain[index - 1]):
            return False
        if not is_valid_proof(block['transactions'][:-1],block['previous_hash'],block['proof']):
            print('proof of work is invalid')
            return False
    return True


def get_user_choice():
    user_choice = input('Enter from the valid choice :')
    return user_choice


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


"""
Add a new transaction value:
    tx_data = get_transaction_value()
        --> if add_transaction(recipient,tx_amount=amount):
            --> if verify_transaction(transaction):
                --> sender_balance = get_balance(transaction['sender'])
                    return sender_balance > transaction['amount']
                    --> return amount_recieved - amount_send

Mine a block:
    --> hash_of_block = get_hash_of_block(last_block)
        --> Get a reward
            --> commit the reward and hash_of_block

So basically while adding itself we are verifying, checking balance and then adding to the open_transaction chain
While mining we are just committing the open_transaction to the global block_chain list
"""

waiting_for_input = True
while waiting_for_input:
    print('Enter the valid input :')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the block chain')
    print('4: Output the participants')
    print('5: Check transaction validity before finally mining the block transaction')
    print('h: Manipulate the block')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, tx_amount=amount):
            print('Transaction successfully Added !!')
        else:
            print('Transaction failed !!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transaction': [{'sender': 'Vilas', 'recipient': 'Sachin', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    if not verify_chain():
        print_blockchain()
        print('Invalid block chain elements !!')
        break
    print('Balance of {} is : {:6.2f}'.format(owner, get_balance(owner)))
else:
    print('-------------- !! Done !! -----------------')

'''
Adding a format function to the print function
'''
