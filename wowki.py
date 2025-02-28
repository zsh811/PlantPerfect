from machine import Pin, ADC
from utime import sleep
import dht

# Creating a DHT22 object
sensor = dht.DHT22(Pin(8))

# Light sensor setup
light_sensor = ADC(Pin(27))

while True:
    try:
        # Measure temperature and humidity
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        
        # Read light level
        light_level = light_sensor.read_u16()
        
        # Print sensor readings
        print("Temperature: {:.2f} °C".format(temperature))
        print("Humidity: {:.2f} %RH".format(humidity))
        print("Light Level:", light_level)
        
        # Determine suitability for planting
        if 20 <= temperature <= 30:
            if 40 <= humidity <= 60:
                if light_level >= 1000:
                    print("Area is suitable for planting.")
                else:
                    print("Insufficient light for planting.")
            else:
                print("Humidity is not within the optimal range for planting.")
        else:
            print("Temperature is not within the optimal range for planting.")
        
    except Exception as e:
        print("Error reading sensor data:", e)
    
    sleep(1)
