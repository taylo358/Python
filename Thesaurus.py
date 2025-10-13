def load_synonyms(word):
    """Load synonyms from the file into a dictionary."""
    try:
        synonyms_dict = {}
        with open(f"{word}.txt", "r") as file:
            for line in file:
                synonyms = line.strip().split()
                if synonyms:
                    # Use the first letter of each synonym group as the key
                    key = synonyms[0][0]
                    synonyms_dict[key] = synonyms
        return synonyms_dict
    except FileNotFoundError:
        print(f"File {word}.txt not found.")
        return None

def main():
    # Read word and letter from the user
    word = input().strip().lower()
    letter = input().strip().lower()

    # Load synonyms from the file into a dictionary
    synonyms_dict = load_synonyms(word)
    if synonyms_dict is None:
        return

    # Check if there are synonyms starting with the given letter
    if letter in synonyms_dict:
        for synonym in synonyms_dict[letter]:
            print(synonym)
    else:
        print(f"No synonyms for {word} begin with {letter}.")

# Call the main function
main()

'''
Explanation:
Given a set of text files containing synonyms for different words, complete the main program to output the synonyms for a specific word. Each text file contains synonyms for the word specified in the file’s name, and each row within the file lists the word’s synonyms that begin with the same letter, separated by a space. The program reads a word and a letter from the user and opens the text file associated with the input word. The program then stores the contents of the text file into a dictionary predefined in the program. Finally the program searches the dictionary and outputs all the synonyms that begin with the input letter, one synonym per line, or a message if no synonyms that begin with the input letter are found.

Hints: Use the first letter of a synonym as the key when storing the synonym into the dictionary. Assume all letters are in lowercase.

Ex: If the input of the program is:

educate
c
the program opens the file educate.txt, which contains:

brainwash brief
civilize coach cultivate
develop discipline drill
edify enlighten exercise explain
foster
improve indoctrinate inform instruct
mature
nurture
rear
school
train tutor
then the program outputs:

civilize
coach
cultivate
Ex: If the input of the program is:

educate
a
then the program outputs:

No synonyms for educate begin with a.
'''
