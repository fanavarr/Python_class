#simple snipped to know if a number is prime or not

def is_prime(x):
    if x < 2:
        print "I am not a Prime Number"
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                 print "I am not a Prime Number"
                 return False
                 break
        print "I am a Prime number" 
        return True
 
is_prime(2)
