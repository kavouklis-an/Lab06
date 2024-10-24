# Anthony Kavouklis UF id 40825019
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

def decoded(password):
    decoded_password = ''
    for i in password:
        integer_num = int(i)
        integer_num -= 3
        decoded_password += str(integer_num)
    return decoded_password
if __name__ == '__main__':
    password = None
    continue_calc = True
    while continue_calc:
        menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            password = str(input('Please enter your password to encode: '))
            password = encode(password)
            print("Your password has been encoded and stored!")
            print('')
        if option == 2:
            decoded_password = decoded(password)
            print(f'The encoded password is {password}, and the original password is {decoded_password}')
            print('')
        if option == 3:
            continue_calc = False

