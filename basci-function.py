def hello():
    print('Hello my friend')

def sawadee():
    print('sawadee')

def nihao():
    print('nihao')

def konichiwa():
    print('konichiwa')

    
def Thai():
    print('Thai')


while True:
    friend = input('Where are you from: ')

    if friend =='thai':
        sawadee()
    elif friend =='china':
        nihao()
    elif friend =='japan':
        konichiwa()
    else:
        hello()
