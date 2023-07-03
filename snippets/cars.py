class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialise attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		#Return long_name value
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set odometer reading to the given value.
		   Reject the change if it attempts to roll the odometer back."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("\nYou can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		if miles < 0:
			print(f"Negative miles cannot be added!")
		else:
			self.odometer_reading += miles

#Represent new car using Car class into a variable
my_new_car = Car('audi', 'a4', 2019)
#Print the returned long_name value using variable and get_descriptive_name()
print(my_new_car.get_descriptive_name())
#Set intial odometer value using Car attribute odometer.reading
my_new_car.odometer_reading = 23
#Display odometer value using read_odometer method
my_new_car.read_odometer()
#Update odometer using Car.update_odometer method
my_new_car.update_odometer(400)
#Display new odometer reading
my_new_car.read_odometer()
#Update using negative value to rollback odometer
my_new_car.update_odometer(-350)
print("\n")