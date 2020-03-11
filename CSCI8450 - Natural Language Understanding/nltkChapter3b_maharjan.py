import nltk, re, pprint

from urllib.request import urlopen

from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'

def question1():

    # Wh-words in English are used in questions, relative clauses and exclamations. 
    # Consider the set of wh-words to consist of the following members: 
    # what, where, when, which, who, whom, whose, why.

    # Your solution should account for the uppercase versions of the words in the list.

    # How many wh-words occur in text2?

    print("\nAnswer:")


    # Prepare the Wh-words given in question with Upper and Lower W/w
    wh_set = ["what", "where", "when", "which", "who", "whom", "whose", "why", "What", "Where", "When", "Which", "Who", "Whom", "Whose", "Why"]

    # Iterate `text2` tokens and search for Wh-words that starts with either W or w followed by h
    # Subset those words only for the Wh-words given in question
    text2_wh_set = [word for word in text2 if re.search('^[Ww]h', word) and word in wh_set]

    print("How many wh-words occur in text2? ", len(text2_wh_set))










def question2():


    # Wh-words in English are used in questions, relative clauses and exclamations. 
    # Consider the set of wh-words to consist of the following members: 
    # what, where, when, which, who, whom, whose, why.

    # Your solution should account for the uppercase versions of the words in the list

    # How many wh-words occur in text7? 
    

    print("\nAnswer:")


    # Prepare the Wh-words given in question with Upper and Lower W/w
    wh_set = ["what", "where", "when", "which", "who", "whom", "whose", "why", "What", "Where", "When", "Which", "Who", "Whom", "Whose", "Why"]

    # Iterate `text7` tokens and search for Wh-words that starts with either W or w followed by h
    # Subset those words only for the Wh-words given in question
    text7_wh_set = [word for word in text7 if re.search('^[Ww]h', word) and word in wh_set]

    print("How many wh-words occur in text7? ", len(text7_wh_set))










def question3():
    

    # Readability measures are used to score the reading difficulty of a text, 
    # for the purposes of selecting texts of appropriate difficulty for language learners. 
    
    # Let us define:
    # mu_w to be the average number of letters per word, and 
    # mu_s to be the average number of words per sentence, in a given text. 
    
    # The Automated Readability Index (ARI) of the text is defined to be: 
    
    # 4.71 * mu_w + 0.5 + mu_s - 21.43
    
    # Make use of the fact that nltk.corpus.brown.words() produces a sequence of words, 
    # while nltk.corpus.brown.sents() produces a sequence of sentences. 
    
    # Do not modify these lists as they are read in. 
    
    # What is the ARI score for the mystery section of the Brown Corpus?

    
    print("\nAnswer:")



    # Brown mystery section for words
    brown_mystery_words = nltk.corpus.brown.words(categories='mystery')

    # Brown mystery section for sentences
    brown_mystery_sentences = nltk.corpus.brown.sents(categories='mystery')


    # mu_w to be the average number of letters per word,
    # Calculate the average number of letters per word

    # Get the total number of letters
    total_number_letter = [len(word) for word in brown_mystery_words]
    
    # Sum total_number_letter
    # Get total size
    sum_total_number_letter = sum(total_number_letter)

    # Get the total number of words
    total_number_words = len(brown_mystery_words)
    
    average_letter_per_word = sum_total_number_letter / total_number_words
    print("Average number of letters per word: ", average_letter_per_word)




    # mu_s to be the average number of words per sentence, in a given text. 
    # Calculate the average number of words per sentences
    
    # Get the total number of words in each 
    # Get total size of each word
    total_number_words = [len(word) for word in brown_mystery_sentences]
    
    # Sum total_number_words
    sum_total_number_words = sum(total_number_words)

    # Get the total number of words
    total_number_sentences = len(brown_mystery_sentences)
    
    average_words_per_sentence =  sum_total_number_words / total_number_sentences


    print("Average number of words per sentences: ", average_words_per_sentence)
        

    # Calculate the Automated Readability Index (ARI) by using the formula 
    ari_score = (4.71 * average_letter_per_word) + (0.5 * average_words_per_sentence) - 21.43
    
    # Round off ARI score to 4 decimanl
    ari_score = round(ari_score, 4)

    print("ARI Score: (round to 4 decimal) ", ari_score)















