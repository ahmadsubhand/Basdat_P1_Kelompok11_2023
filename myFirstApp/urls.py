from django.urls import path
from . import views

urlpatterns = [
    # index.html
    path('', views.index, name='index'),
    path('login_patient/', views.login_patient, name='login_patient'),
    path('login_doctor/', views.login_doctor, name='login_doctor'),

    # login
    path('get_account_patient/', views.get_account_patient, name='get_account_patient'),
    path('get_account_doctor/', views.get_account_doctor, name='get_account_doctor'),
    path('main_patient/<int:id>/', views.main_patient, name='main_patient'),
    path('main_doctor/<int:id>/', views.main_doctor, name='main_doctor'),
    path('patient_register/', views.patient_register, name='patient_register'),

    # patient
    path('create_account/', views.create_account, name='create_account'),
    path('edit_account/', views.edit_account, name='edit_account'),

    # main
    path('patient_edit/<int:id>/', views.patient_edit, name='patient_edit'),
    path('reservation_create/<int:id>/', views.reservation_create, name='reservation_create'),
    path('reservation_edit/<int:id>/', views.reservation_edit, name='reservation_edit'),
    path('cancel_reservation/<int:id>/', views.cancel_reservation, name='cancel_reservation'),
    path('delete_reservation/<int:id>/', views.delete_reservation, name='delete_reservation'),
    path('accept_reservation/<int:id>/', views.accept_reservation, name='accept_reservation'),
    path('decline_reservation/<int:id>/', views.decline_reservation, name='decline_reservation'),
    path('message_patient/<int:id>/', views.message_patient, name='message_patient'),
    path('message_doctor/<int:id>/', views.message_doctor, name='message_doctor'),

    # reservation
    path('get_hospital/', views.get_hospital, name="get_hospital"),
    path('get_doctor/', views.get_doctor, name="get_doctor"),
    path('get_sessions/', views.get_sessions, name='get_sessions'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('edit_reservation/', views.edit_reservation, name='edit_reservation'),

    # message
    path('note_patient/', views.note_patient, name='note_patient'),
    path('note_doctor/', views.note_doctor, name='note_doctor'),
]
