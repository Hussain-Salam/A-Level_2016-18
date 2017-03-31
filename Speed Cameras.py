#   _____                     _    _____                                    |
#  / ____|                   | |  / ____|                                   |
# | (___  _ __   ___  ___  __| | | |     __ _ _ __ ___   ___ _ __ __ _ ___  |
#  \___ \| '_ \ / _ \/ _ \/ _` | | |    / _` | '_ ` _ \ / _ \ '__/ _` / __| |
#  ____) | |_) |  __/  __/ (_| | | |___| (_| | | | | | |  __/ | | (_| \__ \ |
# |_____/| .__/ \___|\___|\__,_|  \_____\__,_|_| |_| |_|\___|_|  \__,_|___/ |
#        | |                                                                |
#        |_|                                                                |
#----------------------------------------------------------------------------
#               Developer: Hussain Salam | Date: 310/03/2017                |
#----------------------------------------------------------------------------

#Imports
import time

#Main
print("Intro....")
input("[SYSTEM]: Press 'RETURN' to begin timer")
start_time = time.time()
input ("[SYSTEM]: Press 'RETURN' to stop timer") 
stop_time = time.time()
distance = (1000)
time = stop_time - start_time

#Debug
    #Remove the # on the lines below to enable debugging
#print("[DEBUG]: ",time) //This value isn't rounded
#print("[DEBUG]: ",distance) //This value isn't rounded

#Output
avg_spd = distance / time
print("[SYSTEM]: The average speed of the vehicle is: {:.2f}".format(avg_spd))
