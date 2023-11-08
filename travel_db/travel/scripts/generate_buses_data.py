import os
import random
from faker import Faker
import mysql.connector

fake = Faker()

def generate_buses(cursor, places):
    existing_combinations = set()

    for departure_palce in places:
        for arrival_place in places:
            if departure_palce != arrival_place:
                travels = fake.company()[:15]
                departure_timeHours = str(random.randint(0, 23)).zfill(2)
                departure_timeMinutes = str(random.randint(0, 59)).zfill(2)
                arrival_timeHours = str(random.randint(0, 23)).zfill(2)
                arrival_timeMinutes = str(random.randint(0, 59)).zfill(2)
                duration = f"{random.randint(1, 12)}h {random.randint(0, 59)}m"
                fare = f"${random.randint(10, 100)}"
                seats_available = random.randint(0, 16)
                ac_sleeper = random.choice(["AC", "Non-AC"])
                bus_num = fake.unique.random_number(digits=7)
                date = fake.date_between(start_date="-1y", end_date="today").strftime("%m/%d/%Y")
                day = fake.day_of_week()
                one = '#DDF4EC'
                two = '#DDF4EC'
                three = '#DDF4EC'
                four = '#DDF4EC'
                five = '#DDF4EC'
                six = '#DDF4EC'
                seven = '#DDF4EC'
                eight = '#DDF4EC'
                nine = '#DDF4EC'
                ten = '#DDF4EC'
                elven = '#DDF4EC'
                twelve = '#DDF4EC'
                thirtn = '#DDF4EC'
                fouthn = '#DDF4EC'
                fivethn = '#DDF4EC'
                sixthn = '#DDF4EC'

                combination = (departure_palce, arrival_place)

                if combination not in existing_combinations:
                    existing_combinations.add(combination)

                    # Insert data into the 'buses_table'
                    sql = "INSERT INTO buses_table (travels, departure_timeHours, departure_timeMinutes, departure_palce, arrival_timeHours, arrival_timeMinutes, arrival_place, duration, fare, seats_available, ac_sleeper, bus_num, date, day, one, two, three, four, five, six, seven, eight, nine, ten, elven, twelve, thirtn, fouthn, fivethn, sixthn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


    # Execute the SQL statement
                cursor.execute(sql, (travels, departure_timeHours, departure_timeMinutes, departure_palce, arrival_timeHours, arrival_timeMinutes, arrival_place, duration, fare, seats_available, ac_sleeper, bus_num, date, day, one, two, three, four, five, six, seven, eight, nine, ten, elven, twelve, thirtn, fouthn, fivethn, sixthn))

def run():
    # Connect to your MySQL database
    conn = mysql.connector.connect(
       host='localhost',
        user='root',
        password='@Vidhita2601',
        database='project',
    )

    cursor = conn.cursor()

    # Fetch places from the 'itinerary' table
    cursor.execute("SELECT DISTINCT place FROM itinerary")
    places = [row[0] for row in cursor.fetchall()]

    # Generate buses for the fetched places
    generate_buses(cursor, places)

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

# Run the code
run()






