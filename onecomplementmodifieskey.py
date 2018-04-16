import binascii
from binascii import hexlify
#input is extra key of 8 characters 
text = input('Enter 8 characters string : ')
#convert extra key to hexadecimal 
key = binascii.hexlify(text)
print ("Hex of key",key, len(key))
#Main key of 16 charachters
key_input =input('enter 16 charachter key')
#converting main key into hexadecimal number
key_16_main = binascii.hexlify(key_input)
print ("Main key :",key_16_main,len(key_16_main))
#divide main key into two parts and stored in the list
main_key = [key_16_main[i:i+16] for i in range(0, len(key_16_main), 16)]
print (main_key)
#take left part of the main key from the list[0] 
print (main_key[0],len(main_key[0]))
#modify left part of the main key with by ex-oring with extra key
modified_keypartleft = hex(int(key,16) ^int(main_key[0],16))[2:]
print("Modified left part of key",modified_keypartleft,len(modified_keypartleft))