def question4():
   
    # Use the Porter Stemmer to normalize some tokenized text, calling the stemmer on each word. 
    # Do the same thing with the Lancaster Stemmer and see if you observe any differences. 
    
    # Use the SimpleText to report your results.

    # SimpleText is a string provided in the template document.

    # Report any differences you observe. Why do you observe these differences?

    
    print("\nAnswer:")



    SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'


    # Initialize Porter Stemmer
    porter = nltk.PorterStemmer()

    # Initialize Lancaster Stemmer
    lancaster = nltk.LancasterStemmer()

    # Normalize SimpleText into its Word Tokens
    SimpleText = nltk.word_tokenize(SimpleText)


    # Use the Porter Stemmer to normalize some tokenized text, calling the stemmer on each word.
    # print([porter.stem(t) for t in SimpleText])

    # Do the same thing with the Lancaster Stemmer and see if you observe any differences.
    # print([lancaster.stem(t) for t in SimpleText])


    # For each token in SimpleText, use Porter Stemmer and Lancaster Stemmer
    for word in SimpleText:
        print("Original Word: ", word)
        print("Porter Stemmer: ", porter.stem(word))
        print("Lancaster Stemmer: ", lancaster.stem(word))
        print("")

        print("I provided explanation about the differences in Canvas")












