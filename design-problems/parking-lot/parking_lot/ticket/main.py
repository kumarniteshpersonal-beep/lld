class Ticket:
    def __init__(self, ticket_id, vehicle, start_time):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.start_time = start_time
        self.end_time = None

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_parking_duration(self):
        if self.end_time is None:
            raise ValueError("End time is not set")
        return self.end_time - self.start_time

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Vehicle: {self.vehicle.get_license_plate()}, Start Time: {self.start_time}, End Time: {self.end_time}"