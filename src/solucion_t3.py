class Flight:
    def __init__ (self,__id,_departure,_arriving,_departure_gate,_arriving_gate,_take_off_track,_landing_track,_status):
        self._id = __id
        self.departure = _departure
        self.arriving = _arriving
        self.departure_gate = _departure_gate
        self.arriving_gate = _arriving_gate
        self.take_off_track = _take_off_track
        self.landing_track = _landing_track
        self.status = _status

class Passenger:
    def __init__ (self,_passport,_location,_flight,__class,_seat):
        self.passport = _passport
        self.location = _location
        self.flight = _flight
        self._class = __class
        self.seat = _seat

class Travaller:
    def __init__ (self,_passport,_forename,_surname,_date_of_birth,_country,_gender,_marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status
        
class Attendant:
    def __init__ (self,_passport,_forename,_surname,_date_of_birth,_country,_gender,_marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status

class Plane:
    def __init__ (self,_plate,_manufacturer,_model,_passengers_capacity,_luggage_capacity,_max_speed):
        self.plate = _plate
        self.manufacturer = _manufacturer
        self.model = _model
        self.passengers_capacity = _passengers_capacity
        self.luggage_capacity = luggage_capacity
        self.max_speed = _max_speed

class Pilot:
    def __init__ (self,_passport,_forename,_surname,_date_of_birth,_country,_gender,_marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status

class Aereoport:
    def __init__(self):
        self.flights ={}
        self.passengers ={}
        self.travellers ={}
        self.attendants ={}
        self.planes ={}

    def cargar_datos_flights():
        F=open("data/flights.csv","r+")
        all_lines=F.readlines()
        F.close
        all_lines.pop(0)
        for line in all_lines():
            campos=all_lines.split(",")
            _id = campos[0]
            departure = campos[4]
            arriving = campos[5]
            status = campos[6]
            departure_gate = campos[7]
            arriving_gate = campos[9]
            take_off_track = campos[8]
            landing_track = campos[10]
            objet_F = Flight(_id,departure,arriving,departure_gate,arriving_gate,take_off_track,landing_track,status)
            self.flights[_id]=object_F

    def cargar_datos_passengers():
        P=open("data/passengers.csv","r+")
        all_lines=P.readlines()
        P.close
        all_lines.pop(0)
        for line in all_lines():
            campos=all_lines.split(",")
            passport=campos[1]
            location=campos[4]
            flight=campos[0]
            _class=campos[2]
            seat=campos[3]
            objet_P= Passenger(passport,location,flight,_class,seat)
            self.passengers[_passport]=object_P

    def cargar_datos_travellers():
        T=open("data/travellers.csv","r+")
        all_lines=T.readlines()
        T.close
        all_lines.pop(0)
        for line in all_lines():
            campos=all_lines.split(",")
            passport=campos[0]
            forename=campos[1]
            surname=campos[2]
            date_of_birth=campos[3]
            country=campos[4]
            gender=campos[5]
            marital_status=campos[6]
            objet_T= Treaveller(passport,forename,surname,date_of_birth,country,gender,marital_status)
            self.travellers[_passport]=object_T

    def cargar_datos_attendants():
        A=open("data/attendants.csv","r+")
        all_lines=A.readlines()
        A.close
        all_lines.pop(0)
        for line in all_lines():
            campos=all_lines.split(",")
            passport=campos[0]
            forename=campos[1]
            surname=campos[2]
            date_of_birth=campos[3]
            country=campos[4]
            gender=campos[5]
            marital_status=campos[6]
            objet_A= Attendant(passport,forename,surname,date_of_birth,country,gender,marital_status)
            self.travellers[_passport]=object_A

    def cargar_datos_planes():
        PLA=open("data/planes.csv","r+")
        all_lines=PLA.readlines()
        PLA.close
        all_lines.pop(0)
        for line in all_lines():
            campos=all_lines.split(",")
            plate=campos[0]
            manufacturer=campos[1]
            model=campos[2]
            passengers_capacity=campos[3]
            luggage_capacity=campos[4]
            max_speed=campos[5]
            objet_PLA= Plane(plate,manufacturer,model,passengers_capacity,luggage_capacity,max_speed)
            self.travellers[_passport]=object_PLA

    def cargar_datos_pilots():
        PIL=open("data/pilots.csv","r+")
        all_lines=PIL.readlines()
        PIL.close
        all_lines.pop(0)
        for line in all_lines():
            campos=all_lines.split(",")
            passport=campos[0]
            forename=campos[1]
            surname=campos[2]
            date_of_birth=campos[3]
            country=campos[4]
            gender=campos[5]
            marital_status=campos[6]
            objet_PIL= Pilot(passport,forename,surname,date_of_birth,country,gender,marital_status)
            self.travellers[_passport]=object_PIL


    def sacar_estadisticas (self):
        estadisticas=open("statistics.csv", "w+")
        estadisticas.write("Date, Time, # of empty tracks, # of busy tracks, # passengers in checl-in, # of passengers in security, # of passengers boarded, # of flights landed, # of flights departured, avaialable gates, occupied gates")
        print("Introduzca la fecha en formato: AA,MM,DD")
        fecha=str(input())
        print("Introduzca la hora con formato: HH,MM")
        hora=str(input())
        occpied_track=[]
        dessoccupied_track=[]
        for flight in self.flights:
            if flight.departure[0:6]==fecha and int (flight.departure [7:11]) <= int (hora):
                if flight.status in ["landing","waiting"]:
                    occupied_track.append(flight.take_off_track)
                else:
                    dessoccupied_track.append(flight.take_off_track)
        number_off_occupied_track=len(ocuupied_track)
        number_off_dessoccupied_track=len(dessocuupied_track)

        occpied_gate=[]
        dessoccupied_gate=[]
        for flight in self.flights:
            if flight.departure[0:6]==fecha and int (flight.departure_gate [7:11]) <= int (hora):
                if flight.status in ["boarding","boarded"]:
                    occupied_gate.append(flight.departure_gate)
                else:
                    dessoccupied_gate.append(flight.departure_gate)
        number_off_occupied_gate=len(ocuupied_gate)
        number_off_dessoccupied_gate=len(dessocuupied_gate)

        arrived=[]
        departured=[]
        for flight in self.flights:
            if flight.departure[0:6]==fecha
                if flight.status in ["landed"]:
                    arrived.append(flight.arriving)
                if flight.status in ["in transit"]:
                    departured.append(flight.departure)
        arrived_flies=len(arrived)
        departured_flies=len(departured)

        check_in=[]
        security=[]
        boarded=[]
        for flight in self.flights:
            if flight.departure[0:6]==fecha and int (flight.departure_gate [7:11]) <= int (hora):
                for p in self.passengers:
                    if flight.location in ["check-in"]:
                        check_in.append(passengers.location)
                    if flight.location in ["security"]:
                        occupied_gate.append(passengers.location)
                    if flight.location in ["boarded"]:
                        occupied_gate.append(passengers.location)


        number_off_check_in=len(check_in)
        number_off_security=len(security)
        number_off_boarded=len(boarded)

        estadisticas.write(fecha+","+hora+","+number_off_dessoccupied_track+","+number_off_occupied_track+","+number_off_check_in+","+number_off_security+","+number_off_boarded+","+arrived_flies+","+departured_flies+","+number_off_dessoccupied_gate+","+number_off_occupied_gate)    

            

