#importing libraries to generate string and randomness
import string
import random


print("""
*********************************************************************
Welcome to Alexander's Random Password Generator. \n
*********************************************************************
\nPasswords should always be Long, Random and
Include Letters, Numbers and Symbols to be as secure as possible!""")

#Prompt the user for what application, software or website the password is for.
print("For what website, application or software do you need this password for?")
application = input("\n>>>")

#define rules from the string library I imported
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combine rules into one
all = lower + upper + num + symbols

#make them random
temp = random.sample(all,16)

#create the password
password = "".join(temp)

#create a progess bar just for the Lolz
from alive_progress import alive_bar
import time

for x in range(30):
    with alive_bar(x, bar='smooth') as bar:
        for i in range(x):
            time.sleep(.001)
            bar()


#print the pasword
print("\nYour Generated password for " , application , " is >> " , password, "\n \nPlease keep this password Secret!")
print("\nYour Generated password is ", password)
