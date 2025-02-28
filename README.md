# PlantPerfect: Assessing Ideal Planting Conditions Device

## The Challenge
Plants and trees are essential to our environment, yet the planting process has become increasingly challenging due to issues such as climate change, overshading, canopy coverage, evaporation, transpiration, and deforestation. Identifying the perfect planting spot with adequate sunlight, humidity, and temperature is now more difficult than ever.

## The Solution
PlantPerfect addresses this issue by designing a simple device that senses and measures humidity, temperature, and sunlight in a potential planting area. The device provides continuous real-time data to help users make informed planting decisions.

## System Design
The first version of PlantPerfect uses the Raspberry Pi Sensor Kit and a connected computer with an IDE for code execution and data visualization. The system includes:
- Sensors for humidity, temperature, and light
- A laptop for output display and data analysis

![image](https://github.com/user-attachments/assets/f6e45d5e-1b0f-40af-a221-422022b97329)

### System Components:
1. **Prototype Hardware**
   - Raspberry Pi microcontroller board (from the Raspberry Pi Sensor Kit).
   - Temperature and humidity sensor.
   - Light sensor.
   - Button for user interaction.
   - Computer for output display and power supply.

2. **Designed Device**
   - 3D-printed container (box) to house:
     - Microcontroller and sensors.
     - Batteries.
   - OLED or similar display screen for data output.
  
### Circuit

![image](https://github.com/user-attachments/assets/897d3caf-32da-455f-a5e9-66c6c8aa5212)

**_Note_:** The Wowki version uses DHT22 instead of DHT20 & a different LDR sensor pin.

## Implementation
The device operates as follows:
1. The user presses a button to initiate the process.
2. The connected microcontroller executes the code via the Thonny IDE.
3. Sensors collect data on environmental conditions.
4. The computer's IDE displays the data, including:
   - Quantitative metrics for temperature, humidity, and light levels.
   - Feedback on whether the area is suitable for planting based on standard conditions.

## Testing
Several tests were conducted to ensure the device's accuracy and functionality:
1. **Temperature Testing**
   - Compared device readings with a thermometer.
   - Result: Minimal margin of error.
2. **Humidity Testing**
   - Compared device readings with a hygrometer.
   - Result: Minimal margin of error.
3. **Light Level Testing**
   - Tested in various lighting conditions (e.g., bright sunlight, shade, darkness).
   - Result: Accurate light level readings.
4. **Button Functionality**
   - Verified the button's ability to start and stop the process.
   - Result: Successfully initiated and halted operations.

## Conclusion and Future Work
PlantPerfect effectively monitors environmental conditions, providing valuable feedback on temperature, humidity, and light levels for optimal planting decisions. 

### Future Enhancements:
- **Improved Design**
  - Smaller size with a built-in screen.
  - Independent power supply for portability.
- **Additional Sensors**
  - Measurements for pH levels, air quality, soil moisture, and gases.
- **Enhanced Usability**
  - Mobile app or built-in displays for easy user interaction.
 
## Simulation:
Downloaded from https://wokwi.com/projects/424077850369591297

Simulate this project on https://wokwi.com

---

*PlantPerfect helps users make informed decisions for successful planting, addressing environmental challenges with precision and reliability.*
