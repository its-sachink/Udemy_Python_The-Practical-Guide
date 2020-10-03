blockchain = []

def get_last_blockchain_value():
    if len(blockchain) == 0:
        return None
    return blockchain[-1]

def add_transaction_value(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    user_input = float(input('Enter the transaction value :'))
    return user_input

def get_user_choice():
    user_input = input('Enter your choice :')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('------- Outputting block ----------')
        print(block)

def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0 :
            block_index += 1
            continue
        if block[0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            return is_valid
        block_index += 1
    return is_valid

while True:
    print('Enter your choice')
    print('1: Add a new transaction value')
    print('2: print block chain')
    print('h: Manilpulate the blockchain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice =='q':
        break
    else:
        print('Enter valid input :')

    if not verify_chain():
        print('Invalid block chain value')
        break

print('!! Done')
