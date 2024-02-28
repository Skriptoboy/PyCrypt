import pyAesCrypt
import os

# Decryp function
def decryption(file, password):
    buffer_size = 512 * 1024

# Decryp method
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    print("[Object '" + str(os.path.splitext(file)[0]) + "' successfully decrypted!]")

    os.remove(file)

# Derictory scan function
def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

# If we find it, decrypt it
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = input("Enter password: ")
walking_by_dirs("***your directory***", password)