blockchain = []

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    user_input = float(input('Enter the amount :'))
    return user_input

def get_user_choice():
    user_choice = input('Enter the valid Choice :')
    return user_choice

def print_block_elements():
    for block in blockchain:
        print('----- Outputting Block -----')
        print(block)
    else:
        print('-'*20)

def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break

    return is_valid

waiting_for_input = True

while True:
    print('Enter the Choice :')
    print('1: Add transaction')
    print('2: Print the block chain elements :')
    print('h: Hack the block chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_block_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 2:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid input, Please enter proper choice :')

    if not verify_chain():
        print_block_elements()
        print('Invalid Block elements')
        break
else:
    print('!! Done !!')
