import re

e_mail = input('Pls enter your e-mail address: ')
RE_MAIL = r'(\w+)@((\w+\.)+(com))'
try:
    r = re.match(RE_MAIL, e_mail)
    keys = ['name', 'domain']
    values = [r[1], r[2]]
    result = dict(zip(keys, values))
    print(result)
except TypeError:
    print('Invalid e-mail')