"""
Gets the inverse of a hexidecimal colour code to return the complimentary colour
"""


inHex = input("Insert hex number for your colour: ")
inHex = inHex.strip("#")

#Breaking inout into red, blue and green channels
inRed = int("0x" + inHex[:2],16)
inBlue = int("0x" + inHex[2:4], 16)
inGreen = int("0x" + inHex[4:], 16)

#Inverting channels
outRed = str(hex(255 - inRed))
outBlue = str(hex(255 - inBlue))
outGreen = str(hex(255 - inGreen))

outputHex = [outRed, outBlue, outGreen]

#Doing some tidy up as Python hex isn't in desired format 
for i in range(3):
    newHex = outputHex[i][2:]
    if len(newHex) < 2:
        newHex = "0" + newHex
    outputHex[i] = newHex
    

print("The complimentary colour of #" + str(inHex) + " is:")
print("#" + outputHex[0] + outputHex[1] + outputHex[2])
