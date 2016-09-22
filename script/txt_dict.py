"""
Convert str to dictionary
"""
def txt_dict(filename):
    with open(filename, 'r') as txt:
        print('-------------------------------start------------------------------')
        data_list = txt.read().split(';')
        data_dict = dict()
        list(map(lambda x: data_dict.setdefault(x.lstrip().rstrip('\n').split('=', 1)[0], x.lstrip().rstrip('\n').split('=')[1]), data_list))
        print('================================end===============================')
        return(data_dict)

"""
data_dict = txt_dict()
with open('Cookie_dict', 'w') as txt:
    for cookie_key, cookie_value in data_dict.items():
        txt.write('\''+cookie_key+'\''+': '+'\''+cookie_value.strip('\"')+'\''+'\n')

with open('Cookie_dict', 'r') as txt:
    data = txt.read()
    print(data)
"""
