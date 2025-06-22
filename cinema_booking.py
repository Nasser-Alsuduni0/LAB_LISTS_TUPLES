booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

def display_booked_seats():
    ''' This function displays all currently booked seats in sorted order.'''
    
    if not booked_seats:
        print("No seats booked yet.")
    else:
        print("\nBooked Seats:")
        for row, seat in sorted(booked_seats):
            print(f"Row {row}, Seat {seat}")

def check_availability():
    ''' This function checks if a specific seat is available or already booked.'''

    try:
        row = int(input("Enter row number (1-10): "))
        seat = int(input("Enter seat number (1-20): "))
        if (row, seat) in booked_seats:
            print(f"Seat Row {row}, Seat {seat} is already booked.")
        else:
            print(f"Seat Row {row}, Seat {seat} is available.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def add_booking():
    ''' This function allows the user to book a seat if it's available.'''

    try:
        row = int(input("Enter row number (1-10): "))
        seat = int(input("Enter seat number (1-20): "))
        if not (1 <= row <= 10 and 1 <= seat <= 20):
            print("Invalid seat. Row must be 1-10 and Seat must be 1-20.")
        elif (row, seat) in booked_seats:
            print("This seat is already booked.")
        else:
            booked_seats.append((row, seat))
            print("Booking successful.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def cancel_booking():
    ''' This function allows the user to cancel an existing booking.'''

    try:
        row = int(input("Enter row number to cancel (1-10): "))
        seat = int(input("Enter seat number to cancel (1-20): "))
        if (row, seat) in booked_seats:
            booked_seats.remove((row, seat))
            print("Booking cancelled.")
        else:
            print("This seat is not booked.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def print_stats():
    ''' This function prints statistics: total booked seats and number of bookings per row.'''

    print("\nBooking Statistics:")
    print(f"Total booked seats: {len(booked_seats)}")
    row_counts = [0] * 10  
    for row, seat in booked_seats:
        row_counts[row - 1] += 1
    for i, count in enumerate(row_counts):
        print(f"Row {i+1}: {count} seats booked")

def menu():
    ''' This function displays the main menu and handles user interaction.'''

    while True:
        print("\n--- Cinema Booking System ---")
        print("1. Display all booked seats")
        print("2. Check seat availability")
        print("3. Add a booking")
        print("4. Cancel a booking")
        print("5. Print all booked seats (sorted)")
        print("6. Show statistics")
        print("Type 'exit' to quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == '1':
            display_booked_seats()
        elif choice == '2':
            check_availability()
        elif choice == '3':
            add_booking()
        elif choice == '4':
            cancel_booking()
        elif choice == '5':
            display_booked_seats()
        elif choice == '6':
            print_stats()
        elif choice == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
