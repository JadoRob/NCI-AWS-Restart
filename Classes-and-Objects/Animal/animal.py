class Animal:
    def __int__(self, breed=None, name=None, size=None, age=None, temperament=None):
        self.breed = breed
        self.name = name
        self.size = size
        self.age = age
        self.temperament = temperament

    def setBreed(self, breed):
        self.breed = breed
    
    def getBreed(self):
        return self.breed

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size