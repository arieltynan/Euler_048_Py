#Ariel Tynan
#Euler Problem 048, Self powers, solved in Python
#Started 4 March 2022, completed 5 March 2022... Misleading as its a little after 12am 

#Method of converting large data values to strings for computation was not developed by me for this problem
#Even though it kind of was this whole problem
#Will be studying and applying this method in the future
#Have created something similar in C++

import math

MOD = 10**10 # last 10 digits
def powerLL(x, n): # Function derived from "mits" on GeeksforGeeks
 
    result = 1;
    while (n):
        if (n & 1):
            result = result * x % MOD
        n = int(n / 2)
        x = x * x % MOD
    return result
 
def powerStrings(sa, sb): # Function derived from "mits" on GeeksforGeeks
     
    # We convert strings to number
    a = b = 0
 
    # calculating a % MOD
    for i in range(len(sa)): #Shuffles through each digit, multipling by 10, adding next digit, taking modulus
        a = (a * 10 + (ord(sa[i]) - ord('0'))) % MOD
 
    # calculating b % (MOD - 1)
    for i in range(len(sb)): #Shuffles through each digit, multipling by 10, adding next digit, taking modulus
        b = (b * 10 + (ord(sb[i]) - ord('0'))) % (MOD - 1)
    return powerLL(a, b);

sum = 0
for i in range(1,1001): #from 1 to 1000
    sa = sb = "{}".format(i) #convert int to string
    #print(i, powerStrings(sa, sb))
    sum = int(powerStrings(sa, sb)) + sum #convert string to int and sum

print(sum % MOD) #Only want last 10 digits