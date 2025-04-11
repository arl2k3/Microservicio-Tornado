from services.appointment_service import (
    get_all_appointments, get_appointments_by_pet, create_appointment,
    update_appointment, delete_appointment
)

class AppointmentController:
    def list_appointments(self):
        return get_all_appointments()

    def get_appointments_by_pet(self, pet_id):
        return get_appointments_by_pet(pet_id)

    def create(self, date, reason, pet_id):
        return create_appointment(date, reason, pet_id)

    def update(self, appointment_id, date, reason, pet_id):
        update_appointment(appointment_id, date, reason, pet_id)

    def delete(self, appointment_id):
        delete_appointment(appointment_id)