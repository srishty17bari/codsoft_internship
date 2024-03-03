import random
print("THIS IS A SIMPLE PASSWORD GENERATOR")
n=int(input("Enter the length of the password(more than 8)\n"))
if(n<8):
    print("Enter a value greater than 8!")
    exit
else:
    digits=['0','1','2','3','4','5','6','7','8','9']
    lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    special=['!','@','#','$','%','^','&','*','<','>','/','?']
    pass_s = digits + lowercase + uppercase + special
    rand_d=random.choice(digits)
    rand_l=random.choice(lowercase)
    rand_u=random.choice(uppercase)
    rand_s=random.choice(special)
    pass_word=rand_d+rand_l+rand_u+rand_s
    for x in range(0,n-4):
        pass_word=pass_word+random.choice(pass_s)
    print("The password generated is:\n",pass_word)


