from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .models import Patient, Doctor, Hospital, Session, Reservation
from django.http import JsonResponse

#----------------------------------------------------------------------------------------------------

# index.html 

def index(request):
    return render(request, 'index.html')

def login_patient(request):
    return render(request, 'login_patient.html')

def login_doctor(request):
    return render(request, 'login_doctor.html')

#----------------------------------------------------------------------------------------------------

# login

def main_patient(request, id):
    patient = Patient.objects.get(id=id)
    reservasi = Reservation.objects.filter(id_patient=id).order_by('date', 'id_session')
    if not reservasi.exists():
        kosong = mark_safe('<div class="kosong">There is no reservation schedule</div>')
        none = mark_safe('style="display: none;"')
    else:
        kosong = "" 
        none = ""
    reservation_details = []
    for i in reservasi:
        doctor = Doctor.objects.get(id=i.id_doctor)
        hospital = Hospital.objects.get(id=i.id_hospital)
        session = Session.objects.get(id=i.id_session)
        reservation = Reservation.objects.get(id=i.id)
        reservation_detail = {
            'doctor': doctor,
            'hospital': hospital,
            'session': session,
            'reservation': reservation,
        }
        reservation_details.append(reservation_detail)
    context = {
        'kosong': kosong,
        'none': none,
        'patient': patient,
        'reservation_details': reservation_details,
    }
    return render(request, 'main_patient.html', context)

def main_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    reservasi = Reservation.objects.filter(id_doctor=id).order_by('date', 'id_session')
    if not reservasi.exists():
        kosong = mark_safe('<div class="kosong">There is no reservation schedule</div>')
        none = mark_safe('style="display: none;"')
    else:
        kosong = "" 
        none = ""
    reservation_details = []
    for i in reservasi:
        patient = Patient.objects.get(id=i.id_patient)
        hospital = Hospital.objects.get(id=i.id_hospital)
        session = Session.objects.get(id=i.id_session)
        reservation = Reservation.objects.get(id=i.id)
        reservation_detail = {
            'patient': patient,
            'hospital': hospital,
            'session': session,
            'reservation': reservation,
        }
        reservation_details.append(reservation_detail)
    context = {
        'kosong': kosong,
        'none': none,
        'doctor': doctor,
        'reservation_details': reservation_details,
    }
    return render(request, 'main_doctor.html', context)

def get_account_patient(request):
    username = request.POST['username']
    password = request.POST['password']
    akun = Patient.objects.filter(username=username, password=password)
    if akun.exists():
        return redirect('/main_patient/' + str(akun.first().id) + '/')
    else:
        context = {
            'alert': mark_safe('<div class="alert"> *Your username or password is incorect </div>')
        }
        return render (request, 'login_patient.html', context)
        

def get_account_doctor(request):
    username = request.POST['username']
    password = request.POST['password']
    akun = Doctor.objects.filter(username=username, password=password)
    if akun.exists():
        return redirect('/main_doctor/' + str(akun.first().id) + '/')
    else:
        context = {
            'alert': mark_safe('<div class="alert"> *Your username or password is incorect </div>'),
        }
        return render (request, 'login_doctor.html', context)
    

def patient_register(request):
    return render(request, 'patient_register.html')

#----------------------------------------------------------------------------------------------------

# Patient

def create_account(request):
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birth_date = request.POST['birth_date']
    gender = request.POST['gender']

    patient = Patient.objects.filter(username=username)
    if patient.exists():
        context = {
            'alert': mark_safe('<div class="alert"> *Username already taken, please create another one </div>'),
        }
        return render(request, 'patient_register.html', context)
    else:
        akun = Patient(username=username, password=password, first_name=first_name, last_name=last_name,
                        gender=gender, birth_date=birth_date)
        akun.save()
        return redirect('/main_patient/' + str(akun.id) + '/')

def edit_account(request):
    id = request.POST['id']
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birth_date = request.POST['birth_date']
    gender = request.POST['gender']

    akun = Patient.objects.get(id=id)
    akun.username = username
    akun.first_name = first_name
    akun.last_name = last_name
    akun.birth_date = birth_date
    akun.gender = gender
    akun.save()

    return redirect('/main_patient/' + str(akun.id) + '/')

#----------------------------------------------------------------------------------------------------

# Main

# Patient 
def patient_edit(request, id):
    akun = Patient.objects.get(id=id)
    akun.birth_date = akun.birth_date.strftime('%Y-%m-%d')
    context = {
        'akun': akun,
    }
    return render(request, 'patient_edit.html', context)

def reservation_create(request, id):
    patient = Patient.objects.get(id=id)
    hospital = Hospital.objects.all()
    location_details = []
    for i in hospital:
        location_detail = {
            'location': i.location
        }
        location_details.append(location_detail)
    context = {
        'patient': patient,
        'location_details': location_details,
    }
    return render(request, 'reservation_create.html', context)

