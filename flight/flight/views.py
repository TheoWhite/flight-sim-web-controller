from django.views import View
from django.shortcuts import render

class Homepage(View):
    def get(self,request):
        return render(request,"homepage.html")