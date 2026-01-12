from django.urls import path
from . import views

urlpatterns = [
    path('/', views.ToonAll),
    path('/addSpeler', views.AddSpeler),
    path('/<int:id>', views.ToonSpler),
    path('/addMatch', views.AddMatch),
    path('/changeMatchCode/<int:id>', views.changeMatchCode),
    path('/resultaat/<int:spelerID>/<int:matchCode>', views.getRes),
    path('/totaal/<int:spelerID>', views.getTotaal)
]