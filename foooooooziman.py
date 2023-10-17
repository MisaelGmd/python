def lista(string):
    result = []
    for char in string:
        if char.lower() == 'o':
            result.append('0')
        elif char.lower() == 'i':
            result.append('1')
        elif char.lower() == 's':
            result.append('$')
        elif char.lower() == 'a':
            result.append('@')
        else:
            result.append(char.upper())
    return result

input_string = "fooziman"
output_list = lista(input_string)
print(output_list)
