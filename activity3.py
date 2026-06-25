class parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

ob = parrot("pigeon", 12)
woo = parrot("woo", 13)

print("blue is a {}".format(ob.species))
print("woo is also a {}".format(woo.species))

print("{} is {} years old".format(ob.name, ob.age))
print("{} is {} years old".format(woo.name, woo.age))