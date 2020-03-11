from __future__ import division
import nltk, re, pprint

from urllib.request import urlopen

#from nltk import book

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import abc

from nltk.stem import WordNetLemmatizer

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'


def question1():

    # Use the Brown Corpus.

    # Which "nouns/tokens" are "more common" in their "plural form"," rather than" their "singular form" 

    # (Use the parts of speech tags NN and NNS in the corpus to identify plural versus singular nouns 

    # and use nltk.WordNetLemmatizer() to get the singular form of a noun from its plural form).

    # What is the second most frequent plural noun that features this property?


    # WordNet lemmatizer initialization
    wnl = nltk.WordNetLemmatizer()

    # Tagged words of Brown for the Part of Speech
    brown_tag = brown.tagged_words()

    # Normalize each word into lowercase 
    brown_tag_nouns = [(word.lower(), tag) for (word, tag) in brown_tag  if tag == 'NN' or tag == 'NNS']

    # For each word, get the frequency distribution tagged with NN
    nn_freq = nltk.FreqDist([(word) for (word, tag) in brown_tag_nouns if tag == 'NN'])

    # For each word, get the frequency distribution tagged with NNS
    nns_freq = nltk.FreqDist([(word) for (word, tag) in brown_tag_nouns if tag == 'NNS'])

    # create a dictionary to store the rank
    rank = {}

    # For each NNS word, loop and check if this word exists in NN
    for nns_word in nns_freq:
        
        # Lemmatize the word so that we can compare it with NN
        nns_word_lemma = wnl.lemmatize(nns_word)

        # For each NN word, loop and check if this word match with lematized NNS
        for nn_word in nn_freq:

            # if lematized NNS and NN words match AND if the FreqDist of NNS is greater than NN
            if((nns_word_lemma == nn_word) and (nns_freq[nns_word] > nn_freq[nn_word])):
                # print("match: ","(NNS = ", nns_word, ") - " , nns_word_lemma , " = " , nn_word)
                # print("count: ", nns_freq[nns_word] , nn_freq[nn_word])
                
                # Store the value in the rank dictionary 
                rank[nns_word] = nns_freq[nns_word]

    # Since dictionary are not ordered by default, we will sort them by the "value" of each word
    rank_sorted = sorted(rank, key=rank.get, reverse=True)

    # Print the entire dictionary
    print("Dictionary of rank is: \n", rank, "\n")

    # Print the second most frequent plural noun
    print("Second most frequent plural noun is ", rank_sorted[1])







def question2():
    
    # Use the Brown Corpus.

    # List the 5 most frequent tags in order of decreasing frequency. 

    # What do the tags represent?

    brown_tag = brown.tagged_words()

    brown_tag_freq = nltk.FreqDist([(b) for (a,b) in brown_tag])

    print("Five most frequent tags are: ", brown_tag_freq.most_common(5))



def question3():

    # Which three tags precede nouns tagged with the 'NN' tag most commonly? 

    # What do these three tags represent? 

    # Report your findings separately for the following categories of Brown corpus: humor, romance, government


    def tags_precede_nouns(category):

        print("**** Three tags precede nouns in category: ", category, "****")   

        # Tag the words in Brown Corpus for the given category
        brown_tag = brown.tagged_words(categories = category)

        # Get the index, word, and tag for each word in Brown Corpus tagged with NN for a given category
        brown_tag_nn = [(i,(a,b)) for (i, (a,b)) in enumerate(brown_tag) if b == 'NN']

        # Get the preceding word and tag that follows NN
        brown_tag_precede_nn = [(brown_tag[i-1])  for (i, (a,b)) in brown_tag_nn]

        # List the tags as Frequency Distribution
        FreqDist = nltk.FreqDist([(b) for (a,b) in brown_tag_precede_nn])

        # Print the Freq Dist for each of the preceding tags
        print(FreqDist.most_common(3),  '\n\n')

    tags_precede_nouns('humor')
    tags_precede_nouns('romance')
    tags_precede_nouns('government')





def question4():

    # In the “Combining Taggers” Subsection of Section 5.5 of the textbook, an example of a backoff tagger is provided. 
     
    # Extend that example by defining a TrigramTagger called t3 which backs off to t2. 
     
    # Train this tagger on all of the sentences from the Brown corpus with the category news. 
     
    # Then evaluate your tagger using “evaluate” function on all of the sentences from the Brown corpus with the category lore. 
    
    # Report the number. 
      
    # How does this number compare to when this tagger is evaluated on all of the sentences from the Brown corpus with the category news?


    # Tagged sents for news category in Brown Corpus
    brown_news = brown.tagged_sents(categories = 'news')

    # Tagged sents for lore category in Brown Corpus
    brown_lore = brown.tagged_sents(categories = 'lore')

    # Brown news as train set
    train_sents = brown_news

    # Brown lore as test set
    test_sents = brown_lore

    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff = t0)
    t2 = nltk.BigramTagger(train_sents, backoff = t1)
    t3 = nltk.TrigramTagger(train_sents, backoff = t2)

    # Evaluate the t3 tagger with Brown lore tagged sentences
    print("brown_lore: ", t3.evaluate(test_sents))

    # Evaluate the t3 tagger with Brown news tagged sentences
    print("brown_news: ", t3.evaluate(train_sents))

 




def question5():

    # Provide the output of your tagger from the previous question on the 200th sentence of the lore category 
    # of the Brown Corpus (note that brown.sents(categories='lore')[199] produces the 200th sentence).

    # Would you tag this sentence in the same manner? Why?

    # Tagged sents for news category in Brown Corpus
    brown_news = brown.tagged_sents(categories='news')
   
    # Tagged sents for lore category in Brown Corpus
    brown_lore = brown.sents(categories='lore')

     # Brown news as train set
    train_sents = brown_news

    # Brown lore as test set for 200th sentence
    test_sents = brown_lore[199]

    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    t3 = nltk.TrigramTagger(train_sents, backoff=t2)

    # Report the brown_lore 200th sentence
    print("brown_lore: ", t3.tag(test_sents))



