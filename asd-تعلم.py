import time
import webbrowser
import sys
import random

# كل البرمجة من الـ Wael-14
er = '1234567890abqikvcryzpexnmosdfghjkluABTRQWEZXSDFGHJKMNVCUIYT'
TY = '1234567890'  # يمكنك تغيير هذا اذا اردة الى احرف او ارقام او كلاهما \ هذا لمولد كلمات المرور
print('''                    |---------|
                     |Wael-14|
                    |_________|''')
print('============================================================')

def wail():
    import time
    print('1-open my website 3-password generator 2-accounts generator   ')

    w = input('>')
    if w == '1':
        time.sleep(2)
    if w == '1':
        webbrowser.open('https://scratch.mit.edu/users/Wael14/')
        wail14()
    elif w == '2':
        print('Enter the number of accounts?')
        i = input()
        i = int(i)
        print('Enter the length of the account without the range?')
        l = input()
        l = int(l)
        print('Enter domain? ')
        o = input(1351                                                                                                                                                                                    )
        print('Enter letters or numbers?')
        p = input()
        print('========================')
        for mmm in range(i):
            mmm = ''

            for item in range(l):
                mmm = ''
            for item in range(l):
                mmm += random.choice(er)

            print(p + mmm + o)
            with open('mmm.txt', 'a') as u:
                u.write(p + mmm + o + '\n')
        wail14()
    elif w == '3':
        print('Enter the number of passwords?')
        b = input()
        b = int(b)
        print('Enter the length of the passwords?')
        s = input()
        s = int(s)
        print('========================')

        for mmm in range(b):
            mmm = ''

            for item in range(s):
                mmm = ''
            for item in range(s):
                mmm += random.choice(TY)

            print(mmm)
            with open('mmm.txt', 'a') as u:
                u.write(mmm + '\n')

        wail14()


def wail14():
    print('========================')
    print("Thanks for using the tool")
    time.sleep(5)
    webbrowser.open('mmm.txt')
    sys.exit()



wail()
