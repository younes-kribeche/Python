import string
def alphabet():
    return list(string.ascii_lowercase)
print(alphabet())
                # ou
import string
alphabet = string.ascii_lowercase
list_alphabet = list(alphabet)
print(list_alphabet)