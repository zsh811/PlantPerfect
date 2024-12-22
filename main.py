from machine import Pin, I2C, ADC
from utime import sleep
from dht20 import DHT20

i2c0_sda = Pin(8)
i2c0_scl = Pin(9)
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)

dht20 = DHT20(0x38, i2c0)

light_sensor_pin = Pin(0)
light_sensor = ADC(light_sensor_pin)

while True:
    measurements = dht20.measurements
    temperature = measurements['t']
    humidity = measurements['rh']

    light_level = light_sensor.read_u16()

    print("Temperature: {:.2f} °C".format(temperature))
    print("Humidity: {:.2f} %RH".format(humidity))
    print("Light Level:", light_level)

    if temperature >= 20 and temperature <= 30:
         if humidity >= 40 and humidity <= 60:
             if light_level >= 1000:
                        print("Area is suitable for planting.")
             else:
                        print("Insufficient light for planting.")
         else:
                    print("Humidity is not within the optimal range for planting.")
    else:
                print("Temperature is not within the optimal range for planting.")

  sleep(1)
