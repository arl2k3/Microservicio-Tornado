from tornado.web import RequestHandler, Application  
from tornado.escape import json_decode 
from controllers.pet_controller import PetController
from controllers.appointment_controller import AppointmentController

class PetHandler(RequestHandler):
    def initialize(self):
        self.controller = PetController()

    def get(self, pet_id=None):
        if pet_id:
            pet = self.controller.get_pet(int(pet_id))
            if pet:
                self.write(pet) 
            else:
                self.set_status(404)
                self.write({"error": "Mascota no encontrada"})
        else:
            pets = self.controller.list_pets()
            self.write({"pets": pets}) 

    def post(self):
        data = json_decode(self.request.body)
        pet_id = self.controller.create(data['name'], data['species'], data['age'])
        self.write({
            "message": "Mascota creada",
            "pet": {
                "id": pet_id,
                "name": data['name'],
                "species": data['species'],
                "age": data['age']
            }
        })

    def put(self, pet_id):
        data = json_decode(self.request.body)
        self.controller.update(int(pet_id), data['name'], data['species'], data['age'])
        updated_pet = self.controller.get_pet(int(pet_id))
        self.write({
            "message": "Mascota actualizada",
            "pet": updated_pet
        })

    def delete(self, pet_id):
        self.controller.delete(int(pet_id))
        self.write({"message": "Mascota eliminada"})

class AppointmentHandler(RequestHandler):
    def initialize(self):
        self.controller = AppointmentController()

    def get(self, pet_id=None):
        if pet_id:
            appointments = self.controller.get_appointments_by_pet(int(pet_id))
            self.write({'appointments': appointments})
        else:
            appointments = self.controller.list_appointments()
            self.write({'appointments': appointments})

    def post(self):
        data = json_decode(self.request.body)
        appointment_id = self.controller.create(data['date'], data['reason'], data['pet_id'])
        self.write({'message': 'Cita médica creada', 'id': appointment_id})

    def put(self, appointment_id):
        data = json_decode(self.request.body)
        self.controller.update(int(appointment_id), data['date'], data['reason'], data['pet_id'])
        self.write({'message': 'Cita médica actualizada'})

    def delete(self, appointment_id):
        self.controller.delete(int(appointment_id))
        self.write({'message': 'Cita médica eliminada'})

def make_app():
    return Application([
        (r"/pets", PetHandler),
        (r"/pets/(\d+)", PetHandler),
        (r"/appointments", AppointmentHandler),
        (r"/appointments/(\d+)", AppointmentHandler),
    ])