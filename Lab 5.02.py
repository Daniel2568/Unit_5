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
my_paragraph = '''Dogs can be very good pets. In my opinion dogs are superior to cats. 
The reason being because dogs do more than just sit around.
I would prefer to have a pet that does more than just be there for emotional support.
Dogs can help do things for you and be a medical aid if you need them to be.
Dogs also have the energy to play more than cats which makes it better to have dogs around than cats.
Its a little biased but I like dogs more than cats.'''

#print my_paragraph
print(my_paragraph)

#make all letters lowercase
my_paragraph_lower = my_paragraph.lower()

#remove all periods
my_paragraph_lower_no_punctuation = my_paragraph_lower.replace(".", "")
my_paragraph_lower_no_punctuation = my_paragraph_lower_no_punctuation.replace("\n", "")


#convert paragraph into a list of individual strings
word_list = my_paragraph_lower_no_punctuation.split(" ")

#my paragraph dict
my_paragraph_dict = {}

#populate word dict
for word in word_list:
    if word in my_paragraph_dict:
        my_paragraph_dict[word] += 1
    else:
        my_paragraph_dict[word] = 1


while True:

    user_choice = input("What word would you like to know the frequency of?>")

    if word in my_paragraph_dict:
        print(f"The word '{user_choice}' appears {my_paragraph_dict[user_choice]} time(s) in the paragraph.")
    elif user_choice == 'q':
        break
    else:
        print(f"The word '{user_choice}' is not used in this paragraph.")
