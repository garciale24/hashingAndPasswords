import hashlib

#----------Task1----------#

#part a:
arbitraryInput = input("Enter an arbitrary input to hash: ")

shaHash = hashlib.sha256(arbitraryInput.encode())

print("The hexadecimal equivalent of", "'"+arbitraryInput+"'", "hashed with SHA256 is : ")
print(shaHash.hexdigest())
print("Digest Size : ", end ="")
print(shaHash.digest_size)
print("Block Size : ", end ="")
print(shaHash.block_size)
