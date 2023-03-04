from django.shortcuts import render
from .models import Project, Work, Education, Contact, Skills, Hobbies, IndexBody

# Create your views here.
def index(request):
    context={
        'IndexBody':IndexBody.objects.all()
         
    }
    return render(request, 'index.html',{'title':'homepage'})

def cv(request):
    context= {
        'title':'My Cv',
        'Education':Education.objects.all(),
        'Hobbies':Hobbies.objects.all(),
        'Contact': Contact.objects.all(),
        'Skills':Skills.objects.all(),
        'works': Work.objects.all()
    }
    return render(request, 'cv.html',context)

def hireme(request):
    return render(request, 'hire-me.html',{'title':'Hireme'})

def projects(request):
    context = {
        'title':'projects',
        'projects':Project.objects.all()
    }
    return render(request, 'projects.html',context)

 