import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row["letter"]: row["code"] for (index, row) in nato_df.iterrows()}
print(nato_dict)


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        words_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Please only enter letters. ")
        generate_phonetic()
    else:
        print(words_list)


generate_phonetic()


