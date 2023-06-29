from SimConnect import *
from django.core.cache import cache


sm = -1
aq = -1
data = {"ground_altitude":0,
        "sim_on_ground":0,
        "aircraft_name":"",
        "plane_altitude":0,
        "airspeed_indicated":0,
        "airspeed_mach":0,
        "airspeed_true":0}

def get_singleton_instance():
    print("Checking for instance")
    instance = cache.get('flightSim')
    if instance is None:
        x = CheckForFlightSim()
        y = SetRequests()
        cache.set('flightSim',instance)
    return instance


"""
Get the state of the landing gear
"""
def GetLandingGearState():
    return aq.get("GEAR_HANDLE_POSITION")


"""
Set the state of the landing gear
"""
def SetLandingGearState(new_state):
    aq.set("GEAR_HANDLE_POSITION",new_state)
    return GetLandingGearState()


def getSystemState():
    global data
    data["ground_altitude"]=  aq.get("GROUND_ALTITUDE") or False #Ground altitude
    data["sim_on_ground"]= aq.get("SIM_ON_GROUND") #Check if the sim is on the ground
    data["aircraft_name"]= aq.get("TITLE") #Name of the aircraft from aircraft.cfg
    data["plane_altitude"]= aq.get("PLANE_ALTITUDE") #plane altitude
    data["airspeed_indicated"]= aq.get("AIRSPEED_INDICATED") #Indicated airspeed
    data["airspeed_mach"]= aq.get("AIRSPEED_MACH") #Current mach
    data["airspeed_true"]=  aq.get("AIRSPEED_TRUE") #True airspeed
    return data



def SetRequests():
    global aq 
    aq = AircraftRequests(sm, _time=1000)

"""
Function used to create an instance of the SimConnect and check that the game is working correctly
"""
def CheckForFlightSim(system_debug=False):
    try:
        global sm 
        sm = SimConnect()
        print('SimConnect instance created')
        return 1
    except Exception as e:
        if system_debug:
            print("An error occurred:", str(e))
        return -1


get_singleton_instance()


