class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old")


def run():

    person = Person('Daniel', 34)
    print('Age {}'.format(person.age))
    person.say_hello()


if __name__ == '__main__':
    run()

