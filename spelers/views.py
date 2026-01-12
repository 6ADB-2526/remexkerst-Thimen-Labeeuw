from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Speler, Match
import json

# Create your views here.

#spelers
def ToonAll(request):
    AllSpelers = Speler.objects.all().values()
    return JsonResponse(list(AllSpelers), safe=False)

@csrf_exempt
def AddSpeler(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    NewSpeler = Speler()
    NewSpeler.naam = post_data["naam"]
    NewSpeler.voorNaam = post_data["vn"]
    NewSpeler.email = post_data["email"]

    NewSpeler.save()
    return HttpResponse("gelukt")

def ToonSpler(request, id):
    EenSpeler = Speler.objects.get(pk = id)
    
    return JsonResponse(model_to_dict(EenSpeler))

#matches
@csrf_exempt
def AddMatch(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    NewMatch = Match()
    NewMatch.SpelerID = post_data["spelerID"]
    NewMatch.matchCode = post_data["matchCode"]
    NewMatch.punten = post_data["punten"]

    NewMatch.save()

    return HttpResponse("gelukt")

@csrf_exempt
def changeMatchCode(request, id):
    post_data =  json.loads(request.body.decode('utf-8'))
    matchToChange = Match.objects.get(pk = id)
    matchToChange.matchCode = post_data["code"]
    matchToChange.save()

    return HttpResponse("changed")

def getRes(request, spelerID, matchCode):
    res = Match.objects.filter(SpelerID = spelerID, matchCode = matchCode).values()
    return JsonResponse(f"resultaat {res[0]["punten"]}", safe=False)

def getTotaal(resuest, spelerID):

    return HttpResponse("speler totaal")