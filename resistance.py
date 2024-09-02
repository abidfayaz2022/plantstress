import usbtmc
import gpiod
import time
import mysql.connector
from datetime import datetime


conn =mysql.connector.connect(host='localhost',user='root',password='2953',database='Plant_Stress_Resistance')
print(conn.connection_id)
cur = conn.cursor()

relay_pins=[2,3,4,14,15,17,18,27]


chip = gpiod.Chip('gpiochip4')

relay_lines=[]

for pin in relay_pins:
    relay_line = chip.get_line(pin)
    relay_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
    relay_lines.append(relay_line)

# Set all pins to low
for line in relay_lines:
        line.set_value(1)
        time.sleep(0.2)
# Create an instance of the Instrument class
instr = usbtmc.Instrument(6833, 8459)  # Replace with the correct Vendor ID and>

# Identify the device
response = instr.ask("*IDN?")
print("Device ID:", response)

# Reset the device to ensure a known state
instr.write("*RST")

# Clear any previous error states
instr.write("*CLS")

# Set the device to measure resistance
instr.write(":FUNC 'RES'")
# Enable auto-ranging for resistance measurement
instr.write(":RES:RANG:AUTO ON")

try:
    while True:
        container_Resist = [0] * len(relay_pins)

        for i, line in enumerate(relay_lines):
            line.set_value(0)  # Activate relay
            time.sleep(0.1)  # Allow some time for stabilization
            sum_resistance = 0

            for _ in range(10):
                resistance = float(instr.ask(":READ?"))
                sum_resistance += resistance
                time.sleep(1)  # Wait for 1 second before the next reading

            average_resistance = sum_resistance / 10
            container_Resist[i] = average_resistance
            line.set_value(1)  # Deactivate relay

            print(f"Relay {i} Resistance (Ohms):", average_resistance)
        current_time = datetime.now().strftime('%H:%M:%S')
        current_date = datetime.now().strftime('%Y-%m-%d')
        cur.execute(
    """INSERT INTO Resistance (
        Time, Date, Container_1, Container_2, Container_3, 
        Container_4, Container_5, Container_6, Container_7, Container_8
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    (current_time, current_date, container_Resist[0], container_Resist[1], container_Resist[2], 
     container_Resist[3], container_Resist[4], container_Resist[5], 
     container_Resist[6], container_Resist[7])
)

        conn.commit()
   
    

finally:
    # Release all lines
    for line in relay_lines:
        line.release()
    cur.close()
    conn.close()  
    # Close the connection
    instr.close() 





# while(True):
# 	time.sleep(3)
# 	# Trigger a single measurement and read the result
# 	resistance = instr.ask(":READ?")
# 	print("Resistance (Ohms):", resistance)

# # Close the connection
# instr.close()
