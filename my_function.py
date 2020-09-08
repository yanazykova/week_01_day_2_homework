def greet():
    return("Hey!")

print(greet())

def greet(name): 
  return "Hey " + name

greeting = greet("Bob")
print(greeting)

def greet(name, time_of_day):
  return "Good " + time_of_day + ", " + name

greeting = greet('Bob', 'morning')
print(greeting)


def greet(name, time_of_day):
  return "Good " + time_of_day + ", " + name

name_1 = "Bob"
time_of_day_1 = "morning"
greeting = greet(name_1, time_of_day_1)
print(greeting)


name_2 = "Ada"
time_of_day_2 = "afternoon"
greeting = greet(name_2, time_of_day_2)
print(greeting)
