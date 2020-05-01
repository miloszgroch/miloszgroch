class Zamiana(object):
    def RomanInt(self,s):
        rom = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        x=0
        n=0
        while x < len(s):
            if x +1 <len(s) and s[x:x+2] in rom:
                n+=rom[s[x:x+2]]
                x+=2
            else:
                n+=rom[s[x]]
                x+=1
        return n
    def IntRoman(self,s):
        introm = {1000:'M',900:'MC',500:'D',400:'DC',100:'C',90:'CX',50:'L',40:'LX',10:'X',9:'XI',5:'V',4:'VI',1:'I'}  
        n=''
        przeskok=10
        for x in range(len(str(s))):
            if s%przeskok == 0:
                przeskok = przeskok*10
                continue
            while s%przeskok not in introm:
                n = n + introm[przeskok/10]
                s = s - przeskok/10
            n = n + introm[s%przeskok]
            s = s - s%przeskok
            przeskok = przeskok*10
        return n[::-1]

if __name__ == '__main__':
    test=Zamiana()
    
