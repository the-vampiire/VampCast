""" Vigenere Cypher with notes and comments """

def alphabet_position(letter):
    """ 
    accepts a string-character and returns the 0 based position of that character in the alphabet
    assumes that ONLY alphabetic letters are passed into the function (must control this OUTSIDE this function) 
    """

    """
    use the ord() method to determine the unicode integer value representing that character

    lowercase letters begin at the unicode value 97 ("a") and end at value 122 ("z")
        in order to return the 0-based index of the letter within the alphabet we have to start "a" at 0
            we can do this by subtracting 97 from its lowercase unicode value

    uppercase letters begin at unicode value 65 ("A") and end at value 90 ("Z")
        in order to return the 0-based index of the letter within the alphabet we have to start "A" at 0
            we can do this by subtracting 65 from its uppercase unicode value
    """

    unicode_value = ord(letter) # store the unicode value of the given letter
    if unicode_value >= 97: # all lowercase letters will be between 97 and 122, inclusive
        return unicode_value - 97 # subtract 97 to return the 0-based alphabetic position of the lowercase letter
    else: # if the unicode_value is below 97 it must be an uppercase letter
        return unicode_value - 65 # subtract 65 to return the 0-based alphabetic position of the uppercase letter

def rotate_character(character, rotation):
    """ 
    accepts a character and a rotation amount. 
    returns the rotated letter if the character is a letter
    if it is not a letter then return the character without any rotation

    calls the alphabet_position() function to get the base alphabetic position from which the letter will be rotated
    """
    from string import ascii_lowercase # import the ascii_lowercase ("abcdefghijklmnopqrstuvwxyz") set from the "string" module

    # first check if the character is alphabetic by using the isalpha() string method
    if character.isalpha(): # if the character IS alphabetic then proceed to the rest of the function block
        # get the initial 0-based alphabetic position of the character using the alphabet_position() function
        initial_position = alphabet_position(character) 
        # determine the new position by adding the rotation amount
        rotated_position = initial_position + rotation
        rotated_position = rotated_position % 26 # use the % operator with the length of the alphabet (26) to "wrap around" as needed
        # use the ascii lowercase string to get the new letter (after rotation) using string indexing "[index]"" syntax
        rotated_letter = ascii_lowercase[rotated_position]
        # modify the rotated letter if the original letter was uppercase
        if character.isupper(): # use the string method isupper() to determine if the original character was uppercase
            rotated_letter = rotated_letter.upper() # use the string method upper() to make the rotated letter capital
        return rotated_letter

    else:  # if the character IS NOT alphabetic then return the character as is (without rotation)
        return character

def encrypt(text, rotation_key):
    rotation_key_index = 0 # use a resettable index to wrap back over the rotation_key as needed
    output_string = "" # empty string to be concatenated by the encryption logic
    for character in text: # loop over each character in the text
        if character.isalpha(): # if the character is alphabetic follow the rotation logic
        # reset the rotation_key_index if it goes out of bounds 
            rotation_key_index = 0 if rotation_key_index == len(rotation_key) else rotation_key_index
        # determine the rotation amount using the current letter in the rotation key
            rotation = alphabet_position(rotation_key[rotation_key_index])
            rotation_key_index += 1 # increment the rotation_key_index every time it is used (above)
            output_string += rotate_character(character, rotation) # concatenate the rotated character from the text
        else: # if the character is not alphabetic concatenate it as is (whitespace, punctuation etc)
            output_string += character
    return output_string

# def quit_handler():
#     """ prompts the user to quit or continue """
#     quit_choice = input("\nTo quit type 'q' or 'quit' otherwise hit any key to continue\n>>> ")
#     if quit_choice in ("q", "quit"):
#         print("Exiting the program")
#         quit()

# def main():
#     """
#     Executed if the Vigenere Cypher is called as a standalone program (not as an import)
#     """

#     welcome_message = """     
#     ********************************************************************************
#     ********************************************************************************
#     ***                                                                          ***
#     ***                                                                          ***
#     ***                             ---------------                              ***
#     ***                             VIGENERE CYPHER                              ***
#     ***                             ---------------                              ***
#     ***                                                                          ***
#     ***                                                                          ***
#     ********************************************************************************
#     ********************************************************************************
#                         title generated using generate_title.py

#     Welcome to the Vigenere Cypher program
#     The cypher works by accepting a string of text and a rotation value
#     The string of text will be encrypted by having each letter replaced by the letter 
#     corresponding to the rotation amount\n
#     For example the letter "a" rotated 3 letters would be replaced with the letter "d"
#     If a rotation would go "out of bounds" (passed the letter "z") it will wrap and 
#     rotate the remaining letters starting over at "a"\n
#     You can decrypt the text as long as you know the rotation used in the encryption!\n
#     Try decrypting this one to start.
#     Text: janw'c hxd j lunena trccnw?
#     Rotation: start guessing!
#     """

#     print(welcome_message)
#     while True:
#         choice = input("Would you like to encrypt or decrypt?\nYou may enter 'encrypt', 'e', 'decrypt' or 'd'\n>>> ")
#         if choice not in ("encrypt", "e", "decrypt", "d"):
#             if choice in ("quit", "q", "exit", "let me out of here please :("): quit()
#             print("\nYou must type 'encrypt', 'e', 'decrypt' or 'd' to continue")
#         else:
#             choice = "encrypt" if choice == "e" else "decrypt"
#             input_text = input("Enter the text you would like to {0}\n>>> ".format(choice))
#             rotation_amount = input("Enter an amount to rotate by\n>>> ") if choice in ("encrypt", "e") else input("Enter the amount the encoded string was rotated by\n>>> ")
#             try:
#                 rotation_amount = int(rotation_amount)
#             except ValueError:
#                 print("Only integer values may be entered for the rotation. Try again")
#             else:
#                 if choice in ("decrypt", "d"):
#                     rotation_amount = 26 - rotation_amount
#                     print("\nEncrypted text: {0}\nDecrypted text: {1}".format(input_text, encrypt(input_text, rotation_amount)))
#                 else:
#                     print("\nUnencrypted text: {0}\nEncrypted text: {1}".format(input_text, encrypt(input_text, rotation_amount)))
#         quit_handler()

# if __name__ == "__main__":
#     main()
