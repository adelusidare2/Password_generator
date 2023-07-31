import secrets
import string
letter = string.ascii_letters 
digits = string.digits
special_chars = string.punctuation
alphabet = letter + digits + special_chars
pwd_length = 16
pwd = ""
for i in range (pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
            
        print(pwd)
        
        