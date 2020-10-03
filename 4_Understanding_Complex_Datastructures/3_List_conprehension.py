genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}

blockchain = [genesis_block]
owner = "Sachin"
open_transactions = []

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, tx_amount=1.0):
    transaction = {
        'recipient': recipient,
        'sender': sender,
        'amount': tx_amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    block_hash = ''
    block_hash = "-".join([str(last_block[key]) for key in last_block])
    # for key in last_block:
    #     value = str(last_block[key])
    #     block_hash += value
    block_hash += '\n'
    block = {
        'previous_hash': block_hash,
        'index': len(blockchain),
        'transaction': open_transactions
    }

    blockchain.append(block)

def get_transaction_value():
    recipient = input('Enter the recipient value :')
    amount = float(input('Enter the amount :'))
    return recipient, amount

def get_user_choice():
    user_choice = input('Enter your valid choice :')
    return user_choice


def print_blockchain_elements():
    for block in blockchain:
        print('------ outputting block -------')
        print(block)


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if blockchain[block_index][0] != blockchain[block_index-1]:
            is_valid = False
            return is_valid
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Enter you choice :')
    print('1: Add a new transaction value')
    print('2: Mine a block')
    print('3: Print the block chain')
    print('q: Quit the program')
    user_choice = get_user_choice()
    if user_choice == '1':
        recipient, amount = get_transaction_value()
        add_transaction(recipient, tx_amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
        open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid input, please enter proper choice')

else:
    print('!!!! Done !!!!')







