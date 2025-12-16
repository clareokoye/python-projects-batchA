
"""
def main():
    word_dic = {
        'hi': 'a way of greeting',
        'nose': 'an organ for smelling',
        'planet': 'claudinwa et Bilinwa',
    }

    while True:
        word = input("what's the word?  ")
        if word == "":
            break
        if word in word_dic:
            #print(f"{word}: {word_dic[word]}")
            print(word: {word_dic[word]})
        if word not in word_dic:
            break


main()

"""

from PyDictionary import PyDictionary
#word = input("Enter your word: ")
#diction = PyDictionary.meaning(word)
while True:
    word = input("Enter your word: ")
    diction = PyDictionary.meaning(word)
    if word == "":
        quit()
    if diction is None:
        print("word not found")
        break
    else:
        print(diction)
        break
