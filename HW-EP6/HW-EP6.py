class BE_Lab_Shop:
    # Attribute
    shopName = 'Ball Electronics Lab'

    # Constructor
    def __init__(self, subject = 'PyBoard'):
        print('Ball Electronics Lab Shop is Open !!!')
        self.subject = subject

    # Method
    def hello(self):
        print('Welcome to Ball Electronics Lab Shop')

    def sell(self):
        print(f'this is our product: {self.subject}')


class onlineShop(BE_Lab_Shop):
    def __init__(self, fullname, level, price, subject):
        super().__init__(subject)
        self.fullname   = fullname
        self.level      = level
        self.price      = price

    def checkPrice(self):
        if self.price >=5000:
            print(f'{self.subject} : Very Expensive')
        elif self.price >=3000:
            print(f'{self.subject} : Expensive')
        elif self.price >=1000:
            print(f'{self.subject} : Medium')
        elif self.price >=300:
            print(f'{self.subject} : Low')
        else:
            print(f'{self.subject} : Very Low')
 

print('------------------------------------------')

shop01 = onlineShop('Dang Lab', 5 , 1250, 'ESP32')
print(f'Shop Name: {shop01.shopName}')
print(f'Seller Name: {shop01.fullname}')
print(f'Level: {shop01.level}')
print(f'Price: {shop01.price}')
shop01.checkPrice()

print('------------------------------------------')
shop02 = onlineShop('Som Lab', 6 , 5000, 'Raspbery Pi 4')
print(f'School Name: {shop02.shopName}')
print(f'Seller Name: {shop02.fullname}')
print(f'Level: {shop02.level}')
print(f'Price: {shop02.price}')
shop02.checkPrice()
print('------------------------------------------')
shop03 = onlineShop('Fah Lab', 3 , 150, 'Arduino Uno')
print(f'School Name: {shop03.shopName}')
print(f'Seller Name: {shop03.fullname}')
print(f'Level: {shop03.level}')
print(f'Price: {shop03.price}')
shop03.checkPrice()