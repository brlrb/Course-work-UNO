from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen

#from nltk import book

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc
from nltk.corpus import stopwords

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'


def question1():
    # Train a unigram tagger on all of the sentences from the Brown corpus with the category news, 
    # just as described in the “Unigram” Subsection of Section 5.1 of the textbook.

    # Evaluate your tagger using “evaluate” function on all of the sentences from the Brown corpus with the category lore. 
    # How does this number compare when this tagger is evaluated on all of the sentences from the Brown corpus with the category news? 
    # Why is this the case?


    # Automatically add part-of-speech tags to text for brown corpus `news` category
    brown_tagged_sents_news = brown.tagged_sents(categories = 'news')

    # break down the brown corpus `news` category per sentences
    brown_sents_news = brown.sents(categories='news')

    #Train the brown_tagged_sents_news - UnigramTagger is a single word context-based tagger 
    unigram_tagger_news = nltk.UnigramTagger(brown_tagged_sents_news)

    # Evaluate the tagger using “evaluate”
    print("Brown Corpus Category = News: ", unigram_tagger_news.evaluate(brown_tagged_sents_news))


    # Evaluate your tagger using “evaluate” function on all of the sentences from the Brown corpus with the category lore. 
    # Automatically add part-of-speech tags to text for brown corpus `lore` category
    brown_tagged_sents_lore = brown.tagged_sents(categories = 'lore')
    unigram_tagger_lore = nltk.UnigramTagger(brown_tagged_sents_lore)

    print("Brown Corpus Category = Lore: ",unigram_tagger_lore)




def question2():

    # Write code to search the Brown Corpus for particular words and phrases according to tags. 
    # Report your findings separately for the following categories of Brown corpus: humor, romance, government.

    # Produce an alphabetically sorted list of the distinct words tagged with JJ. 
    # What is the number of distinct words tagged with JJ for category

    def search_word_phrase(tag, category):

        # Tagged words of Brown for the Part of Speech
        brown_tag = brown.tagged_words(categories = category)

        # Find all the words tagged with JJ
        brown_tag_jj = [(a,b) for (a,b) in brown_tag if b == tag]

        # Convert each word into lowercase
        brown_tag_jj = [a.lower() for (a,b) in brown_tag_jj]

         # Get the list of distinct words
        brown_tag_jj = set(brown_tag_jj)

        # Sort the words tagged with JJ 
        brown_tag_jj = sorted(brown_tag_jj)

        print("Alphabetically sorted list of distinct words JJ: ", brown_tag_jj)

        # Get the length of words tagged with JJ
        brown_tag_jj = len(brown_tag_jj)

        print(category, 'tagged with ', tag, ' count = ', brown_tag_jj)


    # Function to call with TAG with corrosponding Brown Category name
    search_word_phrase(tag = 'JJ', category = 'humor')
    search_word_phrase(tag = 'JJ', category = 'romance')
    search_word_phrase(tag = 'JJ', category = 'government')



def question3():

    # Write code to search the Brown Corpus for particular words and phrases according to tags. 
    # Report your findings separately for the following categories of Brown corpus: humor, romance, government.

    # Identify words that occur as both plural nouns and third person singular verbs (e.g. deals, flies). 
    # Sort these words alphabetically.

    # What is the second element of the sorted list for
    
    
    def search_word_phrase(category): 
       
        # Search Brown Corpus according to its tags
        brown_tag = brown.tagged_words(categories = category)

        #Get the Confitional Frequency of the text
        brown_cfd = nltk.ConditionalFreqDist(brown_tag)
        conditions = brown_cfd.conditions() 

        # Check if the word occur as both both plural nouns third person singular verbs
        nns_vbz_words = [condition for condition in conditions if brown_cfd[condition]['NNS'] or brown_cfd[condition]['VBZ']]

        # Sort the list of words that appear as both both plural nouns third person singular verbs
        sorted_nns_vbz_words = sorted(nns_vbz_words)

        # Print the sorted list
        print("nns_vbz_words: ", sorted_nns_vbz_words)

        # return the second element of the sorted list
        return sorted_nns_vbz_words[1]


    return_humor = search_word_phrase(category = 'humor')
    return_romance = search_word_phrase(category = 'romance')
    return_government = search_word_phrase(category = 'government')

    print("Humor second element: ", return_humor)
    print("Romance second element: ", return_romance)
    print("Government second element: ", return_government)