def question6():

    # Compare the given TrigramTagger from the previous questions with a TrigramTagger where no backoff is provided. 

    # Train this tagger on all of the sentences from the Brown corpus with the category news. 
     
    # Then evaluate your tagger using “evaluate” function on all of the sentences from the Brown corpus with the category lore.

    # Report the numbers. Which tagger performs better? Why?



    # Tagged sents for news category in Brown Corpus
    brown_news = brown.tagged_sents(categories='news')
    
    # Tagged sents for lore category in Brown Corpus
    brown_lore = brown.tagged_sents(categories='lore')
    
    # Brown news as train set
    train_sents = brown_news
    
    # Brown lore as train set
    test_sents = brown_lore

    # t3 tagger with no backoffs to bigram/unigram
    t3 = nltk.TrigramTagger(train_sents)

    # Evaluate lore category to the traned sentences of news
    print("brown_lore: ", t3.evaluate(test_sents))

    # Evaluate news category to the traned sentences of news
    print("brown_news: ", t3.evaluate(train_sents))



def question7():

    # The majority of WordNet's senses are marked by five POS categories: 
    # noun (n), verb (v), adjective (a), adverb (r), and satellite adjectives (s). 

    # Provide the percentage of words from the WordNet corpus that have senses in more than one of these categories. 

    # For example, type has senses which connect to both “noun” and “verb” POS (positive case), 
    # whereas typewriter has only senses which connect to “noun” POS (negative case).

    # Note that, for instance, the following code

    # from nltk.corpus import wordnet

    # wordnet.synsets("cat","n")

    # will return you all the senses of word "cat" that are nouns.


    def highcount():
        # Create a list for POS categories to check the words upon
        pos_categories = ["n","v","a","r","s"]

        # Create a dictionary of words
        words = wn.words()

        #total number of words
        total_words = 0

        #number of words with 1 or more tenses
        multiple_senses_count = 0

        selected_word_list = []

        # For each word in wordnet dictionary
        for word in words:

            # Increment the total count
            total_words+=1

            #pos_categories
            count = 0

            # check in all pos_categories
            for single_pos in pos_categories:
                if wn.synsets(word,single_pos):
                    count+=1
            if count > 1:
                # Increment the multiple_senses_count
                multiple_senses_count+=1
                selected_word_list.append(word)

        print("wordnet_word_count: ", total_words)
        print("matched words: ", multiple_senses_count)
        
        percentage = (multiple_senses_count/total_words)*100

        print("\npercentage(rounded 4 decimal) = ", round(percentage,4))

        return selected_word_list

    highcount()



    def lowcount():

        # Initialize variables for count
        wordnet_word_count = 0
        sense_count = 0  
        multiple_senses_count = 0
        selected_word_list = []


        # Create a wordnet list
        wn_words = [word.lower() for word in wn.words()]

        # Create a dictionary for POS categories to check the words upon
        pos_dict = {'n', 'v', 'a', 'r', 's'}

        # For each words in WordNet corpus
        for word in wn_words:

            # Track the word counts for WordNet
            wordnet_word_count = wordnet_word_count + 1

            # Store the lenght of total senses for the single word
            len_pos = len(wn.synsets(word))

            # Create empty pos_tag list to store the category
            pos_tag = []

            # Loop over the total count of the senses to get a distinct number of categories, eg: {'n', 'a', 'v'}
            for sense_count in range(len_pos):

                # for each senses of the word, find the POS category
                single_pos_tag = wn.synsets(word)[sense_count].pos()
                
                # Store the POS category into the pos_tag list
                pos_tag.append(single_pos_tag)

            # Get the distinct set of categories from the pos_tag list    
            pos_tag_set = set(pos_tag)

            # Store the length of the distinct POS category
            pos_match_len = len(pos_tag_set & pos_dict)

            # Since we only want senses in more than one of categories, filter pos_match_len > 1
            if(pos_match_len > 1):
                # print("WordNet Word: ", word)  
                # print("Word synset: ", wn.synsets(word)) 
                # print("All pos_tag_set: ", pos_tag) 
                # print("Distinct pos_tag_set: ", pos_tag_set)
                # print("Matched tags: ", pos_tag_set & pos_dict)
                # print("POS match length: ", pos_match_len)

                selected_word_list.append(word)

                # Start counting the words from the WordNet corpus that 
                # have senses in more than one of the {'n', 'v', 'a', 'r', 's'} categories.
                multiple_senses_count = multiple_senses_count + 1

                print("multiple_senses_count: ", multiple_senses_count, '\n\n\n')
        print("wordnet_word_count: ", wordnet_word_count)

        percentage = (multiple_senses_count/wordnet_word_count)*100

        print("\npercentage(rounded 4 decimal) = ", round(percentage,4))

        return selected_word_list
    

    highcount()

    highcount_len = len(highcount())
    lowcount_len = len(lowcount())



    print("\n\n\ndiff: ", list(set(highcount()) - set(lowcount())),"\n\n\n")
    print("\n\n\nlen 1: ", highcount_len - lowcount_len,"\n\n\n")
    print("\n\n\nlen 2: ", lowcount_len - highcount_len ,"\n\n\n")




def question(questionNum):
    print("Question {}".format(questionNum))

    globals()["question"+str(questionNum)]()
    print("")


def main():
    # question(1)
    # question(2)
    # question(3)
    # question(4)
    # question(5)
    # question(6)
    question(7)


if __name__ == "__main__":
    main()

