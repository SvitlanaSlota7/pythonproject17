class Animal:
    def talk(self):
        # Цей метод буде перевизначений у нащадках
        raise NotImplementedError("Subclasses must implement abstract method")

class Dog(Animal):
    def talk(self):
        print("Woof woof!")

class Cat(Animal):
    def talk(self):
        print("Meow!")

def animal_talk(animal_instance):
    """
    Приймає об'єкт будь-якої тварини і викликає його метод talk.
    """
    animal_instance.talk()


if __name__ == "__main__":
    my_dog = Dog()
    my_cat = Cat()

    print("Dog says: ", end="")
    animal_talk(my_dog)

    print("Cat says: ", end="")
    animal_talk(my_cat)