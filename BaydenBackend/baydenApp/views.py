from django.shortcuts import render
from .models import Events, Subscriber
from django.http import HttpResponse, HttpRequest
from .forms import SubscriberForm

# Create your views here.
def homepage(request):
    all_events = Events.objects.all()
    print(all_events)
    return render(request=request, template_name="homepage.html",
                  context={"all_events": all_events})

def index(request : HttpRequest):
    if request.method == "GET":
        all_events = Events.objects.all()
        context={"all_events": all_events}
        return render(request=request, template_name="index.html",
                      context=context)

    elif request.method == "POST":
        data ={"firstname": request.POST.get("first_name"),
               "lastname": request.POST.get("second_name"),
               "email": request.POST.get("email")}
        print(request.POST)
        from_form_subscriber = SubscriberForm(data=data)
        print("*" * 10)
        print(from_form_subscriber.is_valid())

        if from_form_subscriber.is_valid():
            new_subscriber = Subscriber()
            new_subscriber.firstname = from_form_subscriber.cleaned_data["firstname"]
            new_subscriber.lastname = from_form_subscriber.cleaned_data["lastname"]
            new_subscriber.email = from_form_subscriber.cleaned_data["email"]
            new_subscriber.save()

        return render(request=request, template_name="index.html",)