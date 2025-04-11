from services.pet_service import (
    get_all_pets, get_pet_by_id, create_pet, update_pet, delete_pet
)

class PetController:
    def list_pets(self):
        return get_all_pets()

    def get_pet(self, pet_id):
        return get_pet_by_id(pet_id)

    def create(self, name, species, age):
        return create_pet(name, species, age)

    def update(self, pet_id, name, species, age):
        update_pet(pet_id, name, species, age)

    def delete(self, pet_id):
        delete_pet(pet_id)