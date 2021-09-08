from web.models import Subject
from django.shortcuts import render

# Create your views here.


def index (request):
    context = {}
    context['Subjects'] = Subject.objects.all()

    return render(request, 'index.html', context)


def detall(request, id):
    context = { }
    subjects = Subject.objects.filter(id=id)
    for subject in subjects:
        context['subject'] = subject
        
    return render(request, "detall.html", context)
    

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')