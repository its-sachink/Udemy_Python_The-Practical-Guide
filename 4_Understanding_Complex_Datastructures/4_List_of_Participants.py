genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transaction': []
}

blockchain = [genesis_block]
owner = "Sachin"
open_transactions = []
participants = {owner}

def get_hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(recipient, sender=owner, tx_amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': tx_amount
    }
    open_transactions.append(transaction)
    participants.add(recipient)
    participants.add(sender)

def mine_block():
    last_block = blockchain[-1]
    hash_block = get_hash_block(last_block)
    global open_transactions
    block = {
        'previous_hash': hash_block,
        'index': len(blockchain),
        'transaction': open_transactions
    }
    blockchain.append(block)
    open_transactions = []

def get_transaction_value():
    recipient = str(input('Enter the name of Recipient :'))
    tx_amount = float(input('Enter the amount for transaction :'))
    return recipient, tx_amount

def print_blockchain_elements():
    for block in blockchain:
        print('-----Outputting Block -----')
        print(block)
    else:
        print('-'*20)

def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != get_hash_block(blockchain[index-1]):
            return False
    return True

def get_user_choice():
    user_choice = input('Enter the valid Choice :')
    return user_choice

waiting_for_input = True

while waiting_for_input:
    print('Please choose :')
    print('1: Add transaction')
    print('2: Mine a new block')
    print('3: Output the blockchain')
    print('4: Output the participants')
    print('h: Hack the block chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, tx_amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input is invalid, Please pick a value from List')
    if not verify_chain():
        print_blockchain_elements()
        print('Blockchain is Invalid')
        break
else:
    print('--------------- Done ----------------')


