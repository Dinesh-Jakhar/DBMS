import mysql.connector

def clear_cost_column(cursor):
    # Clear the 'cost' column by setting it to 0
    cursor.execute("UPDATE touristplaces SET cost = 0")

def calculate_and_update_cost(cursor):
    # Fetch places from 'itinerary' table
    cursor.execute("SELECT place, ticket_cost FROM itinerary")
    places_cost = cursor.fetchall()

    # Aggregate the ticket costs for each place
    aggregated_costs = {}
    for place, ticket_cost in places_cost:
        if place in aggregated_costs:
            aggregated_costs[place] += ticket_cost
        else:
            aggregated_costs[place] = ticket_cost

    # Update the 'cost' column in 'touristplaces' table based on the aggregated costs
    for place, total_cost in aggregated_costs.items():
        cursor.execute("UPDATE touristplaces SET cost = %s WHERE place = %s", (total_cost, place))

def run():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Vidhita2601',
        database='project',
    )

    cursor = conn.cursor()


        # Clear the 'cost' column
    clear_cost_column(cursor)

        # Calculate and update cost based on itinerary data
    calculate_and_update_cost(cursor)

        # Commit changes
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run()
