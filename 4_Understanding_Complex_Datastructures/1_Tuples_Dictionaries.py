blockchain = []
opentransactions = []
owner = 'Sachin'

def get_last_blockchain_value():

    if len(blockchain) == 0:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):

    transaction = {
        'recipient': recipient,
        'sender': sender,
        'amount': amount
    }
    opentransactions.append(transaction)

def mine():
    pass


def get_transaction_value():

    tx_recipient = input('Enter the name of recipient :')
    tx_amount = float(input('Enter the transaction amouunt :'))
    return tx_recipient, tx_amount


def get_user_choice():
    user_choice = input('Enter proper your choice:  ')
    return user_choice


def print_blockchain_elements():
    for block in blockchain:
        print('------ Blockchain -------')
        print(block)

def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        else:
            if blockchain[block_index][0] != blockchain[-1]:
                is_valid = False
                return is_valid
        block_index += 1

    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Enter your choice :')
    print('1: Add transaction')
    print('2: print blockchain')
    print('h: manipulate the chain')
    print('q: quit the program')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, tx_amount = tx_data
        add_transaction(recipient, amount=tx_amount)
        print(opentransactions)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input is invalid, Enter proper choice')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid block chain.....Exiting !!!!')
        break

else:
    print('!!!!! Done !!!!!')