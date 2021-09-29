from django.shortcuts import render
from .models import Hospital, Doctor, MainDoctor,Patients
from django.views.generic import CreateView
from .forms import *

def index(request):
    hospitals = Hospital.objects.all()
    return render(request, 'index.html', {'hospitals':Hospital.objects.all()})

def detail(request, pk):
    hospital_detail = Hospital.objects.get(pk=pk)
    doctor_detail = Doctor.objects.filter(hospital=pk)
    patients_detail = Patients.objects.filter(doctor=pk)

    context = {
        'hospital_detail':hospital_detail,
        'doctor_detail':doctor_detail,
        'patients_detail':patients_detail
    }
    return render(request, "detail.html", context)


class AddDoctor(CreateView):
    form_class = AddDoctor
    template_name = "addnew.html"
    raise_exception = True

class AddNurse(CreateView):
    form_class = AddNurses
    template_name = 'addnew.html'
    raise_exception = True

class AddPatient(CreateView):
    form_class = AddPatients
    template_name = 'addnew.html'
    raise_exception = True
