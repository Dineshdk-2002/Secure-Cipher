# SecureCipher: Simple Caesar Cipher Encryption and Decryption Tool
# Import the string module to access the alphabet
import string
alphabets = list(string.ascii_lowercase)
def encrypt(plain_text,shift_key):
  cipher_text = ""   
  for char in plain_text :
    if char in alphabets:
      position = alphabets.index(char)
      new_position = (position + shift_key) % 26
      cipher_text += alphabets[new_position]
    else :
      cipher_text += char
  print(f"Encryption text : {cipher_text}")

def Decrypt(cipher_text,shift_key):
  plain_text = ""
  for char in cipher_text :
    if char in alphabets:
      position = alphabets.index(char)
      new_position = (position - shift_key) % 26
      plain_text += alphabets[new_position]
    else :
      plain_text += char
  print(f"Decryption text : {plain_text}")

end = False
while  not end:
  what_to_do = input("Type 'Encrypt' for Encryption or Type 'Decrypt' for Decryption : ")
  what_to_do = what_to_do.capitalize() 
  text = input("Type the message : ")
  shift = int(input("Enter the shift key : "))
  if what_to_do == "Encrypt":
    encrypt(plain_text = text,shift_key = shift)
  elif what_to_do == "Decrypt":
    Decrypt(cipher_text = text,shift_key = shift)
  next_try = input("Type yes to continue or q to quit : ")
  next_try = next_try.capitalize()
  if next_try == "Q":
    end = True
    print("Thank you, see you later")
