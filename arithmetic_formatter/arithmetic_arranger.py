from pickle import FALSE

def operators_index(operation_string):
    index_operation = 0
    try:
        index_operation = operation_string.index('+')
    except:
        index_operation = operation_string.index('-')
    return index_operation


def manydigits(operation_string):
    index_operation = 0
    try:
        index_operation = operation_string.index('+')
    except:
        index_operation = operation_string.index('-')

    number_1_digits = len(operation_string[:index_operation-1])
    number_2_digits = len(operation_string[index_operation+2:])
    if number_1_digits > 4 or number_2_digits > 4:
       raise NameError('Error: Numbers cannot be more than four digits.')


def valid_operators(operation_string):
    if '+' not in operation_string or '-' not in operation_string:
        raise NameError(f'Error: Operator must be \'+\' or \'-\'.')


def valid_characters(operation_string):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    characters = [' ','+', '-']
    valid_characters = digits + characters

    for character in operation_string:
        if character not in valid_characters:
            raise NameError('Error: Numbers must only contain digits.')


def arithmetic_arranger(operations_list,responses=FALSE):
    
    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''
    
    if len(operations_list) > 5:
        raise NameError('Too many problems.')

    for operation in operations_list:
        
        valid_operators(operation)
        
        valid_characters(operation)
        
        manydigits(operation)

