# Program: Movie Ticket Booking Manager

def get_available(total, booked):
    """Return available seat numbers."""
    return [seat for seat in range(1, total + 1) if seat not in booked]

def make_booking(booked, seat):
    """Books a seat if free."""
    if seat in booked:
        print(f"Seat {seat} already taken!")
    else:
        booked.append(seat)
    return booked

def cancel_booking(booked, seat):
    """Cancels a booking if found."""
    if seat in booked:
        booked.remove(seat)
    else:
        print(f"Seat {seat} was not booked.")
    return booked

# Example run
total = 10
booked_list = [2, 5, 7]
booked_list = make_booking(booked_list, 3)
booked_list = cancel_booking(booked_list, 5)
print("Free Seats:", get_available(total, booked_list))
