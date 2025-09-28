import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",       # your MySQL username
    password="12345",   # your MySQL password
    database="theater_db"
)

cursor = db.cursor()

def add_movie():
    title = input("Enter movie title: ")
    duration = int(input("Enter duration (minutes): "))
    rating = input("Enter rating (e.g. PG, U/A, A): ")
    cursor.execute("INSERT INTO movies (title, duration, rating) VALUES (%s, %s, %s)", 
                   (title, duration, rating))
    db.commit()
    print("Movie added successfully!")

def view_movies():
    cursor.execute("SELECT * FROM movies")
    for row in cursor.fetchall():
        print(row)

def add_show():
    movie_id = int(input("Enter movie ID: "))
    show_time = input("Enter show time (YYYY-MM-DD HH:MM:SS): ")
    seats = int(input("Enter total seats: "))
    cursor.execute("INSERT INTO shows (movie_id, show_time, total_seats, available_seats) VALUES (%s, %s, %s, %s)",
                   (movie_id, show_time, seats, seats))
    db.commit()
    print("Show added successfully!")

def view_shows():
    cursor.execute("SELECT s.show_id, m.title, s.show_time, s.available_seats FROM shows s JOIN movies m ON s.movie_id = m.movie_id")
    for row in cursor.fetchall():
        print(row)

def book_ticket():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    cursor.execute("INSERT INTO customers (name, phone) VALUES (%s, %s)", (name, phone))
    customer_id = cursor.lastrowid

    view_shows()
    show_id = int(input("Enter show ID to book: "))
    seats = int(input("Enter number of seats: "))

    cursor.execute("SELECT available_seats FROM shows WHERE show_id=%s", (show_id,))
    available = cursor.fetchone()[0]

    if available >= seats:
        cursor.execute("INSERT INTO bookings (customer_id, show_id, seats_booked) VALUES (%s, %s, %s)",
                       (customer_id, show_id, seats))
        cursor.execute("UPDATE shows SET available_seats = available_seats - %s WHERE show_id=%s",
                       (seats, show_id))
        db.commit()
        print("Booking successful!")
    else:
        print("Not enough seats available.")

def view_bookings():
    cursor.execute("""SELECT b.booking_id, c.name, m.title, s.show_time, b.seats_booked 
                      FROM bookings b 
                      JOIN customers c ON b.customer_id=c.customer_id 
                      JOIN shows s ON b.show_id=s.show_id 
                      JOIN movies m ON s.movie_id=m.movie_id""")
    for row in cursor.fetchall():
        print(row)

# Menu
while True:
    print("\n--- Theater Booking System ---")
    print("1. Add Movie")
    
    print("2. Add Show")
    
    print("3. Book Ticket")
    
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        add_show()
    elif choice == "3":
        book_ticket()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
