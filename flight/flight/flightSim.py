from SimConnect import *
from django.core.cache import cache


sm = -1
aq = -1

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


