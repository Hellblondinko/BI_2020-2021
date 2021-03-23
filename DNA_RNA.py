class Dna:

    def __init__(self, sequence=''):
        self.sequence = sequence.lower()
        self.reverse_sequence = ''
        self.counter = 0

    def get_sequence(self):
        return self.sequence

    def set_sequence(self, value):
        self.sequence = value.lower()

    def gc_content(self):
        return (self.sequence.count('g') + self.sequence.count('c')) * 100 / len(self.sequence)

    def reverse_complement(self):
        for ch in self.sequence:
            if ch == 'a':
                self.reverse_sequence += 't'
            elif ch == 't':
                self.reverse_sequence += 'a'
            elif ch == 'g':
                self.reverse_sequence += 'c'
            else:
                self.reverse_sequence += 'g'
        return self.reverse_sequence

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.sequence):
            ret = self.sequence[self.counter]
            self.counter += 1
            return ret
        else:
            raise StopIteration

    def __eq__(self, other):
        return self.sequence == other.sequence

    def __hash__(self):
        return hash(self.sequence)

    def transcribe(self):
        return self.sequence.lower().replace('t', 'u')


class Rna:
    def __init__(self, sequence=''):
        self.sequence = sequence.lower()
        if self.sequence.count('t') != 0:
            print('��� ���!')
        self.reverse_sequence = ''
        self.counter = 0


    def get_sequence(self):
        return self.sequence

    def set_sequence(self, value):
        self.sequence = value.lower()

    def gc_content(self):
        return (self.sequence.count('g') + self.sequence.count('c')) * 100 / len(self.sequence)

    def reverse_complement(self):
        for ch in self.sequence:
            if ch == 'a':
                self.reverse_sequence += 'u'
            elif ch == 'u':
                self.reverse_sequence += 'a'
            elif ch == 'g':
                self.reverse_sequence += 'c'
            else:
                self.reverse_sequence += 'g'
        return self.reverse_sequence

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.sequence):
            ret = self.sequence[self.counter]
            self.counter += 1
            return ret
        else:
            raise StopIteration

    def __eq__(self, other):
        return self.sequence == other.sequence

    def __hash__(self):
        return hash(self.sequence)


if __name__ == '__main__':
    dna_o = Dna('atgc')
    dna_o2 = Dna('atgc')
    res = set()
    res.add(dna_o)
    res.add(dna_o2)
    print(len(res))
    print(dna_o.gc_content())
