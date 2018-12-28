import dateparser as dp
import sys

DUE = 'due'
ANY = 'any'
ONLY = 'only'
LIST = 'list'

arguments = sys.argv[1:]

print(arguments)

if DUE in arguments:
    due_index = arguments.index(DUE)
    due_date  = ' '.join(arguments[due_index + 1:])
    arguments = arguments[:due_index]

print(due_date)
print(dp.parse(due_date))
print(f'arguments after removal {arguments}')
