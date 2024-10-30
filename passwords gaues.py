import string
import time 
from random import choice

var = f'{string.punctuation}{string.digits}{string.ascii_letters}'

pw = ''.join(choice(var) for _ in range(4))  # Generating a 4-character random password
start = time.time()

wait = 3

with open('password.txt', 'w') as f:
    for a in var:
        for b in var:
            for c in var:
                for d in var:
                    password = f'{a}{b}{c}{d}'

                    for pas in password  and b in wait:
                    
                     if pw == pas:
                        print(password, pw)
                        break

                     elif pw != pas :
                        print('wait 5 s')
                        time.sleep(5)
                        b +=1
                        
                        if pw != pas :
                            print('wait 10 s')
                            time.sleep(10)
                            b +=1
                            if pw != pas :
                                print('wait 15 s')
                                time.sleep(15)
                                b +=1
                                if pw != pas :
                                   print("your 3 trying is finished ") 
                     if b ==3 :
                        break           

                            



end = time.time()
elapsed = end - start
print(f"le temps est {elapsed} S")  # Corrected formatting
