class Apple:
    STAGES = ["цветение", "зеленое", "красное"]

    def __init__(self, index):
        self.index = index
        self.stage = self.STAGES[0]

    def ripen(self):
        current_stage_index = self.STAGES.index(self.stage)
        if current_stage_index < len(self.STAGES) - 1:
            self.stage = self.STAGES[current_stage_index + 1]

    def is_ripe(self):
        return self.stage == self.STAGES[-1]


class Tree:
    def __init__(self, *apples):
        self.apples = list(apples)

    def grow(self):
        for apple in self.apples:
            apple.ripen()

    def are_all_apples_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def harvest(self):
        if self.are_all_apples_ripe():
            self.apples = []
        else:
            print("Не все яблоки созрели!")


class Gardener:
    def __init__(self, name, *plants):
        self.name = name
        self.plants = list(plants)

    def take_care_of_plants(self):
        for plant in self.plants:
            plant.grow()

    def harvest_all_plants(self):
        for plant in self.plants:
            if isinstance(plant, Tree):
                plant.harvest()
            else:
                print("Для данного растения нет метода сбора урожая.")


# пример использования
apple1 = Apple(1)
apple2 = Apple(2)
apple3 = Apple(3)
tree = Tree(apple1, apple2, apple3)
gardener = Gardener("John", tree)

print("Перед уходом садовника:")
for apple in tree.apples:
    print(f"Яблоко {apple.index} в стадии {apple.stage}")

gardener.take_care_of_plants()
gardener.harvest_all_plants()

print("После работы садовника:")
if tree.apples:
    print("На дереве остались незрелые яблоки.")
else:
    print("Дерево пусто.")
