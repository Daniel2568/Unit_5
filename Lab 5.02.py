'''
#############
Lab 5.02
#############
In this lab we will implement a word frequency algorithm. 
It will tell you how many of each word you had in an essay.

At the top of the document save a variable with a long paragraph (example below). 
In order to turn this paragraph into a list of lower case words we will use the split(" "), 
replace(), and lower() functions. There is code at the bottom of this page that will do this 
for you. Feel free to read more about split() in the Python documentation, but it's not critical 
to this lab.

For each word in the document, count the number of times it occurs. Consider the following phrase: 
'Cats are cool. Baby cats are called kittens. Cats make great pets.' The word 'cats' appears 3 times. 
The word 'are' appears 2 times.

The program will first create a dictionary with the words as keys and the number of times they occur 
as values. Then it will prompt the user which word they are curious about. If the word was in the 
paragraph it will print the number of times it occurred.

Example
------------
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? cats
'cats' occurs 3 times
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? dogs
'dogs' does not occur

split, replace, and lower
--------------------------
This is the code to lower case the letters in the paragraph, remove the periods, and split them into 
individual words.

example_paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk 
from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in 
New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided 
to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande 
decides to go to Times Square instead. What a beautiful day in New York."

#make all letters lowercase
example_paragraph_lower = example_paragraph.lower()

#remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")

#convert paragraph into a list of individual strings
example_word_list = example_paragraph_lower_no_punctuation.split(" ")
'''
my_paragraph = "Dogs can be very good pets. In my opinion dogs are superior to cats. The reason being because dogs do more than just sit around.\nI would prefer to have a pet that does more than just be there for emotional support. Dogs can help do things for you and be a medical aid if you need them to be.\nDogs also have the energy to play more than cats which makes it better to have dogs around than cats. Its a little biased but I like dogs more than cats."

my_paragraph_dict = {
'dogs': '7',
'can': '2',
'be': '4',
'being':'1',
'very': '1',
'good': '1',
'pets': '1',
'in': '1',
'my': '1',
'opinion': '1',
'are': '1',
'superior': '1',
'to': '5',
'cats': '4',
'the': '1',
'reason': '1',
'because': '1',
'do': '2',
'more': '4',
'than': '5',
'just': '2',
'sit': '1',
'around': '1',
'I': '2',
'would': '1',
'prefer': '1',
'have': '3',
'a': '2',
'pet': '1',
'that': '1',
'does': '1',
'for': '2',
'emotional': '1',
'support': '1',
'help': '1',
'things': '1',
'you': '1',
'and': '1',
'medical': '1',
'aid': '1',
'if': '1',
'need': '1',
'them': '1',
'also': '1',
'have': '2',
'energy': '1',
'play': '1',
'makes': '1',
'it': '1',
'its': '1',
'which': '1',
'better': '1',
'little': '1',
'biased': '1',
'but': '1',
'like': '1',
}

#find frequency of all words in paragraph
print(f"{my_paragraph}")
print()
word_choice = input("What word would you like to know the frequency of?>")
def frequency(word):
    if word in my_paragraph_dict:
        print(f"The word {word_choice} appears {my_paragraph_dict[word_choice]} time(s) in the paragraph.")
    else:
        print(f"The word {word_choice} is not used in this paragraph.")

frequency(word_choice)

#make all letters lowercase
my_paragraph_lower = my_paragraph.lower()

#remove all periods
my_paragraph_lower_no_punctuation = my_paragraph_lower.replace(".", "")


#convert paragraph into a list of individual strings
word_list = my_paragraph_lower_no_punctuation.split(" ")
