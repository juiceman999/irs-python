# app.py

from datetime import datetime, timedelta
import calendar
import app_query

class Appointment:
    def __init__(self, start_time, end_time, description=""):
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

class AppointmentManager:
    def __init__(self):
        self.appointments = {}

    def add_appointment(self, date, appointment):
        if date not in self.appointments:
            self.appointments[date] = []
        self.appointments[date].append(appointment)

    def display_schedule(self, date):
        if date in self.appointments:
            appointments = self.appointments[date]
            print(f"Schedule for {date}:")
            for appointment in appointments:
                print(f"{appointment.start_time} - {appointment.end_time}: {appointment.description}")
        else:
            print(f"No appointments scheduled for {date}")

    def select_appointment(self, date, start_time, end_time, description):
        appointment = Appointment(start_time, end_time, description)
        self.add_appointment(date, appointment)
        print(f"Appointment added on {date} from {start_time} to {end_time}: {description}")

    def display_calendar(self, year, month):
        cal = calendar.monthcalendar(year, month)
        for week in cal:
            for day in week:
                if day == 0:
                    print("   ", end=" ")  # Print empty space for days that are part of the previous or next month
                else:
                    appointments = self.appointments.get(f"{year}-{month:02d}-{day}", [])
                    if appointments:
                        print(f"[{day:2d}]", end=" ")  # Print day with appointments in brackets
                    else:
                        print(f"{day:2d} ", end=" ")  # Print day with no appointments
            print()  # Move to the next line after each week
