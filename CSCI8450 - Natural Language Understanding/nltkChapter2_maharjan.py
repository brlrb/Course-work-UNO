import nltk, re, pprint

from nltk.book import *

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords




def question1():

    # get the length of word tokens
    persuasion_word_token_length = len(nltk.corpus.gutenberg.words('austen-persuasion.txt'))
    print(persuasion_word_token_length)






def question2():

    # get the length of word types
    persuasion_word_token_length = nltk.corpus.gutenberg.words('austen-persuasion.txt')
    persuasion_word_token_type = len(set(persuasion_word_token_length))
    print(persuasion_word_token_type)





def question3():

    print("Pair 1: Paper Book")
    paper = wn.synsets('paper')
    paper = wn.synset('paper.n.01')
    print("member_meronyms: ", paper.member_meronyms())
    print("part_meronyms", paper.part_meronyms())
    print("substance_meronyms", paper.substance_meronyms())
    print("member_holonyms", paper.member_holonyms())
    print("part_holonyms", paper.part_holonyms())
    print("substance_holonyms", paper.substance_holonyms())
    print("")

    print("Pair 2: Word Letter")
    word = wn.synsets('word')
    word = wn.synset('word.n.01')
    print("member_meronyms: ", word.member_meronyms())
    print("part_meronyms", word.part_meronyms())
    print("substance_meronyms", word.substance_meronyms())
    print("member_holonyms", word.member_holonyms())
    print("part_holonyms", word.part_holonyms())
    print("substance_holonyms", word.substance_holonyms())
    print("")

    print("Pair 3: Wheel Automobile")
    wheel = wn.synsets('wheel')
    wheel = wn.synset('wheel.n.01')
    print("member_meronyms: ", wheel.member_meronyms())
    print("part_meronyms", wheel.part_meronyms())
    print("substance_meronyms", wheel.substance_meronyms())
    print("member_holonyms", wheel.member_holonyms())
    print("part_holonyms", wheel.part_holonyms())
    print("substance_holonyms", wheel.substance_holonyms())
    print("")

    print("Pair 4: Disk Computer")
    disk = wn.synsets('disk')
    disk = wn.synset('disk.n.01')
    print("member_meronyms: ", disk.member_meronyms())
    print("part_meronyms", disk.part_meronyms())
    print("substance_meronyms", disk.substance_meronyms())
    print("member_holonyms", disk.member_holonyms())
    print("part_holonyms", disk.part_holonyms())
    print("substance_holonyms", disk.substance_holonyms())
    print("")

    print("Pair 5: Coffee Beans")
    coffee = wn.synsets('coffee')
    coffee = wn.synset('coffee.n.01')
    print("member_meronyms: ", coffee.member_meronyms())
    print("part_meronyms", coffee.part_meronyms())
    print("substance_meronyms", coffee.substance_meronyms())
    print("member_holonyms", coffee.member_holonyms())
    print("part_holonyms", coffee.part_holonyms())
    print("substance_holonyms", coffee.substance_holonyms())
    print("")

    print("Pair 6: Bee Honey")
    bee = wn.synsets('bee')
    bee = wn.synset('bee.n.01')
    print("member_meronyms: ", bee.member_meronyms())
    print("part_meronyms", bee.part_meronyms())
    print("substance_meronyms", bee.substance_meronyms())
    print("member_holonyms", bee.member_holonyms())
    print("part_holonyms", bee.part_holonyms())
    print("substance_holonyms", bee.substance_holonyms())
    print("")

    print("Pair 7: Pen Ink")
    pen = wn.synsets('pen')
    pen = wn.synset('pen.n.01')
    print("member_meronyms: ", pen.member_meronyms())
    print("part_meronyms", pen.part_meronyms())
    print("substance_meronyms", pen.substance_meronyms())
    print("member_holonyms", pen.member_holonyms())
    print("part_holonyms", pen.part_holonyms())
    print("substance_holonyms", pen.substance_holonyms())
    print("")

    print("Pair 8: Ball Game")
    ball = wn.synsets('ball')
    ball = wn.synset('ball.n.01')
    print("member_meronyms: ", ball.member_meronyms())
    print("part_meronyms", ball.part_meronyms())
    print("substance_meronyms", ball.substance_meronyms())
    print("member_holonyms", ball.member_holonyms())
    print("part_holonyms", ball.part_holonyms())
    print("substance_holonyms", ball.substance_holonyms())
    print("")

    print("Pair 9: Happiness Expression")
    happiness = wn.synsets('happiness')
    happiness = wn.synset('happiness.n.01')
    print("member_meronyms: ", happiness.member_meronyms())
    print("part_meronyms", happiness.part_meronyms())
    print("substance_meronyms", happiness.substance_meronyms())
    print("member_holonyms", happiness.member_holonyms())
    print("part_holonyms", happiness.part_holonyms())
    print("substance_holonyms", happiness.substance_holonyms())
    print("")

    print("Pair 10: Car Drive")
    car = wn.synsets('car')
    car = wn.synset('car.n.01')
    print("member_meronyms: ", car.member_meronyms())
    print("part_meronyms", car.part_meronyms())
    print("substance_meronyms", car.substance_meronyms())
    print("member_holonyms", car.member_holonyms())
    print("part_holonyms", car.part_holonyms())
    print("substance_holonyms", car.substance_holonyms())
    print("")







