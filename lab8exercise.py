def find_first_repeating_character(s):
    character_count = {}

    for character in s:
        #check if the character already encountered
        if character in character_count:
            # Print the memory adress of the repeating character
            print(f"The memory adress of the first repeating character '{character}' is: {id(character)}")
            return id(character)
        else:
            # store the count of character
            character_count[character] = 1

    # if no repeating character found
    return None
    
print(find_first_repeating_character("people"))