from pickle import FALSE, TRUE

def fill_lines(operation_string,lines,responses,count,limit):
    index = operator_index(operation_string)
        
    number_1 , number_2 = get_numbers(operation_string,index)
    number_1, number_2 = int(number_1), int(number_2)
    number_1_digits, number_2_digits = get_characters_numbers(operation_string)

    if responses == True:
        if number_1_digits == number_2_digits:
            if count == limit:
                lines[1] += operation_string[index] + ' ' + str(number_2)
                lines[0] += '  ' + str(number_1)
                lines[2] += '-' * 2 + '-'*number_1_digits
                if operation_string[index] == '+':
                    result = number_1 + number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_2_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result)
                else:
                    result = number_1 - number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_2_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result)
            else:
                lines[1] += operation_string[index] + ' ' + str(number_2) + '    '
                lines[0] += '  ' + str(number_1) + '    '
                lines[2] += '-' * 2 + '-'*number_1_digits + '    '
                if operation_string[index] == '+':
                    result = number_1 + number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_2_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result) + '    '
                else:
                    result = number_1 - number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_2_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result) + '    '

        elif number_1_digits > number_2_digits:
            if count == limit:
                lines[0] += '  ' + str(number_1)
                number_white_spaces = number_1_digits - number_2_digits
                lines[1] += operation_string[index] + ' ' + ' '*number_white_spaces + str(number_2)
                lines[2] += '-' * 2 + '-'*number_1_digits
                if operation_string[index] == '+':
                    result = number_1 + number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_1_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result)
                else:
                    result = number_1 - number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_1_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result)
            else:
                lines[0] += '  ' + str(number_1) + '    '
                number_white_spaces = number_1_digits - number_2_digits
                lines[1] += operation_string[index] + ' ' + ' '*number_white_spaces + str(number_2) + '    '
                lines[2] += '-' * 2 + '-'*number_1_digits + '    '
                if operation_string[index] == '+':
                    result = number_1 + number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_1_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result) + '    '
                else:
                    result = number_1 - number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_1_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result) + '    '

        else:
            if count == limit:
                lines[1] += operation_string[index] + ' ' + str(number_2)
                number_white_spaces = number_2_digits - number_1_digits
                lines[0] += '  ' + ' '*number_white_spaces + str(number_1)
                lines[2] += '-' * 2 + '-'*number_2_digits
                if operation_string[index] == '+':
                    result = number_1 + number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_2_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result)
                else:
                    result = number_1 - number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_2_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result)
            else:
                lines[1] += operation_string[index] + ' ' + str(number_2) + '    '
                number_white_spaces = number_2_digits - number_1_digits
                lines[0] += '  ' + ' '*number_white_spaces + str(number_1) + '    '
                lines[2] += '-' * 2 + '-'*number_2_digits + '    '
                if operation_string[index] == '+':
                    result = number_1 + number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_2_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result) + '    '
                else:
                    result = number_1 - number_2
                    length_result = len(str(result))
                    number_white_spaces = 2 + number_2_digits - length_result
                    lines[3] += ' '*number_white_spaces + str(result) + '    '

    else:
        if number_1_digits == number_2_digits:
            if count == limit:
                lines[1] += operation_string[index] + ' ' + str(number_2)
                lines[0] += '  ' + str(number_1)
                lines[2] += '-' * 2 + '-'*number_1_digits
            else:
                lines[1] += operation_string[index] + ' ' + str(number_2) + '    '
                lines[0] += '  ' + str(number_1) + '    '
                lines[2] += '-' * 2 + '-'*number_1_digits + '    '

        elif number_1_digits > number_2_digits:
            if count == limit:
                lines[0] += '  ' + str(number_1)
                number_white_spaces = number_1_digits - number_2_digits
                lines[1] += operation_string[index] + ' ' + ' '*number_white_spaces + str(number_2)
                lines[2] += '-' * 2 + '-'*number_1_digits
            else:
                lines[0] += '  ' + str(number_1) + '    '
                number_white_spaces = number_1_digits - number_2_digits
                lines[1] += operation_string[index] + ' ' + ' '*number_white_spaces + str(number_2) + '    '
                lines[2] += '-' * 2 + '-'*number_1_digits + '    '

        else:
            if count == limit:
                lines[1] += operation_string[index] + ' ' + str(number_2)
                number_white_spaces = number_2_digits - number_1_digits
                lines[0] += '  ' + ' '*number_white_spaces + str(number_1)
                lines[2] += '-' * 2 + '-'*number_2_digits
            else:
                lines[1] += operation_string[index] + ' ' + str(number_2) + '    '
                number_white_spaces = number_2_digits - number_1_digits
                lines[0] += '  ' + ' '*number_white_spaces + str(number_1) + '    '
                lines[2] += '-' * 2 + '-'*number_2_digits + '    '


def get_characters_numbers(operation_string):
    index = operator_index(operation_string)

    number_1, number_2 = get_numbers(operation_string,index)

    number_1_digits = len(str(number_1))
    number_2_digits = len(str(number_2))

    return (number_1_digits,number_2_digits)

def get_numbers(operation_string,operator_index):
    number_1 = operation_string[:operator_index-1]
    number_2 = operation_string[operator_index+2:]
    return (number_1, number_2)


def operator_index(operation_string):
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
    if '+' not in operation_string:
        if '-' not in operation_string:
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
    lines = [line_1,line_2,line_3,line_4]

    if len(operations_list) > 5:
        raise NameError('Too many problems.')
    count = 0
    for operation in operations_list:
        count += 1
        valid_operators(operation)
        
        valid_characters(operation)
        
        manydigits(operation)
        
        fill_lines(operation,lines,responses,count,len(operations_list))

    output_string = ''
    output_string += lines[0] + '\n'
    output_string += lines[1] + '\n'
    output_string += lines[2] + '\n'
    if responses == True:
        output_string += lines[3] + '\n'
    
    return output_string

