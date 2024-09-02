import usbtmc
instr = usbtmc.Instrument(6833, 8459)
print(instr.ask("*IDN?"))
# returns 'AGILENT TECHNOLOGIES,MSO7104A,MY********,06.16.0001'
