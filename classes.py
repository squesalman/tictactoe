class Flight():
  def __init__(self,capacity):
    self.capacity = capacity
    self.passenger = []

  #method to add passenger and check if its exceed capacity
  def add_passenger(self,name):
      if not self.open_seats():
        return False
      self.passenger.append(name)
      return True

  def open_seats(self):
    return self.capacity - len(self.passenger)

flight = Flight(3)
people = ["Harry","Hermione","Ron","ginny"]

for person in people:
  if flight.add_passenger(person):
    print(f"passenger {person} added")
  else:
    print(f"{person} cannot be added")