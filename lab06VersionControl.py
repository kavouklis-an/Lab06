def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()

def encode(password):
    encoded_password = ''
    for i in password:
        integer_num = int(i)
        integer_num += 3
        encoded_password += str(integer_num)
    return encoded_password
if __name__ == '__main__':
    password = None
    continue_calc = True
    while continue_calc:
        menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            password = str(input('Please enter your password to encode: '))
            print("Your password has been encoded and stored!")
            password = encode(password)
            print(password)
        if option == 2:
            pass
        if option == 3:
            continue_calc = False

