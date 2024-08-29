import sys

# Braille translation dictionaries
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
    "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "......": " ", ".....O": "cap",
    ".O.OOO": "num"}

english_to_braille = {x: y for y, x in braille_to_english.items() if x not in ['cap', 'num']}

def translate_braille_to_english(braille_input):
    output = []
    braille_input = [braille_input[i:i+6] for i in range(0, len(braille_input), 6)]
    
    is_cap = False
    is_num = False
    
    for cell in braille_input:
        if cell == ".....O":
            is_cap = True
            continue
        if cell == ".O.OOO":
            is_num = True
            continue
        if cell == "......":
            output.append(" ")
            is_cap = False
            is_num = False
        else:
            character = braille_to_english.get(cell, "")
            if is_cap:
                character = character.upper()
                is_cap = False
            if is_num:
                output.append(str(ord(character) - ord('a') + 1))
            else:
                output.append(character)
    
    return "".join(output)

def translate_english_to_braille(eng_input):
    output = []
    
    for char in eng_input:
        if char.isupper():
            output.append(".....O")
            char = char.lower()
        if char.isdigit():
            output.append(".O.OOO")
            num_char = chr(ord('a') + int(char) - 1)
            output.append(english_to_braille[num_char])
        else:
            output.append(english_to_braille.get(char, ""))
    
    return "".join(output)

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <string>")
        return
    
    input_string = sys.argv[1]
    
    # Check if the input is Braille (contains only O and .)
    if set(input_string).issubset({'O', '.'}):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))

if __name__ == "__main__":
    main()
