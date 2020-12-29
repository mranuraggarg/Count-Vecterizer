class CountVectorizer:
    """
    Class CountVectorizer:
        cut the sequence into pieces and increment the
        value on the corresponding index in the vector.
    """

    # It will count the number of repeated objects in a list and return a dictionary

    from collections import Counter

    def __init__(self, ngram_size: int):
        # Size of token
        self.ngram = ngram_size
        self.fit_dictionary = {}
        self.fit_sequence = []
        self.transform_matrix = []

    '''
    Method fit():
    Takes the corpus as in input
    build a dictionary "token to index" from the input
    corpus and save it as an attribute of the class;
    '''

    def fit(self, corpus):
        """

        @type corpus: list
        """
        self.fit_dictionary = {}
        fit_set = {}
        for word in corpus:
            sequence = {word[i:i + self.ngram] for i in range(len(word) - self.ngram + 1)}
            fit_set = set.union(sequence, fit_set)

        fit_seq = list(fit_set)
        fit_seq.sort()
        i = 0
        for word in fit_seq:
            if word not in self.fit_dictionary:
                self.fit_dictionary[word] = i
                i += 1
        return None

    '''
    Method transform:
    it takes a new corpus as a input
    transform a new corpus based on a saved dictionary,
    should return a list of lists. If some token from the new corpus
    is not represented in the dictionary, then you need to ignore it;
    It returns a list of lists as a output
    '''

    def transform(self, corpus):
        self.fit_sequence = []
        self.transform_matrix = []
        self.transform_matrix = []
        for row in range(len(corpus)):
            self.transform_matrix.append([0 for _ in range(len(self.fit_dictionary))])
        len(self.transform_matrix)
        for word in corpus:
            sequence = [word[i:i + self.ngram] for i in range(len(word) - self.ngram + 1)]
            self.fit_sequence.append(sequence)

        m = -1
        for array in self.fit_sequence:
            m += 1
            n = 0
            a = dict(self.Counter(array))
            for word in self.fit_dictionary.keys():
                if word not in array:
                    self.transform_matrix[m][n] = 0
                else:
                    self.transform_matrix[m][n] += a[word]
                n += 1
        return self.transform_matrix

    '''
    Method fit_transform:
    It takes a corpus as an input
    fit and transform on the same corpus, return a list of lists.
    '''

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)
