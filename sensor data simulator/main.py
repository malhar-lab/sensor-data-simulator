import random # import the random module to genarate random numbers
import time  #  import time module to add delays
import csv # import csv module to handle csv files
from datetime import datetime # import datetime module to handle date and time

# function to simulate sensor data reading
def generate_sensor_data():

    # dictionary to hold sensor data
    return {
    "temperature": round(random.uniform(20, 40),2), #generate random temperature between 20 and 40 degrees celsius in 2 decimal places
    "humidity" : round(random.uniform(30,90),2), #generate random humydity between 30 and 90 percent in 2 decimal places
    "light" : random.randint(100,1000), #generate random light intensity between 100 and 1000 lumens
    "gas" : random.randint(200,1000) # genarate random gas level between 200 and 1000 ppm
    }

# function to log sensor data to csv file
def save_to_csv(data):
    #open the csv file in append mode
    with open("iot_data_csv","a", newline="") as f: 
        # create a csv writer object
        writer=csv.writer(f)
        # write the data to csv file
        writer.writerow([datetime.now().strftime("%y-%m-%d %H:%M:%S"),data["temperature"],data["humidity"],data["light"],data["gas"]])

# function to display data
def display_data(data):
    print(f"\n[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}]")
    print(f"temperature : {data["temperature"]} C") 
    print(f"humidity : {data["humidity"]} %")
    print(f"Light Intensity : {data["light"]} lumens")
    print(f"gas level : {data["gas"]} ppm")

# alert system
def alert_system(data):
    if data["temperature"]>35:
        print("ALERT : high temperature!") 
        if data["humidity"]>85:
            print("ALERT : high humidity!")
            if data["gas"] >850:
                print("ALERT : high gas level!")   
# main funtion                

print("===== IOT Sensor Data Monitoring System =====")
print("generating sensor data... (press Cerl+C to stop)")

# csv file header creation
with open("iot_data.csv","w",newline="")as f:
    writer=csv.writer(f)
    writer.writerow(["timestamp","tempreture (C)","humidity (%)","light intensity(lumens)","gas level(ppm)"])

# infinite loop to contineusly read and log sensor data

while True:
    sensor_data=generate_sensor_data() # generate sensor data
    display_data(sensor_data) # display the sensor data
    save_to_csv(sensor_data) # save the sensor data to csv file
    alert_system(sensor_data)# check for alerts
    time.sleep(5) # wait for 5 sec before next readings    