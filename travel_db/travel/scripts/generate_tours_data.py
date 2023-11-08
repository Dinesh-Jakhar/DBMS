import os
import random
from faker import Faker
import mysql.connector
from travel.models import Tours  # Import the Tours model from your Django app

fake = Faker()

# Create a list of example tourist places
tourist_places = [
    "Eiffel Tower, Paris",
    "The Colosseum, Rome",
    "Machu Picchu, Peru",
    "Great Wall of China",
    "Pyramids of Giza, Egypt",
    "Taj Mahal, India",
    "Christ the Redeemer, Brazil",
    "Petra, Jordan",
    "Santorini, Greece",
    "Venice, Italy",
    "Angkor Wat, Cambodia",
    "Safari in Serengeti, Tanzania",
    "Iguazu Falls, Argentina/Brazil",
    "Grand Canyon, USA",
    "The Louvre, Paris",
    "Sagrada Familia, Spain",
    "Acropolis, Athens",
    "Museum of Modern Art, New York",
    "Museum of Fine Arts, Boston",
    "Victoria Falls, Zambia/Zimbabwe",
    "Chichen Itza, Mexico",
    "The Great Barrier Reef, Australia",
    "The Alhambra, Spain",
    "Sistine Chapel, Vatican City",
    "Edinburgh Castle, Scotland",
    "St. Peter's Basilica, Vatican City",
    "The Shard, London",
    "Potala Palace, Tibet",
    "The Palace of Versailles, France",
    "Blue Lagoon, Iceland",
    "Banff National Park, Canada",
    "Antelope Canyon, USA",
    "Uluru, Australia",
    "Mount Everest, Nepal/Tibet",
    "Mesa Verde National Park, USA",
    "Mystic Seaport, USA",
    "Niagara Falls, USA/Canada",
    "Red Square, Russia",
    "Bora Bora, French Polynesia",
    "Mount Kilimanjaro, Tanzania",
    "Mont Saint-Michel, France",
    "The White House, USA",
    "Times Square, New York",
    "Yellowstone National Park, USA",
    "Dubai Mall, UAE",
    "Table Mountain, South Africa",
]

def tours_data(cursor):
    location = fake.city()
    
    # Select a random set of tourist places from the list
    num_selected_places = random.randint(2, 5)
    selected_places = random.sample(tourist_places, num_selected_places)
    touristplces_covered = ', '.join(selected_places)
    
    hotel = fake.company()
    cost = f"${random.randint(100, 1000)}"

    # Generate and insert a random Tours record using SQL
    sql = "INSERT INTO Tours (location, touristplces_covered, hotel, cost) VALUES (%s, %s, %s, %s)"

    # Execute the SQL statement
    cursor.execute(sql, (location, touristplces_covered, hotel, cost))

def run():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Vidhita2601',
        database='project',
    )

    cursor = conn.cursor()
    num_tours_to_generate = 100  # Adjust this number as needed
    for _ in range(num_tours_to_generate):
        tours_data(cursor)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    run()
