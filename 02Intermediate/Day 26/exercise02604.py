# Python program to count the letters in the words of a sentence using a Dictionary Comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()

result = {word: len(word) for word in word_list}
print(result)
