import pyAesCrypt
import os

# Encryp function
def encryption(file, password):
    buffer_size = 512 * 1024

# Encryp method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

# Output of files that have been encrypted
    print("[Object '" + str(os.path.splitext(file)[0]) + "' successfully encrypted!]")

# Deleting the original file(s)
    os.remove(file)

# Derictory Viewer Function
def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = input("Enter the encryption password: ")
walking_by_dirs("***directory with the files you want to encrypt***", password)