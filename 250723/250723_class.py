# def func(pos1, pos2, default_arg = 'default' , *args, **kwargs):
#     print('pos1:',pos1)
#     print('pos2:',pos2)
#     print('default_arg:', default_arg)
#     print('args:', args)
#     print('kwargs:', kwargs)

# func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
# """
# pos1: 1
# pos2: 2
# default_arg: 3
# args: (4, 5, 6)
# kwargs: { 'key' : 'value1', 'key2': 'value2'}
# """

# print('hello', end = '\n')
# print('aaaa')

def my_function(x, y, z):
    print(x,y,z)

name = ['aa', 'bb']
my_function(*name)