##-------------------------------------------
##  _____  _     _                          |
## |  __ \(_)   | |                         |
## | |  | |_ ___| |_ __ _ _ __   ___ ___    |
## | |  | | / __| __/ _` | '_ \ / __/ _ \   | 
## | |__| | \__ \ || (_| | | | | (_|  __/   |
## |_____/|_|___/\__\__,_|_| |_|\___\___|   |
##------------------------------------------|
##Author: Hussain Salam | Date: 06/10/2016  |
##-------------------------------------------

CAR_L = 4                                       
DIST_1 = int(input("[SYSTEM]: Input the distance between you and the FRONT vehicle: "))
DIST_2 = int(input("[SYSTEM]: Input the distance between you and the REAR vehicle: "))
SPEED = int(input("[SYSTEM]: Input your current speed: "))
WEATHER = input("[SYSTEM]: Is it raining (Y/N)")            
MID_P = (DIST_1+DIST_2)/2
SCEN_2 = (SPEED/10)*10
print ("[DEBUGGER]: Midpoint is", MID_P)
print("[SYSTEM]: You vehicle should be: ",MID_P,"away from both vehicles (SCEN1)")
print ("[SYSTEM]: Your vehicle should be: ",SCEN_2," away from both vehicles (SCEN2)")
if WEATHER = Y:
    SCEN_2 = SCEN_2*2
    print ("[SYSTEM]: Your vehicle should be: ",SCEN_2," away from both vehicles (SCEN3)")
elif WEATHER = N:
    print ("[SYSTEM]: Your vehicle should be: ",SCEN_2," away from both vehicles (SCEN3)")
else:
    print("[ERROR]: Unrecognized Syntax, Contact Author.")
