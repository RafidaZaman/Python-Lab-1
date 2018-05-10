#2)	Write a Python function that accepts a sentence of words from user and display the following:
# a)	Middle word
# b)	Longest word in the sentence
# c)	Reverse all the words in sentence

#b)
def find_longest_word(Sentence):
    longest_word =  max(Sentence, key=len)
    print("Longest word : ",longest_word)
    return longest_word

words = input('Please enter a few words')
Sentence = words.split()
find_longest_word(Sentence)

#c)
sentence="My name is Jacqueline Fernandez Dsouza"
def reversed_words(revers):
    return ' '.join(word[::-1] for word in revers.split())
print("Reversed Sentence :",reversed_words(sentence))