def question4():


    # Write code to search the Brown Corpus for particular words and phrases according to tags. 
    # Report your findings separately for the following categories of Brown corpus: humor, romance, government.

    # Identify three-word prepositional phrases of the form IN + AT + NN (eg. at the house).

    # What is the most frequent three-word prepositional phrases (break ties alphabetically) for


    def search_word_phrase(category):

        # Fetch the tagged text in brown
        brown_tagged_text = brown.tagged_words(categories = category)

        # Convert the fetched text into trigrams (three words)
        brown_trigrams = list(nltk.trigrams(brown_tagged_text))

        result_trigram = [trigram for trigram in brown_trigrams if [t for t in zip(*trigram)][1] == ('IN', 'AT', 'NN')]  
        sorted_result_trigram = sorted(result_trigram)
        
        # print("sorted_result_trigram: ", sorted_result_trigram)
        
        jj_trigram_lower = [((a.lower(), b), (c,d), (e,f)) for (a, b), (c,d), (e,f) in sorted_result_trigram]
        
        # print("jj_trigram_lower: ", jj_trigram_lower)

        brown_trigram_freq = [nltk.FreqDist(jj_trigram_lower)]

        print(category, "most frequent three-word prepositional phrases: " ,brown_trigram_freq)



    search_word_phrase(category = 'humor')
    search_word_phrase(category = 'romance')
    search_word_phrase(category = 'government')





def question5():
    
    # Write code to search the Brown Corpus for particular words and phrases according to tags. 
    # Report your findings separately for the following categories of Brown corpus: humor, romance, government.

    # Brown tags for pronouns include 
    # ['PPL-HL', 'PPO', 'PPS-NC', 'PPS+HVD', 'PP$-NC', 'PPO-TL', 'PPS+BEZ-NC', 'PPL', 'PPL-NC', 'PPO-NC', 'PPS', 
    # 'PP$-TL', 'PPS-HL', 'PP$$', 'PPS+BEZ', 'PPS+MD', 'PPS+HVZ', 'PPS-TL', 'PP$'] . 

    # What number of masculine pronouns [himself, his, him , he, he's, he'd, he'll] 
    # and feminine pronouns [herself, her, hers, she, she's, she'd, she'll] are there. 
    
    # When constructing your code ensure that you count only occurrences of listed pronouns tagged by listed tags. 
     
    # Consider an uppercase "She" to count toward this total as "she" is in the feminine pronouns list.



    masculine = ['himself','his','him','he',"he's","he'd","he'll"]

    feminine = ['herself','her','hers','she',"she's","she'd","she'll"]

    pronoun_tags = ['PPL-HL', 'PPO', 'PPS-NC', 'PPS+HVD', 'PP$-NC', 'PPO-TL',
                'PPS+BEZ-NC', 'PPL', 'PPL-NC', 'PPO-NC', 'PPS', 'PP$-TL',
                'PPS-HL', 'PP$$', 'PPS+BEZ', 'PPS+MD', 'PPS+HVZ', 'PPS-TL', 'PP$']


    def search_word_phrase(category):

        # Given data in question
        masculine = ['himself','his','him','he',"he's","he'd","he'll"]
        feminine = ['herself','her','hers','she',"she's","she'd","she'll"]

        # Get the words in the Brown Corpus
        brown_tagged_text = brown.tagged_words(categories = category)

        # Convert each words into lower case
        # Check if the word appear in the listed tag
        # Check if the word belong to the listed pronouns
        brown_words_masculine = [(word.lower(), tag) for (word, tag) in brown_tagged_text if word in masculine and tag in pronoun_tags]
        brown_words_feminine = [(word.lower(), tag) for (word, tag) in brown_tagged_text if word in feminine and tag in pronoun_tags]


        # print("brown_words_masculine: ", brown_words_masculine)
        # print("brown_words_feminine: ", brown_words_feminine)


        print("brown_words_masculine LEN for ", category, "= ", len(brown_words_masculine))
        print("brown_words_feminine LEN ", category, "= ", len(brown_words_feminine))
        print('\n')



    search_word_phrase(category = 'humor')
    search_word_phrase(category = 'romance')
    search_word_phrase(category = 'government')

    