def reservation_edit(request, id):
    reservasi = Reservation.objects.get(id=id)
    hospital = Hospital.objects.get(id=reservasi.id_hospital)
    patient = Patient.objects.get(id=reservasi.id_patient)
    location = hospital.location
    reservasi.date = reservasi.date.strftime('%Y-%m-%d')

    hospitals = Hospital.objects.all()
    location_details = []
    for i in hospitals:
        location_detail = {
            'location': i.location
        }
        location_details.append(location_detail)

    context = {
        'reservation': reservasi,
        'patient': patient,
        'location': location,
        'location_details': location_details,
    }
    return render(request, 'reservation_edit.html', context)

def cancel_reservation(request, id):
    reservasi = Reservation.objects.get(id=id)
    reservasi.status = "ditolak"
    reservasi.save()
    return redirect('/main_patient/' + str(reservasi.id_patient) + '/')

def delete_reservation(request, id):
    reservasi = Reservation.objects.get(id=id)
    patient_id = reservasi.id_patient
    reservasi.delete()
    return redirect('/main_patient/' + str(patient_id) + '/')

def message_patient(request, id):
    reservasi = Reservation.objects.get(id=id)
    context = {
        'reservasi': reservasi,
    }
    return render(request, 'message_patient.html', context)

# Doctor

def accept_reservation(request, id):
    reservasi = Reservation.objects.get(id=id)
    reservasi.status = "diterima"
    reservasi.save()
    return redirect('/main_doctor/' + str(reservasi.id_doctor) + '/')

def decline_reservation(request, id):
    reservasi = Reservation.objects.get(id=id)
    reservasi.status = "ditolak"
    reservasi.save()
    return redirect('/main_doctor/' + str(reservasi.id_doctor) + '/')

def message_doctor(request, id):
    reservasi = Reservation.objects.get(id=id)
    context = {
        'reservasi': reservasi,
    }
    return render(request, 'message_doctor.html', context)

#----------------------------------------------------------------------------------------------------

# Reservation
def get_hospital(request):
    location = request.GET.get('location')
    hospitals = Hospital.objects.filter(location=location).values('id', 'address')
    return JsonResponse(list(hospitals), safe=False)

def get_doctor(request):
    hospital_id = request.GET.get('hospital_id')
    date_id = request.GET.get('date_id')

    # Filter doctors based on hospital and date
    doctors = Doctor.objects.filter(id_hospital=hospital_id, day__contains=date_id).values('id', 'first_name')

    return JsonResponse(list(doctors), safe=False)

def get_sessions(request):
    doctor_id = request.GET.get('doctor_id')
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        doctor_sessions = doctor.get_sessions()
        sessions = Session.objects.filter(id__in=doctor_sessions).values('id', 'start', 'end')
        return JsonResponse(list(sessions), safe=False)
    except Doctor.DoesNotExist:
        return JsonResponse([], safe=False)
    
def create_reservation(request):
    patient_id = request.POST['pasien']
    date = request.POST['date']
    session_id = request.POST['session']
    hospital_id = request.POST['hospital']
    doctor_id = request.POST['dokter']
    reservation = Reservation(date=date, id_patient=patient_id, id_hospital=hospital_id, id_doctor=doctor_id, id_session=session_id)
    reservation.save()
    return redirect('/main_patient/' + str(patient_id) + '/')

def edit_reservation(request):
    reservation_id = request.POST['reservasi']
    date = request.POST['date']
    session_id = request.POST['session']
    hospital_id = request.POST['hospital']
    doctor_id = request.POST['dokter']

    reservasi = Reservation.objects.get(id=reservation_id)
    reservasi.date = date
    reservasi.id_session = session_id
    reservasi.id_hospital = hospital_id
    reservasi.id_doctor = doctor_id
    reservasi.status = "menunggu"
    reservasi.message_doctor = ""
    reservasi.message_patient = ""
    reservasi.save()

    return redirect('/main_patient/' + str(reservasi.id_patient) + '/')

#----------------------------------------------------------------------------------------------------

# Message

def note_patient(request):
    id = request.POST['id']
    message = request.POST['message']
    reservasi = Reservation.objects.get(id=id)
    reservasi.message_patient = message
    reservasi.save()
    return redirect('/main_patient/' + str(reservasi.id_patient) + '/')

def note_doctor(request):
    id = request.POST['id']
    message = request.POST['message']
    reservasi = Reservation.objects.get(id=id)
    reservasi.message_doctor = message
    reservasi.save()
    return redirect('/main_doctor/' + str(reservasi.id_doctor) + '/')