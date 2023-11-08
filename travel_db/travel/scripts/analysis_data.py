import os
import random
from faker import Faker
import mysql.connector
from travel.models import VisitingData, TravelsData, SeasonsData

fake = Faker()

def insert_visiting_data(cursor):
    place = fake.city()
    population = random.randint(1000, 1000000)
    
    visiting_data = VisitingData(place=place, population=population)
    visiting_data.save()

def insert_travels_data(cursor):
    travels = fake.company()
    population = random.randint(1000, 1000000)
    
    travels_data = TravelsData(travels=travels, population=population)
    travels_data.save()

season_names = ['Summer', 'Winter', 'Spring', 'Autumn', 'Fall', 'Monsoon']

def insert_seasons_data(cursor):
    season = random.choice(season_names)
    population = random.randint(1000, 1000000)
    
    seasons_data = SeasonsData(season=season, population=population)
    seasons_data.save()

def run():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Vidhita2601',
        database='project',
    )

    cursor = conn.cursor()
    
    num_records_to_generate = 100  # Adjust this number as needed

    for _ in range(num_records_to_generate):
        insert_visiting_data(cursor)
        insert_travels_data(cursor)
        insert_seasons_data(cursor)
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    run()
