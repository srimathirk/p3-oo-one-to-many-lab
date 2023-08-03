#Define a Pet and pass into the constructor its name, pet_type and an optional owner
class Pet:

    #Define a class variable PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] 
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    #Define a class variable all that stores all instances of the Pet class.
    all = []
       
    def __init__(self, name, pet_type,owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        #and validate that the pet_type is one of those types in the __init__ method.raise Exception if this check fails.
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet types")
        # append all pets
        Pet.all.append(self)

#Define an Owner class and pass into the constructor a name argument.
    
class Owner:
    def __init__(self,name):
        self.name = name

    #In the Owner class write a method called pets(self) that returns a full list of the owner's pets.
    def pets(self):
        pet = [pet for pet in Pet.all]
        return pet

    #In the Owner class write a method called add_pet(self, pet) that checks that the the pet is of type Pet and adds the owner to the pet.
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    #In the Owner class write a method called sort_pets_by_name(self) returns a sorted list of pets by their names.
    def get_sorted_pets(self):
        after_sort = sorted(self.pets(),key=lambda pet:pet.name )
        return after_sort