def encrypt():
  # Ask user for the message to encrypt
  message = input("Enter the message to encrypt: ")
  
  # Ask user for the shift value
  shift = int(input("Enter the shift value: "))
  
  # Encrypt the message
  encrypted_message = ""
  for char in message:
    # Check if the character is a letter
    if char.isalpha():
      # Shift the letter by the shift value
      encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
      encrypted_message += encrypted_char
    if char.isspace():
  return encrypted_message

def decrypt():
  # Ask user for the message to decrypt
  message = input("Enter the message to decrypt: ")
  
  # Ask user for the shift value
  shift = int(input("Enter the shift value: "))
  
  # Decrypt the message
  decrypted_message = ""
  for char in message:
    # Check if the character is a letter
    if char.isalpha():
      # Shift the letter by the shift value
      decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
      decrypted_message += decrypted_char
  return decrypted_message

print(encrypt())
