blockchain = []

def get_last_block_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    user_input = float(input('Enter the amount :'))
    return user_input

def get_user_input():
    user_input = input('Enter your Choice :')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)

tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print("Enter the choice: ")
    print('1: Add a transaction value')
    print('2: Print the transaction value')
    print('q: Quit')
    user_input = get_user_input()
    if user_input == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_block_value())
    elif user_input == '2':
        print_blockchain_elements()
    elif user_input == 'q':
        break
    else:
        print('Enter a proper choice')
    print('Choice registered')

print('!Done')



