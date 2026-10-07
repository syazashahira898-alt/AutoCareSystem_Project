class Vehicle:

    def __init__(
        self,
        owner_name,
        phone,
        vehicle_number,
        model,
        service_total=0
    ):
        self.owner_name = owner_name
        self.phone = phone
        self.vehicle_number = vehicle_number
        self.model = model
        self.service_total = service_total

    def __str__(self):
        return (
            f"Owner Name: {self.owner_name}\n"
            f"Phone: {self.phone}\n"
            f"Vehicle Number: {self.vehicle_number}\n"
            f"Vehicle Model: {self.model}\n"
            f"Service Total: RM{self.service_total:.2f}"
        )

    def __add__(self, other):
        return self.service_total + other.service_total


class PremiumVehicle(Vehicle):

    def premium_service(self):
        return "Premium Priority Service"