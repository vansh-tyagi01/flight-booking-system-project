print("*........FLIGHT BOOKING SYSTEM........*")
print(" ")
passengar_seat_1=97
passengar_seat_2=passengar_seat_1
passengar_seat_2=list(range(1,passengar_seat_2+1))
booked_name_seat=[]
show_booked_seat_total_seat=[]

def booking_seat():
    name=input("Enter your name:")
    seat_no=int(input("Enter your seat no to Book:"))
        
    if seat_no not in passengar_seat_2:
        print("Invalid seat Number!")
        return
    
    if seat_no in show_booked_seat_total_seat:
        print("Allready Booked")
    else:
        booked_name_seat.append([name,seat_no])
        show_booked_seat_total_seat.append(seat_no)
        print(name,"your seat",seat_no,"is Booked Successfully")
            
def cancel_seat():
    name=input("Enter your name:")
    seat_no=int(input("Enter your seat number to remove?:"))

    if seat_no in show_booked_seat_total_seat and [name,seat_no] in booked_name_seat:
        booked_name_seat.remove([name,seat_no])
        show_booked_seat_total_seat.remove(seat_no)
        print(f"{name} your seat {seat_no} is cancelled successfully")
    else:
        print("Booking not found")


def show_Booked_Seat():
    if len(booked_name_seat)==0:
        print("Empty booked seat")
    else:
        print("List of passenger name and Booking seat :",booked_name_seat)
    #print("Empty booked seat" if len(booked_name_seat)==0 else booked_name_seat)


def show_booked_seat():
    print("Total Seat :",passengar_seat_2)
    if len(show_booked_seat_total_seat)==0:
        print("Empty booked seat")
    else:
        print("Booking Seat :",show_booked_seat_total_seat)

while True:
    print("1. Book the seat")
    print("2. Cancel seat")
    print("3. show passenger name and Booking seat")
    print("4. Would you like to see how many seats have already been booked out of the total seats?")
    ch=int(input("Enter your choice?(0 to exit):"))

    if ch == 0:
        print("Program Exit")
        break
    elif ch == 1:
        booking_seat()
    elif ch == 2:
        cancel_seat()
    elif ch == 3:
        show_Booked_Seat()
    elif ch ==4:
        show_booked_seat() 
    else:
        print("Invalid choice!")