def question4():

    # Get a distinct set on each text
    # Then the words that occurs on both the text1 and text7 
    common_text1_text7 = set(text1) & set(text7)
    print("--- word 1 ---- ")
    print("text 1: ")
    print(text1.concordance("permanent"))
    print("text 7: ")
    print(text7.concordance("permanent"))
    print(" ")


    print("--- word 2 ---- ")
    print("text 1: ")
    print(text1.concordance("war"))
    print("text 7: ")
    print(text7.concordance("war"))
    print(" ")


    print("--- word 3 ---- ")
    print("text 1: ")
    print(text1.concordance("bids"))
    print("text 7: ")
    print(text7.concordance("bids"))
    print(" ")


    print("--- word 4 ---- ")
    print("text 1: ")
    print(text1.concordance("illness"))
    print("text 7: ")
    print(text7.concordance("illness"))









def question5():
    modal_distribution = nltk.ConditionalFreqDist((genre,word)for genre in brown.categories() for word in brown.words(categories=genre))
    genres = ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']


    one = ["who", "what", "when", "where", "why", "how"]
    two = ['can', 'could', 'may', 'might', 'must', 'will']
    three = ['he', 'she', 'it', 'I', 'they', 'you', 'we']


    
    modal_distribution.tabulate(conditions=genres, samples=one)
    print(" ")

    modal_distribution.tabulate(conditions=genres, samples=two)
    print(" ")

    modal_distribution.tabulate(conditions=genres, samples=three)










def question6():

    # Get all Noun
    all_noun = [noun for noun in wn.all_synsets('n')]

    # Get words that has no hyponyms
    no_hyponyms = [noun for noun in wn.all_synsets('n') if len(noun.hyponyms())==0]

    # Find the percentage
    percentage_non_hyponym_noun = (len(no_hyponyms)/len(all_noun)) * 100
    
    # Round it to 2 decimal place
    print(round(percentage_non_hyponym_noun,2))








def question7():

    # get the list of stop words    
    stopwords = nltk.corpus.stopwords.words('english')
    
    # initiliaze empty all_brown_bigrams
    all_brown_bigrams = []
    
    # loop into all brown corpous categories
    for cat in brown.categories():
    
        # create a list of all bigrams with no stopwords and only alphabets
        all_brown_bigrams= all_brown_bigrams + [b for b in nltk.bigrams(brown.words(categories=cat)) if b[0] not in stopwords and b[1] not in stopwords and any(c.isalpha() for c in b[0]) and any(c.isalpha() for c in b[1])]

    # # get the 5 most common bigrams
    print(nltk.FreqDist(all_brown_bigrams).most_common(5))








def question8():

    # create a list of same  lemma that may occur in different synsets
    same_lemma = []

    # total count of data
    total_count = 0

    #total count of polysemy
    count_polysemy = 0
    
    # iterate over all of the wn for noun 
    for synset in wn.all_synsets('n'):
       
        # get each lemmma and ge the name
        for lemma in synset.lemmas():
            lemma_name = lemma.name()
            
            # if the name expsts then do not use
            if lemma_name not in same_lemma:
                same_lemma.append(lemma_name)
                
                # count the polysemy
                count_polysemy = count_polysemy + len(wn.synsets(lemma_name, 'n'))
                
                # all count
                total_count = total_count + 1

    # divide both total and polysemy to get the average
    average_polysemy = count_polysemy / total_count

    # round the result in 2 decimal and print
    print(round(average_polysemy, 2))




def question(questionNum):
    print("Question {}".format(questionNum))

    globals()["question"+str(questionNum)]()
    print("")


def main():
    question(1) # exercise 2
    question(2) # exercise 2
    question(3) # exercise 5
    question(4) # exercise 9
    question(5) # exercise 11
    question(6) # exercise 13
    question(7) # exercise 18
    question(8) # exercise 27


if __name__ == "__main__":
    main()
