import requests
import sys
import pandas as pd

#classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"
    
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return f"{self.name} says Meow!"

jerry = Dog(name="Jerry", breed="Labrador")
jerry.bark()

dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", color="Tabby")

print(dog.name)
print(cat.meow())

#try and except
try:
    result = 10 / 0
except:
    print("An error occurred:")


def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")


# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

#working with strings
first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"

star = "*"
stars = star * 10  # "**********"

separator = "-" * 20  # "--------------------"

def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")

# Call with values
introduce("Alice", 25)
introduce("Bob", 30)