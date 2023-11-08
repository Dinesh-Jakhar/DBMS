import random
from faker import Faker
import mysql.connector


fake = Faker()

# Create a list to store generated city names
city_names = []

def touristplaces(cursor, city_names):
    place = fake.city()
    cost = 0  
    time = random.randint(1, 7)  # Adjust the range as needed
    state = fake.city()

    # Append the generated city name to the list
    city_names.append(place)

    # Create and execute the SQL statement to insert data
    sql = "INSERT INTO touristplaces (place, cost, time, state) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (place, cost, time, state))

def generate_distances(cursor, city_names):
    existing_combinations = set()

    for from_place in city_names:
        for to_place in city_names:
            if from_place != to_place:
                distance = random.randint(50, 500)  # Adjust the range as needed
                combination = (from_place, to_place)

                # Ensure that the combination is not repeated
                if combination not in existing_combinations:
                    existing_combinations.add(combination)

                    # Insert data into the 'Distances' table
                    sql = "INSERT INTO distances (fromplace, toplace, distance) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (from_place, to_place, distance))

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
        touristplaces(cursor, city_names)

    generate_distances(cursor, city_names)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    run()
