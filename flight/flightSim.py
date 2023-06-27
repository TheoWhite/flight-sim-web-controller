from SimConnect import *


def CheckForFlightSim(system_debug=False):
    try: 
        return SimConnect()
    except SimConnect.SimConnectException as e:
        if(system_debug == True):
            print("An error occured: " , e)
    return -1


