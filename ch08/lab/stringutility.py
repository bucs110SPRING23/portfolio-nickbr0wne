class StringUtility:

    def __init__(self,string):
        self.string=string
    def __str__(self):
        return self.string
    def vowels(self):
        vowels='aeiou'
        count=sum(1 for char in self.string if char in vowels)
        if count < 5:
            return str(count)
        else:
            return 'many'
    def bothEnds(self):
        if len(self.string) <3:
            return ''
        return (self.string[0]+self.string[1]+self.string[-2]+self.string[-1])
    def fixStart(self):
        if len(self.string) <=1:
            return self.string
        else:
            return self.string[0]+self.string[1:].replace(self.string[0],'*')
    def asciiSum(self):
        return sum (ord(char) for char in self.string)
    def cipher(self):
        cipher=''
        for char in self.string:
            if char.isalpha():
                shift=len(self.string)
                if char.isupper():
                    base=ord('A')
                else:
                    base=ord('a')
                cipher+=chr((ord(char)-base+shift) %26+base)
            else:
                cipher+=char
        return cipher