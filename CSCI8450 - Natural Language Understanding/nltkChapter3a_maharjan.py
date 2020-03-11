import nltk, re, pprint

from urllib.request import urlopen
from urllib import request

from bs4 import BeautifulSoup

from nltk import book

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn


SimpleText = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'
# SimpleText = 'a an the A An The Quiet, quiet, aquiet, aQuiet, One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'

def question1():

    #Describe the class of strings matched by the following regular expression: [A-Z][a-z]*
    print(""" 
    
    The regular expression [A-Z][a-z]* match the zero or more words that starts with Uppercase Letter and followed
    by any number of Lowercase number becuase it has a Kleene closures.
    
    """)




def question2():

    # Describe the class of strings matched by the following regular expression: p[aeiou]{,2}t
    print(""" 
    
    The regular expression p[aeiou]{,2}t match that start p then followed by upto 2 vowels and followed by letter t
     
    """)




def question3():

    # Describe the class of strings matched by the following regular expression: \w+|[^\w\s]+
    
    print(""" 
    
    The regular expression \w+|[^\w\s]+ match one or more letter or one or more that are not a letter or a white space
    
    """)




def question4():

    # Write regular expressions to match the following class of strings:
    # A single determiner (assume that a, an, and the are the only determiners).
    # What is the entire output of your regular expression when it is run on SimpleText?
    # SimpleText is a string provided in the template document.
    # Use nltk.re_show() for your output.



    match_determiner = nltk.re_show(r'\b([Aa][Nn]?|[Tt][Hh][Ee])\b', SimpleText, left='[ ', right=' ]')

    return match_determiner




def question5():

    # Question 5

    # Write a function unknown() that takes a URL as its argument, 
    # and returns a list of unknown words that occur on that webpage. 
    # In order to do this, extract all substrings consisting of lowercase letters (using re.findall()) 
    # and remove any items from this set that occur in the Words Corpus (nltk.corpus.words).


    # Function USING re.findall
    def unknown(url):

        print("USING re.findall - re.findall() ")
        print("-------------------------------\n")

        # Get the text from the `url` parameter
        dijkstra_html = request.urlopen(url).read().decode('utf8')

        # Strip HTML element/components from `dijkstra_without_html`
        dijkstra_without_html = BeautifulSoup(dijkstra_html, "html.parser").get_text()

        # Extract all substrings consisting of lowercase letters (using re.findall()) in `dijkstra_without_html`
        dijkstra_without_html_lower = re.findall(r'\b[a-z]+', dijkstra_without_html)

        # Set of word in Words Corpus 
        set_words = set(nltk.corpus.words.words('en'))

        # Words that are lowercase and does not appear in Words Corpus (nltk.corpus.words)
        unknown_words = [word for word in dijkstra_without_html_lower if word not in set_words]
        
        print("unknown_words len: ", len(unknown_words))
        
        return unknown_words

    print(unknown('https://www.cs.utexas.edu/~vl/notes/dijkstra.html'))





    # Function USING unknown_word_tokenize
    def unknown_word_tokenize(url):

        print("\n USING unknown_word_tokenize - nltk.word_tokenize()")
        print("-----------------------------------------------------\n")

        # Get the text from the `url` parameter
        dijkstra_html = request.urlopen(url).read().decode('utf8')

        # Strip HTML element/components from `dijkstra_without_html`
        dijkstra_without_html = BeautifulSoup(dijkstra_html, "html.parser").get_text()

        # Extract all substrings consisting of lowercase letters in `dijkstra_without_html`
        dijkstra_without_html_lower = nltk.word_tokenize(dijkstra_without_html)
        dijkstra_without_html_lower = [word for word in dijkstra_without_html_lower if word.islower()]

        # Set of word in Words Corpus 
        set_words = set(nltk.corpus.words.words('en'))

        # Words that are lowercase and does not appear in Words Corpus (nltk.corpus.words)
        unknown_word_tokenize = [word for word in dijkstra_without_html_lower if word not in set_words]
        print("unknown_word_tokenize len: ", len(unknown_word_tokenize))

        return unknown_word_tokenize

    print(unknown_word_tokenize('https://www.cs.utexas.edu/~vl/notes/dijkstra.html'))





    # Function USING WordNet lemmatizer  - nltk.WordNetLemmatizer() 
    def unknown_wnl(url):

        print("\nUSING WordNet lemmatizer  - nltk.WordNetLemmatizer() ")
        print("----------------------------------------------------\n")

        # Get the text from the `url` parameter
        dijkstra_html = request.urlopen(url).read().decode('utf8')

        # Strip HTML element/components from `dijkstra_without_html`
        dijkstra_without_html = BeautifulSoup(dijkstra_html, "html.parser").get_text()

        # Extract all substrings consisting of lowercase letters (using re.findall()) in `dijkstra_without_html`
        dijkstra_without_html_lower = re.findall(r'\b[a-z]+', dijkstra_without_html)

        print("Actual lower words only upto 100... from the URL: ", '\n', dijkstra_without_html_lower[:100])
        print("Total length of above full words: ", len(dijkstra_without_html_lower), '\n')


        # Instantiate WordNet lemmatizer 
        wnl = nltk.WordNetLemmatizer()

        # Chapter 3 Question 5.2: Use nltk.WordNetLemmatizer() on your tokens before checking them against the Words Corpus. 
        # Do you find fewer or more unknown words? Why?
        dijkstra_without_html_lower_wnl = [wnl.lemmatize(t) for t in dijkstra_without_html_lower]
        print("Actual words upto 100... after nltk.WordNetLemmatizer(): ", '\n', dijkstra_without_html_lower_wnl[:100])
        print("Total length above full words: ", len(dijkstra_without_html_lower_wnl), '\n')

        # Set of word in Words Corpus 
        set_words = set(nltk.corpus.words.words('en'))


        # Words that are lowercase and does not appear in Words Corpus (nltk.corpus.words)
        unknown_wnl = [word for word in dijkstra_without_html_lower_wnl if word not in set_words]
        print("All words after going through nltk.WordNetLemmatizer() and Words Corpous: ", '\n', unknown_wnl )
        print("Total length  above full words: ", len(unknown_wnl), '\n')
        
        
        return unknown_wnl


    unknown_wnl('https://www.cs.utexas.edu/~vl/notes/dijkstra.html')


    


