#Account Number/Weekly Task

#reference: https://thispointer.com/replace-first-n-characters-from-a-string-in-python/ 


BankNo = input("Please enter a 10 digit account number: ")

x = 6

replacement = 'XXXXXX'

BankNo = replacement + BankNo[x:]

print(BankNo)