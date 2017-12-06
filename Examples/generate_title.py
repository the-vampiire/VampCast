"""
Generates an ASCII title output like this one...

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^                                                                          ^^^
^^^                                                                          ^^^
^^^                                 --------                                 ^^^
^^^                                 VAMPIIRE                                 ^^^
^^^                                 --------                                 ^^^
^^^                                                                          ^^^
^^^                                                                          ^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if called with __name__ as __main__ 
    prompts for title and character to use for the border

no input validation at the moment...care to help improve? make it better and share!
"""

def generate_title_table(title, edge_character = "#", height = 11, width = 80, thickness = 2,   side_thickness = 3):
    mid_row = (height / 2) if height % 2 == 0 else ((height + 1) / 2)
    middle_rows = [(mid_row - 1), mid_row, (mid_row + 1)]
    title_length = len(title)
    number_of_spaces = int((((width - (side_thickness * 2)) - title_length) / 2))
    left_spaces = (number_of_spaces * " ")
    right_spaces = left_spaces if title_length % 2 == 0 else ((number_of_spaces + 1) * " ")
    edge = side_thickness * edge_character
    output = ""

    for row in range(1, height + 1):
        if row not in middle_rows: # normal rows
            if row in [(thickness - 1), thickness, (height - 1), height]: # top / bottom
                output += ((edge_character * width)  + "\n")
            else: # character-edged rows
                output += (edge + (" " * (width - (2 * side_thickness))) + edge + "\n")
        else: # title rows
            if row != mid_row:
                output += (edge + left_spaces + ("-" * title_length) + right_spaces + edge + "\n")
            else:
                output += (edge + left_spaces + title.upper() + right_spaces + edge + "\n")
    return output

if __name__ == "__main__":
    title = input("enter a title to generate your ASCII title output!\n>>> ")
    character = input("what character will the border be made of?\n>>> ")
    print("\n" + generate_title_table(title, character))
