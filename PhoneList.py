#Created By GnonymousGems
with open('phonenumbers.txt', 'a') as f:
 print("Welcome to PhoneList. Create the wordlist of PhoneNumbers")
 print("Example like: 98xxxxxxxxx, 97xxxxxxxxxx, 01xxxxxxxx etc")
 print("The wordlist of phone numbers will be available the directory where the program is located")
 i = int(input("Enter the first two digits you want to start from: "))
 i = i * 100000000
 while i <= (int(i) + int(99999999)):
  i = i + 1
  print(i)
  print(i, file=f)
 print("Succesfully saved into name phonenumbers.txt")
