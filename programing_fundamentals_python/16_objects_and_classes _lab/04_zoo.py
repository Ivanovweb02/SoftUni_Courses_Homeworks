class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
       result = ""
       if species == 'mammal':
           result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
       elif species == 'fish':
           result += f"Fishes in {self.name}: {', '.join(self.fish)}"
       elif species == 'bird':
           result += f"Birds in {self.name}: {', '.join(self.birds)}"

       result += f"\nTotal animals: {self.__animals}"
       return result


zoo_name = input()
zoo = Zoo(zoo_name)
number_of_animals = int(input())

for _ in range(number_of_animals):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
