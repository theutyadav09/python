class person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hi, im {self.name} ")


person1 = person("utkarsh yadav")
print(person1.name)
person1.talk()