from django.views import View
from django.shortcuts import render
from . import flightSim as fs
import keyboard
import time


keyboard_en = 0

class Homepage(View):
    def get(self,request):
        fs.get_singleton_instance()
        data = fs.getSystemState()
        print("Data is ", data)
        return render(request,"homepage.html")
    

class FlightData(View):
    def get(self,request):
        fs.get_singleton_instance()
        data = fs.getSystemState()
        print("Data is ", data)
        return render(request,"homepage.html")

    def post(self,request):
        fs.get_singleton_instance()
        req = request.POST.dict()
        if("input[gear]" in req):
            updateLandingGear(req)
            return render(request,"homepage.html", {"gear":fs.GetLandingGearState()})
        if("input[keyboard_value]" in req):
            global keyboard_en
            keyboard_en = req.get("input[keyboard_value]")
        return render(request,"homepage.html")
    

def updateLandingGear(req):
    landingGearState = int(req.get("input[gear]"))
    data = fs.getSystemState()
    print("Data is ", data)
    global keyboard_en
    if(keyboard_en == 1):
        keyboard.press('g')
        time.sleep(0.1)
        keyboard.release('g')
    else :
        fs.SetLandingGearState(landingGearState)