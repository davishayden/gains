from django.http import HttpResponse
from models import WorkoutInstance
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def index(request):
    latest_workout_list = WorkoutInstance.objects.order_by('-created_at')[:5]
    context = {'latest_workout_list': latest_workout_list}
    return render(request, 'lifts/index.html', context)

def workoutDetail(request, workout_id):
    #needs to be changed so workout_details is an object with an array of lift instances and the data behind
    workout_details = WorkoutInstance.objects.get(id=workout_id)
    context = {'workout_details': workout_details}
    return render(request, 'lifts/workoutdetail.html', context)

def login(request):
    return HttpResponseRedirect("/lifts")

    #username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(username=username, password=password)
    #if user is not None:
     #   login(request, user)
        # Redirect to a success page.
    #else:
        # Return an 'invalid login' error message.
    #user = authenticate(username="hayden", password="password")
    #return render(request, 'lifts/index.html', user)