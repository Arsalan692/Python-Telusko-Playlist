


def count_word_in(file_name, specific_word=None):
    try:
        with open(filename) as file_obj:
            content = file_obj.read()
    except FileNotFoundError:
        print("There is no file of this name! ")
    else:
        splitted = content.split()
        print(f"There are {len(splitted)} words in \"{file_name}\". ")
        if specific_word:
            specific_word_counter = splitted.count(specific_word)
            print(f"Its {specific_word_counter} times")


filename = "Simple_Text.txt"
