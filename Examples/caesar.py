""" Caesar's Cypher with notes and comments """

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
    from string import ascii_lowercase # import the ascii_lowercase library "abcdefghijklmnopqrstuvwxyz"

    # first check if the character is alphabetic by using the isalpha() string method
    if character.isalpha(): # if the character IS alphabetic then proceed to the rest of the function block
        # get the initial 0-based alphabetic position of the character using the alphabet_position() function
        initial_position = alphabet_position(character) 
        # determine the new position by adding the rotation amount
        rotated_position = initial_position + rotation
        # modify the rotation amount if it goes beyond 25 (the end of the alphabet) using the modulus (%) operator
        if rotated_position > 25:
            rotated_position = rotated_position % 26 # use the % operator with the length of the alphabet (26) to "wrap around" the alphabet
        # use the ascii lowercase string to get the new letter (after rotation) using string indexing
        rotated_letter = ascii_lowercase[rotated_position]
        # modify the rotated letter if the original letter was uppercase
        if character.isupper(): # use the string method isupper() to determine if the original character was uppercase
            rotated_letter = rotated_letter.upper() # use the string method upper() to make the rotated letter capital
        return rotated_letter

    else:  # if the character IS NOT alphabetic then return the character as is (without rotation)
        return character

def encrypt(text, rotation):
    """
    accepts a string of text to be encoded by the rotation amount of the second argument
    returns an encrypted string
    """

    # build an output string by looping over each character in the text and calling rotate_character() on that character
        # build the output string using string concatenation within the loop
    
    output_string = "" # initialize the output string as an empty string to be concatenated in the loop

    for character in text: # loop over each character in the text
    # build the output_string by string concatenation with each rotated character
        output_string += rotate_character(character, rotation) 
    return output_string

def quit_handler():
    """ prompts the user to quit or continue """
    quit_choice = input("\nTo quit type 'q' or 'quit' otherwise hit any key to continue\n>>> ")
    if quit_choice in ("q", "quit"):
        print("Exiting the program")
        quit()

def main():
    """
    if Caesar's Cypher is to be used as a standalone program prompt the user for inputs
    and perform the encryption / decryption as requested
    """

    while True:
        choice = input("Would you like to encrypt or decrypt?\nYou may enter 'encrypt', 'e', 'decrypt' or 'd'\n>>> ")
        if choice not in ("encrypt", "e", "decrypt", "d"):
            print("\nYou must type 'encrypt', 'e', 'decrypt' or 'd' to continue")
        else:
            choice = "encrypt" if choice == "e" else "decrypt"
            input_text = input("Enter the text you would like to {0}\n>>> ".format(choice))
            rotation_amount = input("Enter an amount to rotate by\n>>> ") if choice in ("encrypt", "e") else input("Enter the amount the encoded string was rotated by\n>>> ")
            try:
                rotation_amount = int(rotation_amount)
            except ValueError:
                print("Only integer values may be entered for the rotation. Try again")
            else:
                if choice in ("decrypt", "d"):
                    rotation_amount = 26 - rotation_amount
                    print("\nEncrypted text: {0}\nDecrypted text: {1}".format(input_text, encrypt(input_text, rotation_amount)))
                else:
                    print("\nUnencrypted text: {0}\nEncrypted text: {1}".format(input_text, encrypt(input_text, rotation_amount)))
        quit_handler()

if __name__ == "__main__":
    main()
