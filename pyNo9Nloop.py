# Nested Loop

from symtable import Symbol


rows = int(input('how many rows: '))
columns = int(input('how many columns: '))
symbol= input('Enter a symbol to use:')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()

    