def question6():    

    # Analyze the tagged words to determine the number of distinct words that have exactly 5 possible tags. 
    # For example: The word read has 4 possible tags (NP, VB, VBN, VBD) found in the Brown corpus, 
    # whereas debt only has one possible tag (NN).

    # What number of tagged words have exactly 5 possible tags?


    # Tagged word in Brown Corpus POS
    brown_tags = brown.tagged_words()

    # Normalize the words and lowercase the word
    brown_tags = [(word.lower(), tag) for (word, tag) in brown_tags]

    brown_tags = set(brown_tags)

    # Conditional Freq dist
    brown_cfd = nltk.ConditionalFreqDist((word, tag) for (word, tag) in brown_tags)

    # count the number of times it appears
    count = 0

    # Check what words has 5 tags associated with it
    for word in sorted(brown_cfd.conditions()):
        if len(brown_cfd[word]) == 5:
            count = count + 1
            tags_cnt = [tag for (tag, _) in brown_cfd[word].most_common()]
            final_words = word, ' '.join(tags_cnt)
            print(final_words)


    print("Total count of 5 possible tags: ", count )
        










def question7():
    

    # Determine which word(s) has/have the most distinct tags in Brown corpus. 

    # Choose one of these word(s) and find sentences demonstrating the use of at 
    # least 5 distinct tags from the possible tags for the selected word.

    # Report the word(s), the word(s) tag list(s), and the derived sentence(s).

    # set the stop words
    stop_words = stopwords.words('english')

    # Tagged word in Brown Corpus POS
    brown_tags = brown.tagged_words()

    # Normalize the words and lowercase the word
    brown_tags = [(word.lower(), tag) for (word, tag) in brown_tags if word not in stop_words]

    brown_tags = set(brown_tags)

    # Conditional Freq dist
    brown_cfd = nltk.ConditionalFreqDist((word, tag) for (word, tag) in brown_tags)

    # Check what words has more than 10 tags associated with it - to find most distinct words
    print("Some words with most distinct tags ( >7 ): ")
    for word in sorted(brown_cfd.conditions()):
        if len(brown_cfd[word]) > 7:
            tags_cnt = [tag for (tag, _) in brown_cfd[word].most_common()]
            final_words = word, ' '.join(tags_cnt)
            print(final_words)

        
    print("\nI selected 'home' \n")
    print(" home_word_tags =  'NR-HL', 'NN-NC', 'NR-TL', 'NP', 'NR-NC', 'VB', 'NN-TL', 'NN-HL', 'NN', 'NR' are the tags for 'home' \n")

    # Tagged sentences in Brown Corpus POS
    brown_tag_sents = brown.tagged_sents()

    home_word_tags = ['NR-HL', 'NN-NC', 'NR-TL', 'NP', 'NR-NC', 'VB', 'NN-TL', 'NN-HL', 'NN', 'NR']

    # For each single sentences in Brown Corpus sentences, get the list of tags
    # Get the distinct list of tags for these sentences
    # Loop over the tags to check with our list of tags if it matches
    # If it matches, then print the sentences
    for single_sentence in brown_tag_sents:
        
        # get the list of tags from the single sentence
        list_sents = [(tag) for (word, tag) in single_sentence]

        # convert it into a distincet tag set
        list_sents_set = set(list_sents)
        
        # counter to check if atleast 5 tags are used
        total_tag_used = 0

        # Iterate over each tag to verify if the word we selected matches the tag form the sentences
        for single_tag in home_word_tags:

            # Is our tag is in the list of tags of the sentence? 
            if(single_tag in list_sents_set):

                # Keep track of the count of match
                total_tag_used = total_tag_used + 1

            # If the sentence has atleast 5 or more tags, then print the entire sentence
            if(total_tag_used >= 5):
                print("Sentence with 5 or more tags from home_word_tags: \n", single_sentence, '\n\n')

        
    
        
    






def question(questionNum):
    print("Question {}".format(questionNum))

    globals()["question"+str(questionNum)]()
    print("")


def main():
    question(1)
    question(2)
    question(3)
    question(4)
    question(5)
    question(6)
    question(7)


if __name__ == "__main__":
    main()
