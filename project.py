import usbtmc
import time

# Create an instance of the Instrument class
instr = usbtmc.Instrument(6833, 8459)  # Replace with the correct Vendor ID and Product ID

# Identify the device
response = instr.ask("*IDN?")
print("Device ID:", response)

# Set up the device (e.g., set to DC voltage measurement mode)
instr.write(":FUNC 'VOLT:DC'")  # Set to DC voltage measurement mode

# Set the range (e.g., set to 10V range)
instr.write(":VOLT:DC:RANG 10")

# Read the voltage value
voltage = instr.ask(":READ?")
print("Voltage:", voltage)

# Close the connection
instr.close()
