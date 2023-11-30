from django.db import models
from datetime import date

# Create your models here.
class Patient(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, default='a')
    last_name = models.CharField(max_length=200, default='a')
    gender = models.CharField(max_length=1, default='m')
    birth_date = models.DateField(default=date(2003, 10, 2))

    @property
    def age(self):
      if self.birth_date:
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
      return None


class Doctor(models.Model):
  username = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  first_name = models.CharField(max_length=200, default='a')
  last_name = models.CharField(max_length=200, default='a')
  gender = models.CharField(max_length=1, default='m')
  birth_date = models.DateField(default='2003-10-02')
  session = models.CharField(max_length=200, default='a,a')
  day = models.CharField(max_length=200, default='a,a')
  id_hospital = models.CharField(max_length=200)

  def set_sessions(self, sessions):
    self.session = ','.join(sessions)

  def get_sessions(self):
    return self.session.split(',')

  def set_days(self, days):
    self.day = ','.join(days)

  def get_days(self):
    return self.day.split(',')
  
  @property
  def age(self):
    if self.birth_date:
      today = date.today()
      age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
      return age
    return None

class Session(models.Model):
  start = models.TimeField()
  end = models.TimeField()

class Hospital(models.Model):
  location = models.CharField(max_length=200)
  address = models.CharField(max_length=200)

class Reservation(models.Model):
  date = models.DateField(null=True, blank=True)
  status = models.CharField(max_length=200, default='menunggu')
  message_patient = models.TextField(default='')
  message_doctor = models.TextField(default='')
  id_patient = models.CharField(max_length=200)
  id_hospital = models.CharField(max_length=200)
  id_doctor = models.CharField(max_length=200)
  id_session = models.CharField(max_length=200, default='1')