def question6():

    # Convert SimpleText to Pig Latin.
    # SimpleText is a string provided in the template document.

    # To convert a word to Pig Latin
        # move any consonant (or consonant cluster) that appears at the start of the word to the end
        # append ay
        # preserve capitalization
        # keep qu together (i.e. so that quiet becomes ietquay)
        # detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style)
        # string → ingstray, idle → idleay, style → ylestay, yellow → ellowyay.

    # Report the entire outcome below


    # Create a tokens for the SimpleText
    SimpleText_tokens = nltk.word_tokenize(SimpleText)


    # Helper function to check consonants
    def pig_latin_helper(SimpleText):

        pattern = re.compile(r'^[^aeiouAEIOU]+')
        
        if re.findall(pattern, SimpleText):

            # Save the CONSONANT word
            check_consonant = re.findall(pattern, SimpleText)
            # print("Available Consonant: ", check_consonant)

            # Save the NON-CONSONANT word
            SimpleText = pattern.sub('', SimpleText)
            # print(" Non Consonant word: ", SimpleText)

            # Move the first consequtive CONSONANT letter(s) at the end
            SimpleText = SimpleText + str(check_consonant[0])

            #  Return SimpleText
            return SimpleText
        
        # Return same if there is no match 
        return SimpleText



    # Helper function to check the [detect when y is used as a consonant]
    def pig_latin_helper_y(SimpleText):

        if re.findall(r'[^aeiouAEIOU]y[^aeiouAEIOU]', SimpleText):
           
            # Treat y as vowel if its assumed as CONSONANT
            pattern = re.compile(r'^[^aeiouAEIOUy]+')

            check_y = re.findall(pattern, SimpleText)
            SimpleText = pattern.sub('', SimpleText)
            SimpleText = SimpleText + str(check_y[0]) 
            
            return SimpleText
        
        # Return SimpleText if there is no match
        return SimpleText




    # Check if the starting letters of the word is with Qu or qu
    def pig_latin_helper_qu(SimpleText):
        
        # Match a word that has/starts with Q and q followed by u
        if re.findall(r'^[Qq]u', SimpleText):
            
            # keeps qu together a la quiet
            pattern = re.compile(r'^[Qq]u')
            check_qu = re.findall(pattern, SimpleText)
            SimpleText = pattern.sub('', SimpleText)
            SimpleText = SimpleText + str(check_qu[0])

            return SimpleText

        return SimpleText
    
    


    # Main Function for converting text into Pig Latin
    # Get a SimpleText as parameters
    def pig_latin(SimpleText):
        
        # Initialize empty pig_latin placeholder
        pig_latin = ''

        # Check if the charaters are alphabets
        pattern = re.compile(r'[^a-zA-Z]')


        # For each token in SimpleText_tokens, we pass to helper functions
        # Each Helper function does a specific task, such as check for consonants, [Qq]u and y used as vowels
        # Finally append ay 
        for token in SimpleText_tokens:
            
            if not re.findall(pattern, token):
                
                # Send a single token to helper function to check and manage qu.
                # keep qu together (i.e. so that quiet becomes ietquay)
                SimpleText = pig_latin_helper_qu(token)

                # detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style)
                SimpleText = pig_latin_helper_y(SimpleText)

                # check for consonant if it appears as a first letter in the word
                SimpleText = pig_latin_helper(SimpleText)

                # append `ay` at the end of the word once other Pig Latin requirement is met
                SimpleText = SimpleText + 'ay'

                # Concatenate Pig Latin words 
                pig_latin = pig_latin + ' ' + SimpleText
            
            else:
                pig_latin = pig_latin + token

        # Return SimpleText in Pig Latin 
        return pig_latin

    print(pig_latin(SimpleText))









def question(questionNum):
    print("Question {}".format(questionNum))

    globals()["question"+str(questionNum)]()
    print("")


def main():
    question(1) # exercise(6)
    question(2) # exercise(6)
    question(3) # exercise(6)
    question(4) # exercise(7)
    question(5) # exercise(21)
    question(6) # exercise(25)


if __name__ == "__main__":
    main()

