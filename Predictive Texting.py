import numpy as np

class Trigram_Language_Model:

    def __init__(self):
        
        self.conditional_distribution = None
        
    def train(self, corpus_file_name):

        # Create an empty dictionary object to count word frequencies
        conditional_frequencies = dict()

        with open (corpus_file_name) as file:
            words = [i.strip ().lower () for i in file.read ().split () ]
        
        bigrams = []
        
        for i in range (len (words)-1):
            bigrams.append (words [i] + " " + words [i+1])
            
        bigrams = list (set (bigrams))
        
        conditional_frequencies = {i : {} for i in bigrams}
        
        for i in range (len (words)-2):
            try:
                conditional_frequencies [words [i] + " " + words [i+1]] [words [i+2]] += 1
            except:
                conditional_frequencies [words [i] + " " + words [i+1]] [words [i+2]] = 1
                
        self.conditional_distribution = {i:{j:(conditional_frequencies [i][j])/sum (conditional_frequencies [i].values ()) for j in conditional_frequencies [i]} for i in conditional_frequencies}
    
    def generate_sentence(self, start_word):

        sentence = []

        bigram_1 = ('<s>', start_word)
        
        # ADD CODE HERE
        sentence = ['<s>', start_word]
        while sentence [-1] != '</s>':
            last_words = sentence [-2] + " " + sentence [-1]
            keys =  list(self.conditional_distribution [last_words].keys ())
            values =  list(self.conditional_distribution [last_words].values())
            #print (keys, values)
            next_word = np.random.choice (keys, 1, p=values)
            sentence.append  (next_word [0])
        return " ".join (sentence [1:-1])

lm = Trigram_Language_Model()
lm.train('sentences_long.txt')

#Sample Usage
print (lm.generate_sentence ("birds"))
print (lm.generate_sentence ("philosophy"))
print (lm.generate_sentence ("blood"))
print (lm.generate_sentence ("fridge"))
print (lm.generate_sentence ("blame"))
print (lm.generate_sentence ("the"))
