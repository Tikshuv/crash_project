from utils import unzip_with_7z

zip_file_path = 'congrats.7z'  # keep as is
dest_path = '.'  # keep as is

find_me = ''  # 2 letters are missing!
secret_password = find_me + 'bcmpda'

# WRITE YOUR CODE BELOW
# ----------------------------------------
# path = '/Users/dmitrijmarculanis/Documents/exam/congrats.7z'
# path_res = '/Users/dmitrijmarculanis/Documents/exam/unzip'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
unzip = False
for f_l in alphabet:
    for s_l in alphabet:
        find_me = f_l + s_l
        secret_password = find_me + 'bcmpda'
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            unzip = True
            break
    if unzip:
        break


