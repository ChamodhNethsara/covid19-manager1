
from django.urls import path
from . import views
app_name = 'manager'

urlpatterns = [
    path('',views.welcome,name='welcome'),
    
    path('all_patients/',views.all_patients,name='all_patients'),

    path('patient/<int:id>/',views.view_patient,name='view_patient'),

    path('add_patient/',views.add_patient,name='add_patient'),

    path('patient_added/',views.patient_added,name='patient_added'),

    path('search/<str:query>/',views.search_for_patient,name='search'),

]
