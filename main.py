import requests
import hashlib
import string
import math
import getpass

def separator(func):
    def wrap_func(*args, **kwargs):
        print('#'*50)
        func(*args, **kwargs)
        print('#'*50)
    return wrap_func
   
def calc_entropy(password):
    if not password:
        print('Empty password')
        return None
    
    amount = 0
    char_types = []
    char_count = [0,0,0,0,len(password)]
    for char in password:
        if char.isupper():
            char_count[0] += 1
            char_types.append(('upper',len(string.ascii_uppercase)))
        elif char.islower():
            char_count[1] += 1
            char_types.append(('lower',len(string.ascii_lowercase)))
        elif char.isdigit():
            char_count[2] += 1
            char_types.append(('digit',len(string.digits)))
        elif char in string.punctuation:                   #Valid chars: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
            char_count[3] += 1                             
            char_types.append(('punctuation',len(string.punctuation)))
        else:
            return None
    
    check_strength(char_count)
    
    char_types = set(char_types)
    amount = sum(i for _, i in char_types)

    print('Checking entropy value... ')
    entropy = amount ** len(password)
    bits_value = math.log2(entropy)
    time_to_crack = entropy / (10 ** 11)       #entropy / tries per second
    time_value = convert_seconds(time_to_crack)

    print(f'Entropy value: {int(bits_value)} bits.')
    print(f'Estimated time to crack password: {time_value}.')
    
    return True

def check_strength(char_count):
    print('Checking strengh... ')
    if char_count[4] < 6:
        print('Password too short. It must be at least 6 characters long!')
    else:
        if char_count[4] >= 10:
            print(f'Strong password with {char_count[4]} characters.')
        else:
            print(f'Medium password with {char_count[4]} characters.')
        
    #Sugestions to make stronger
    if not char_count[0]:
        print('Tip: Add at least one lowercase character!')
    if not char_count[1]:
        print('Tip: Add at least one uppercase character!')
    if not char_count[2]:
        print('Tip: Add at least one digit!')
    if not char_count[3]:
        print('Tip: Add at least one special character!')

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        print(f'Error fetching: {res.status_code}, check the API and try again!')
        return None
    
    return res

def pwned_api_check(password):
    print('Checking if this password has been found in data breaches...')

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    if response:
        return get_password_leaks_count(response, tail)
    
    return 'empty'
    

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count  
    return 0

def convert_seconds(seconds):
    time_units = [
        ("century", 60 * 60 * 24 * 365 * 100),
        ("decade", 60 * 60 * 24 * 365 * 10),          
        ("year", 60 * 60 * 24 * 365),               
        ("month", 60 * 60 * 24 * 30),                 
        ("day", 60 * 60 * 24),                       
        ("hour", 60 * 60),                            
        ("minute", 60),                               
        ("second", 1),                                
        ("millisecond", 1 / 1000),
        ("microsecond", 1 / 1000000)                 
    ]
    
    for unit_name, unit_factor in time_units:
        if seconds >= unit_factor:
            unit_value = seconds // unit_factor
            new_unit_name = unit_name
            
            if unit_value > 1:
                if unit_name == 'century':
                    new_unit_name = unit_name.replace('y', 'ies')
                else:
                    new_unit_name = f'{unit_name}s'
            
            return f'{unit_value} {new_unit_name}'
    
    return f'less than 1 microsecond'

@separator
def main():
    password = getpass.getpass('Type the password:')
    ret = calc_entropy(password)
    
    if not ret:
        print('Password contains a invalid character.')
    else:
        
        count = pwned_api_check(password)
        
        if count == 'empty':
            print("Unable to verify if the password has been exposed in a data breach.")
            return None
        
        if count:
            print(f'This password was found {count} times in data breaches')
        else:
            print('This password was NOT found in data breaches')


if __name__ == '__main__':
    while True:
        exit = ''
        main()
        while exit not in ['y','n','Y','N']:
            exit = input("Do you want to continue? (y/n): ")
        
        if exit in ['n','N']:
            print('Ending program...')
            break



