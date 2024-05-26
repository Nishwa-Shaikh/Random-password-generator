import string
import secrets

class Password:

    def generate_password(self, length):
        alphabet=string.ascii_letters + string.digits + string.punctuation
        password=''.join(secrets.choice(alphabet) for i in range(length))
        return password
    
    def weak_password(self):
        while True:
            length=int(input('Enter length: '))
            if length>=6 and length<10:
                return self.generate_password(length)
            else:
                print('Length  should be greater than or equal to 6 and less than 10')

    def strong_password(self):
        while True:
            length=int(input('Enter length: '))
            if length>=10:
                return self.generate_password(length)
            else:
                print('Length should be greater than or equal to 10')


obj=Password()
print(obj.weak_password())
print(obj.strong_password())
