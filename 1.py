password_list = ['password', '12 3456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567']

n = " "
passcode = ""

while n != passcode:
    n = input("What is the password? : ")
    for i in range(len(password_list)):
        m = password_list[i]
        if n == m:
            passcode = m
            print('Yes, the password is ' + passcode + '. You may enter.')
            break





