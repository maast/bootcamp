# line = 'jose:x:1000:1000:José Jiménez:/home/jose:/bin/bash'
# paths = list()
# # print(paths)
#
#
# for record in line.split(':'):
#     if record.startswith('/'):
#         paths.append(record)
#
# print(f'sciezki: {paths}')
# # ['/home/jose', '/bin/bash']




# my_dict = {'x': 1, 'y': 2}
# print(my_dict)
#
# my_dict2={v:k for k,v in my_dict.items()}
# print(my_dict2)
# # dict {1:'x', 2:'y'}





# def get_dict(number):
#     if number % 2 == 0:
#         return {'number': number, 'status': 'even'}
#     else:
#         return {'number': number, 'status': 'odd'}
#
# # output = [get_dict(x) for x in range(0, 5)]
# output = [get_dict(x) for x in (1,3,4,5)]
#
# print(output)



#
# def get_tuple(number):
#     return (number, number+10)
#
# output = [get_tuple(x) for x in range(0, 5)]
#
# print(output)


AGE_ADULT = 18

def is_adult(age):
    """
    Function checks if person is adult.
    Adult person is over 18 years old.

    >>> is_adult(18)
    True

    >>> is_adult(17.9)
    False
    """
    if age >= AGE_ADULT:
        return True
    else:
        return False