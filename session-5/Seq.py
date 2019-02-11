class Seq:
    def __init__(self,strbase):
        self.strbase=strbase
    def len(self):
        return len(self.strbase)

    def complement(self):
        complement_list = []
        for n in self.strbase:
            if n == "A":
                complement_list.append("T")
            elif n == "T":
                complement_list.append("A")
            elif n == "G":
                complement_list.append("C")
            elif n == "C":
                complement_list.append("G")
        return ','.join (complement_list).replace(",","")

    def reverse(self):
        reverse_list = []
        n = len(self.strbase) - 1
        while n >= 0:
            reverse_list.append(self.strbase[n])
            n -= 1
        return ','.join (reverse_list).replace(",","")

    def count(self, base):
        self.base = base.upper()
        return self.strbase.count(self.base)

    def perc(self, base):
        self.base = base.upper()
        return round(100.0 * self.count(base) / self.len(), 1)


seq1= Seq("AGTCA")
print(seq1.len())
print(seq1.complement())
print(seq1.reverse())
print(seq1.count("a"))
print(seq1.perc("t"))
