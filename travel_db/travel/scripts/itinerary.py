import random
from faker import Faker
import mysql.connector

def run():
    fake = Faker()

    # Connect to your MySQL database
    conn = mysql.connector.connect(
         host='localhost',
        user='root',
        password='@Vidhita2601',
        database='project',
    )

    cursor = conn.cursor()

    # Fetch places and corresponding time values from the touristplaces table
    cursor.execute("SELECT place, time FROM touristplaces")
    places_time = cursor.fetchall()


    def insert_itinerary_data(cursor, place, attractions, total_days):
        current_attraction_number = 0
        previous_place = None
        visiting_day = 1  # Initialize visiting_day to 0
                
        for _ in range(total_days):  # Multiply by 3 as you requested
                        in_time = random.randint(9, 12)  # Assuming hours in a day
                        out_time = random.randint(16, 18)
                        ticket_cost = random.randint(100, 500)
                        cursor.execute(
                            "INSERT INTO itinerary (place, attractions, visiting_day, in_time, out_time, ticket_cost) "
                            "VALUES (%s, %s, %s, %s, %s, %s)",
                            (place, f"Attraction {current_attraction_number+1}", visiting_day, in_time, out_time, ticket_cost)
                        )

                        if (current_attraction_number + 1) % 3 == 0:
                            visiting_day += 1  # Increment visiting_day every 3 attractions

                        if place != previous_place:
                            current_attraction_number = 1
                        else:
                            current_attraction_number += 1
                        previous_place = place


    # Generate data for places and insert it into the itinerary table
    for place, time in places_time:
        attractions = [f"Attraction {i}" for i in range(1, time * 3 + 1)]
        insert_itinerary_data(cursor, place, attractions, time*3 )

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run()
