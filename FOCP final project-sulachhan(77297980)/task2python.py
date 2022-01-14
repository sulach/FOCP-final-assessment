print("Swallow Speed Analysis: Version 1.0")
speed_km = []
speed_miles = []
while True:
    read = input("Enter the next reading: ")
    if read == "":
       break
    if ((read[0]!= "U") and (read[0]!= "E")) :
        print("Invalid Input Format!")
        continue
    if read[0] == 'U':
          speed_miles.append(float(read[1:]))
          speed_km.append(float(read[1:]) *  1.60934)
    elif read[0] == 'E':
          speed_miles.append(float(read[1:]) /  1.60934)
          speed_km.append(float(read[1:]))
if speed_km==[]:
     print("No Readings Entered. \nNothing to do.")
else:
    print(f"\nResults Summary\n\n{len(speed_km)} Readings Analysed.\n")
    print("Max Speed: {:.1f} MPH, {:.1f}KPH.".format(max(speed_miles),max(speed_km)))
    print("Min Speed: {:.1f} MPH, {:.1f}KPH.".format(min(speed_miles),max(speed_km)))
    print("Avg Speed: {:.1f} MPH, {:.1f}KPH.".format(sum(speed_miles)/len(speed_miles),sum(speed_km)/len(speed_km)))
