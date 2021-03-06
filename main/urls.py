from django.urls import path
from .views import detail, index, AddDoctor , AddNurse, AddPatient, singin, register, singout
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', detail, name='detail'),
    path('doctor/registration',AddDoctor.as_view(),name='adddoctor'),
    path('nurse/registration',AddNurse.as_view(),name='addnurses'),
    path('patient/registration',AddPatient.as_view(),name='addpatient'),
    path('register/',register,name='register'),
    path('singin/',singin,name='singin'),
    path('singout/',singout,name='singout')
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
