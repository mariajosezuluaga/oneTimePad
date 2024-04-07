# Simple implementation of the One-Time Pad encryption algorithm

import random

# Function that generates a random key of a given length.
def generate_key(length):
    key = ""
    for i in range(length):
        key += chr(random.randint(0, 255))
    return key


# Function that encrypts a message using the One-Time Pad algorithm.
def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_message += chr(ord(message[i]) ^ ord(key[i]))
    return encrypted_message


# Function that decrypts a message using the One-Time Pad algorithm.
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        decrypted_message += chr(ord(encrypted_message[i]) ^ ord(key[i]))
    # Return the decrypted message in binary format.
    return decrypted_message


# Test the One-Time Pad encryption algorithm.

# Ask the user for a message to encrypt.
message = input("Enter a message to encrypt: ")

# Generate a random key of the same length as the message.
key = generate_key(len(message))

# Encrypt the message using the key.
encrypted_message = encrypt(message, key)

# Decrypt the encrypted message using the key.
decrypted_message = decrypt(encrypted_message, key)

# Print the original message, the encrypted message, and the decrypted message.
print("Original message: " + message)
print("Key: " + key)
print("Encrypted message: " + encrypted_message)
print("Key: " + key)
print("Decrypted message: " + decrypted_message)
