from abc import ABC


class address(ABC):
    def __init__(self, faddress):
        self.fileaddress = faddress

    def CalculateFreqs(self):
        pass


class ListCalc(address):
    def __init__(self, laddress):
        address.__init__(self, laddress)
        weirdwords = open(self.fileaddress)
        text = weirdwords.readlines()
        weirdwords.close()

        for x in text:
            self.words = x.split()

        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.wordfreq = [0 for y in range (26)]  # Technically speaking, a 2D list with 1 depth is a 1D list

    def CalculateFreqs(self):
        print("Calculating frequency in list approach: ")
        for targetword in self.words:
            tword = targetword
            for letter in tword:
                self.wordfreq[self.alphabet.index(letter)] += 1

        for z in range (len(self.alphabet)):
            print(self.alphabet[z] + ' = ' + str(self.wordfreq[z]))



class DictCalc(address):
    def __init__(self, daddress):
        address.__init__(self, daddress)
        weirdwords = open(self.fileaddress)
        text = weirdwords.readlines()
        weirdwords.close()

        for x in text:
            self.words = x.split()

        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.wordfreq = [0 for y in range(26)]  # I'm just going to zip two lists into a dictionary this time
        self.worddict = {self.alphabet: self.wordfreq for self.alphabet, self.wordfreq in zip(self.alphabet, self.wordfreq)}

    def CalculateFreqs(self):
        print("Calculating frequency in dict approach: ")
        for targetword in self.words:
            tword = targetword
            for letter in tword:
                self.worddict[letter] += 1
        print(self.worddict)


listwords = ListCalc('weirdwords.txt')
listwords.CalculateFreqs()
print()
dictwords = DictCalc('weirdwords.txt')
dictwords.CalculateFreqs()