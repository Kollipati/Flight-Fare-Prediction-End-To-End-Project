from flask import Flask, render_template, request
import sklearn
import pickle
import pandas as pd

file = open(r"app.pkl", "rb")
model = pickle.load(file)

app = Flask(__name__)


@app.route("/")
def welcome():
        return render_template("welcome.html")

@app.route("/predictor", methods = ["GET", "POST"])
def predict():
    
    if request.method == "POST":
        
        # Departure Date
        dep_t = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(dep_t, format = "%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dep_t, format = "%Y-%m-%dT%H:%M").month)
        
        # Departure Time
        Dep_hour = int(pd.to_datetime(dep_t, format = "%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(dep_t, format = "%Y-%m-%dT%H:%M").minute)
        
        # Arrival Date
        arr_t = request.form["Arr_Time"]
        Arrival_hour = int(pd.to_datetime(arr_t, format = "%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(arr_t, format = "%Y-%m-%dT%H:%M").minute)
        
        # Duration
        Duration_min = abs(Arrival_hour - Dep_hour)*60 + abs(Arrival_min - Dep_min)
        
        # Total stops
        Total_stops = int(request.form["Total_stops"])
        
        # Airline
        airline = request.form["Airline"]
        
        if airline == "Jet Airways":
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "IndiGo":
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "Air India":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "Multiple carriers":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "SpiceJet":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "Vistara":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "GoAir":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 1
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "Multiple carriers Premium Economy":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 1
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "Vistara Premium economy":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 1
            Jet_Airways_Business = 0
            Trujet = 0
            
        elif airline == "Jet Airways Business":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 1
            Trujet = 0
            
        elif airline == "Trujet":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 1
            
        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            Go_Air = 0 
            Multiple_carriers_Premium_economy = 0
            Vistara_Premium_economy = 0
            Jet_Airways_Business = 0
            Trujet = 0
            
        
        # Source
        source = request.form["Source"]
        
        if source == "Delhi":
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            
        elif source == "Kolkata":
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
            
        elif source == "Mumbai":
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
        
        elif source == "Chennai":
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            
        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            
        
        # Destination
        destination = request.form["Destination"]
        
        if destination == "Cochin":
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            
        elif destination == "Delhi":
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            
        if destination == "New Delhi":
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
            
        if destination == "Hyderabad":
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
            
        if destination == "Kolkata":
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
            
        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            
            
        prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Arrival_hour,
            Arrival_min,
            Dep_hour,
            Dep_min,
            Duration_min,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi,
            Air_India,
            Go_Air,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy
        ]])
        
        output = round(prediction[0], 2)
        print(output)
        
        return render_template("predictor.html", 
                               prediction_text = "Your Flight Fare from {} to {} is Rs. {}".format(source, destination, output))
                   
        
    return render_template("predictor.html")


@app.route("/about")
def about():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug = True)
