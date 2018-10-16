# Import from bitcoin
from bitcoin import *

#Create Private Key
my_private_key = random_key()
print("private key: %s\n" % my_private_key)

#Create Public Key
my_public_key = privtopub(my_private_key)
print(my_public_key)

#Create Wallet Address
my_address = pubtoaddr(my_public_key)
print(my_address)