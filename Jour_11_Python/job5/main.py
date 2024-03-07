import string
def alphabet():
    return list(string.ascii_lowercase)
reversed_alphabet=reversed(alphabet())
print(list(reversed_alphabet))
                # ou
import string
alphabet = string.ascii_lowercase
reversed_alphabet = alphabet[::-1]
list_reversed_alphabet = list(reversed_alphabet)
print(list_reversed_alphabet)