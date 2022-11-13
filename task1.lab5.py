from pprint import pprint
list_dict = [{'bin': bin(val), 'dec': val, 'oct': oct(val), 'hex': hex(val)}
             for val in range(16)]
pprint(list_dict)