"""
Convert str to dictionary
"""

from log import Logger


def header_dict(filename):
    with open(filename, 'r') as txt:
        log = Logger(__name__)
        log.info('start')
        data_list = txt.read().split('\n')[:-2]
        data_dict = dict()
        list(map(lambda x: data_dict.setdefault(x.split(':', 1)[0], x.split(':')[1].strip()), data_list))
        log.info('end')
        return(data_dict)

"""
data_dict = header_dict()
print(data_dict)

with open('Header_dict', 'w') as txt:
    for header_key, header_value in data_dict.items():
        txt.write('\''+header_key+'\''+': '+'\''+header_value.strip('\"')+'\''+'\n')

with open('Header_dict', 'r') as txt:
    data = txt.read()
    print(data)
"""
