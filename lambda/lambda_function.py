import requests
import random
import time
import json
from concurrent.futures import ThreadPoolExecutor

#print(f"Attempting to run")
# Define the base URL of the web service
url = "https://c01-usa-east-et.integrate-test.boomi.com/ws/simple/createReading;boomi_auth=bGFtYmRhQGJvb21pX2p1YW5yb2RyaWd1ZXotNEEwWlpDLlZKUTlSUjoyN2UzZjQzNS1lZWY1LTQ0ZGItOTExOS1jZGIwMDBjNzIzMjA="

def send_post_request(sensor_id, temp, press, t):
    data = {
        "sensor_id": sensor_id,
        "name": f"Sensor {sensor_id}",
        "location": f"Location {sensor_id}",
        "temperature": temp,
        "pressure": press
    }
    response = requests.post(url, json=data)
    print(f"Sensor {sensor_id} sent data for {t} time: {response.status_code}")

def handler(event, context):
    # Define the number of sensors and the duration of the simulation in seconds
    num_sensors = 10
    duration = 10

    # Define the variance for temperature and pressure readings
    temp_var = 2
    press_var = 2

    # Generate a dictionary with the sensor ID as key and two associated values
    sensor_dict = {}
    for i in range(1, num_sensors+1):
        temp_value = random.randint(0, 40)
        pressure_value = random.randint(800, 1200)
        sensor_dict[i] = (temp_value, pressure_value)

    # Loop over the duration of the simulation
    for t in range(duration):

        with ThreadPoolExecutor(max_workers=5) as executor:
            # Loop over each sensor
            for i in range(1, num_sensors+1):
                
                # Generate a random variance for temperature and pressure readings
                temp_var_rand = random.uniform(-temp_var, temp_var)
                press_var_rand = random.uniform(-press_var, press_var)
                if t >= 7 and t<=9 and i in (2,7):
                    press_var_rand += 1000
                
                # Get the associated values for the current sensor from the dictionary
                values = sensor_dict[i]

                # Calculate the new temperature and pressure readings with variance
                temp = values[0] + temp_var_rand
                press = values[1] + press_var_rand

                # Submit the HTTP POST request to the executor
                executor.submit(send_post_request, i, temp, press, t)

        # Wait for 1 second before sending the next round of requests
        time.sleep(1)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Status ": "Executed simulation completely"
        })
    }

#e = ""
#context = ""
#handler(e, context)
