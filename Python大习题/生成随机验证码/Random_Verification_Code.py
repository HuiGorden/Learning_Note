# -*- coding: utf-8 -*-
# @Time    : 2018-01-09 1:39 AM
# @Author  : Jin,Hui
# @Email   : gordeninottawa@gmail.com
# @File    : Random_Verification_Code.py
import random
print("Press Any Key to generate 10 random Verification Code".center(50, "*"))
verification_code = []
for i in range(10):
    each_verification_code = []
    random_length = random.randrange(6, 11)
    for each_bit in range(random_length):
        random_type = random.randrange(1, 4)
        if random_type == 1:
            #Number
                each_verification_code.append(str(chr(random.randrange(48, 58))))
        elif random_type == 2:
            #UpperCase Letter
                each_verification_code.append(str(chr(random.randrange(65, 91))))
        else:
            #LowerCase Letter
                each_verification_code.append(str(chr(random.randrange(97, 123))))
    verification_code.append("".join(each_verification_code))


for each_code in verification_code:
    print(each_code)

