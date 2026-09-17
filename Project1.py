class Pet:
    print("Hello World")

pet_object = Pet()

class PetProfile:
    category = "pet"
    def __init__(self,name,animal_type,age,favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food

pet1 = PetProfile("Rocky","Dog",6,'Steak')
pet2= PetProfile("Linda",'Parrot','3','Green Chilli')

print('Rocky is a {}'.format(pet1.category))
print('Linda is a {}'.format(pet2.category))

print('{} is a {} and is {} years old and loves eating {}.'
.format(pet1.name, pet1.animal_type, 
pet1.age, pet1.favourite_food))


print('{} is a {} and is {} years old and loves eating {}. '
.format(pet2.name, pet2.animal_type,
pet1.age, pet2.favourite_food))
