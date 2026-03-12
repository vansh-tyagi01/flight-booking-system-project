from flask import Flask,render_template,redirect,request

app = Flask(__name__)

total_seat=97
total_seat_real = list(range(1,total_seat+1))

booked_seat = []
booked_name_seat = []

@app.route("/ticket_book" , methods = ["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form.get("username")
        seat_no = int(request.form.get("seat_number"))

        if seat_no not in total_seat_real:
            return "Invalid seat number"
        
        if seat_no in booked_seat:
            return "Already Booked"
        else:
            booked_seat.append(seat_no)
            booked_name_seat.append([name,seat_no])
        
            return render_template("welcome_flight.html" , n=name , s=seat_no)
    
    return render_template("flight_Booking.html")

@app.route("/ticket_cancel" , methods=["GET","POST"])
def cancel():
    if request.method == "POST":
        name = request.form.get("username")
        seat_no = int(request.form.get("seat_number"))

        if seat_no in booked_seat and [name,seat_no] in booked_name_seat:
            booked_seat.remove(seat_no)
            booked_name_seat.remove([name,seat_no])
            return render_template("cancel.html", n=name , s=seat_no)
        else:
            return "seat number not exist in Booked seat"
    
    return render_template("flight_Booking.html")

@app.route("/home")
def homePage():
    return add()

    
@app.route("/show")
def show():
    return render_template("show_passenger_data.html", data=booked_name_seat)
    

@app.route("/Available")
def available():
    available_seat=[]
    for seat in total_seat_real:
        if seat not in booked_seat:
            available_seat.append(seat)
    
    return render_template("Available.html",data=available_seat)








    