def question5():
    
    # Obtain raw texts for ABC Rural News and ABC Science News 
    # (from nltk.corpus.abc; 
    
    # nltk.corpus.abc.raw('rural.txt'), and 
    # nltk.corpus.abc.raw('science.txt'), respectively). 
    
    # Use nltk.word_tokenize() function to tokenize given text into words. 
    
    # Section 3.8 in “Sentence Segmentaion” lists an example of using Punkt for finding the sentences.

    # Compute the ARI scores. Which category has a greater ARI score?


    print("\nAnswer:")


    # Function to compute ARI score of ABC Rural News
    def abc_rural():

        # Obtain raw texts for ABC Rural News
        abc_rural_txt = nltk.corpus.abc.raw('rural.txt')

        # Use nltk.word_tokenize() function to tokenize given text into words. 
        abc_rural_tokens = nltk.word_tokenize(abc_rural_txt)

        # Convert raw texts into sentences using Punkt Section 3.8 in “Sentence Segmentaion”
        abc_rural_sents = nltk.sent_tokenize(abc_rural_txt)
        abc_rural_sents_token = [nltk.word_tokenize(word) for word in abc_rural_sents]


        # mu_w to be the average number of letters per word,
        # Calculate the average number of letters per word

        # Get the total number of letters for ABC Rural News
        total_number_letter_rural = [len(word) for word in abc_rural_tokens]
        
        # Sum total_number_letter_rural
        # Get total size
        sum_total_number_letter_rural = sum(total_number_letter_rural)

        # Get the total number of words in ABC Rural News
        total_number_words_rural = len(abc_rural_tokens)
        
        average_letter_per_word_rural = sum_total_number_letter_rural / total_number_words_rural
        print("Average number of letters per word in ABC Rural: ", average_letter_per_word_rural)


        # mu_s to be the average number of words per sentence, in a given text. 
        # Calculate the average number of words per sentences
        
        # Get the total number of words in each sentences
        # Get total size of each word
        total_number_words_sentences = [len(word) for word in abc_rural_sents_token]
        
        # Sum total_number_words
        sum_total_number_words_rural = sum(total_number_words_sentences)

        # Get the total number of words
        total_number_sentences_rural = len(abc_rural_sents_token)
        
        # Calculate the average score
        average_words_per_sentence_rural =  sum_total_number_words_rural / total_number_sentences_rural

        print("Average number of words per sentence in ABC Rural: ", average_words_per_sentence_rural)
            
        # Calculate the Automated Readability Index (ARI) by using the formula 
        ari_score_rural = (4.71 * average_letter_per_word_rural) + (0.5 * average_words_per_sentence_rural) - 21.43
        
        print("ARI Score for ABC Rural: ", ari_score_rural, "\n")


        # Return the ari_score_rural 
        return ari_score_rural


    # Save the returned value to abc_rural_score
    abc_rural_score = abc_rural()




    # Function to compute ARI score of ABC Science News
    def abc_science():

        # Obtain raw texts for ABC Science News
        abc_science_txt = nltk.corpus.abc.raw('science.txt')

        # Use nltk.word_tokenize() function to tokenize given text into words. 
        abc_science_tokens = nltk.word_tokenize(abc_science_txt)

        # Convert raw texts into sentences using Punkt Section 3.8 in “Sentence Segmentaion”
        abc_science_sents = nltk.sent_tokenize(abc_science_txt)
        abc_science_sents_token = [nltk.word_tokenize(word) for word in abc_science_sents]


        # mu_w to be the average number of letters per word,
        # Calculate the average number of letters per word

        # Get the total number of letters for ABC Science News
        total_number_letter_science = [len(word) for word in abc_science_tokens]
        
        # Sum total_number_letter_science
        # Get total size
        sum_total_number_letter_science = sum(total_number_letter_science)

        # Get the total number of words in ABC Rcience News
        total_number_words_science= len(abc_science_tokens)
        
        average_letter_per_word_science = sum_total_number_letter_science / total_number_words_science
        print("Average number of letters per word in ABC Science: ", average_letter_per_word_science)


        # mu_s to be the average number of words per sentence, in a given text. 
        # Calculate the average number of words per sentences
        
        # Get the total number of words in each sentences
        # Get total size of each word
        total_number_words_sentences = [len(word) for word in abc_science_sents_token]
        
        # Sum total_number_words
        sum_total_number_words_science = sum(total_number_words_sentences)

        # Get the total number of words
        total_number_sentences_science = len(abc_science_sents_token)
        
        average_words_per_sentence_science =  sum_total_number_words_science / total_number_sentences_science


        print("Average number of words per sentence in ABC Science: ", average_words_per_sentence_science)

            
            

        # Calculate the Automated Readability Index (ARI) by using the formula 
        ari_score_science = (4.71 * average_letter_per_word_science) + (0.5 * average_words_per_sentence_science) - 21.43
        
        print("ARI Score for ABC Science: ", ari_score_science, "\n")


        # Return the ari_score_science 
        return ari_score_science

    # Save the returned value to abc_science_score
    abc_science_score = abc_science()

    print("ABC Rural News has a greater ARI score" if abc_rural_score > abc_science_score else "ABC Science News has a greater ARI score")









def question6(): 
    
    # What is the difference between the greater ARI score and the lesser ARI score produced in the previous question? 
    # (positive or negative difference is accepted)


    print(""" 
    Answer:

    From the previous question #5, we have:

    ARI Score for ABC Rural:  12.61676279331764 
    ARI Score for ABC Science:  12.773526577547678 

    Here, we can see that ABC Science has a greater ARI Score and ABC Rural has a lesser ARI Score.

    The differnce between them is the following (round to 4 decimal): (ABC Science - ABC Rural) is """, round(12.773526577547678 - 12.61676279331764, 4)
    
    )













def question(questionNum):
    print("Question {}".format(questionNum))

    globals()["question"+str(questionNum)]()
    print("")


def main():
    question(1) # exercise(18)
    question(2) # exercise(18)
    question(3) # exercise(29)
    question(4) # exercise(30)
    question(5) # exercise(40)
    question(6) # exercise(40)


if __name__ == "__main__":
    main()

