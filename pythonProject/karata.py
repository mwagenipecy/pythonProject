import this

tribes = ["Nyakyusa", "Haya"]
Chaga = ["Shayo", "Kimario", "Shirima", "Temba"]
StartWords = ["Mwa"]


class NameDefiner:

    def __init__(self, name: str):
        self.name = name

    def checker(self):
        length: int = len(self.name)
        if length > 6:
            for wrd in StartWords:
                x: bool = self.name.startswith(wrd)
                if x:
                    print(f"The name {self.name} is probably of {tribes[0]} origin ")

                else:
                    print("Then you are a Haya")


class wordChecker:
    # creating the constructor in django
    def __init__(self, word: str):
        self.word = word

    def checker(self,now):
        this.now=now
        wordlength: int = len(self.word)
        if wordlength > 4:
            print("hellow welcome to....")
            print("hellow welcome to...."+now)


nam = input("enter the name")
wordChecker = wordChecker(nam)
wordChecker.checker("hellow")
