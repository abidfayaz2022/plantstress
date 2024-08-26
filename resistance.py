import usbtmc
import gpiod
import time

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
        # Set all pins to high
        for line in relay_lines:
            line.set_value(0)
            time.sleep(10)
            resistance =instr.ask(":READ?")
            print("Resistance (Ohms):", resistance)
            line.set_value(1)
        
        
        

finally:
    # Release all lines
    for line in relay_lines:
        line.release()


# Close the connection
instr.close()


# while(True):
# 	time.sleep(3)
# 	# Trigger a single measurement and read the result
# 	resistance = instr.ask(":READ?")
# 	print("Resistance (Ohms):", resistance)

# # Close the connection
# instr.close()
