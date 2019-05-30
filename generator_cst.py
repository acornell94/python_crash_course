class Sentence:
    """Create an iterator to loop through words in a sentence."""

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def sentence(sentence):
    """Create a generator function to loop through words in a sentence."""
    for word in sentence.split():
        yield word


my_sentence = Sentence('this is a sentence')

for word in my_sentence:
    print(word)

my_sentence2 = sentence('this is also a sentence')

for word in my_sentence2:
    print(word)