from django.views import View
from django.shortcuts import render
from . import flightSim as fs


class Homepage(View):
    def get(self,request):
        return render(request,"homepage.html")
    

class FlightData(View):
    def get(self,request):
        fs.get_singleton_instance()
        return render(request,"homepage.html")

    def post(self,request):
        fs.get_singleton_instance()
        req = request.POST.dict()
        landingGearState = int(req.get("input[gear]"))
        #print("---\n",landingGearState,"\nState:",type(landingGearState),"\n","---\n")
        fs.SetLandingGearState(landingGearState)
        return render(request,"homepage.html", {"gear":fs.GetLandingGearState()})