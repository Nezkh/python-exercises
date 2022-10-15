from django.shortcuts import render

# Create your views here.
from.models import Director, Cast, Film

def index(request):
    num_director = Director.objects.all().count()
    num_cast = Cast.objects.all().count()
    num_film = Film.objects.all().count()
    
    return render(request,
                  'index.html', 
                  context={
                      'num_director': num_director,
                      'num_cast': num_cast,
                      'num_film': num_film,
                      }
                )