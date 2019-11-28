class Aereoport:
    def __init__(self):
        self.flights ={}
        self.passengers ={}
        self.travellers ={}

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
            objet_F = flights(_id,departure,arriving,departure_gate,arriving_gate,take_off_track,landing_track,status)
            self.flights[_id]=object_F

    def cargar_datos_passengers():
        P=open("data/passengers.csv","r+")
        all_lines=P.readlines()
        P.close
        all_lines.pop(0)
        for line in all_lines():
            campos=all_lines.split(",")
            flight=campos[0]
            passport=campos[1]
            location=campos[4]
            objet_P=passengers(flight,passport,location)
            self.passengers[_flight]=object_P






            

    def cargar_datos_attendants():
        A=open("data/attendants.csv","r+")
        all_lines=A.readlines()
        A.close
            

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
    def __init__ (self,_flight,_passport,_location):
        self._id = __id

class Travaller:
    def __init__ (self,_passport,_forename,_surname):
