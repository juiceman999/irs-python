# app_planning.py

from datetime import datetime
import calendar
import app_query

class AppointmentManager:
    def __init__(self):
        pass
    
    def add_appointment(self, username, date, start_time, end_time, description):
        app_query.add_appointment(username, date, start_time, end_time, description)

    def delete_appointment(self, appointment_id):
        app_query.delete_appointment(appointment_id)

    def display_schedule(self, username, date):
        appointments = app_query.get_schedule(username, date)
        
        if appointments:
            print(f"Schedule for {date}:")
            for appointment in appointments:
                print(f"ID: {appointment['id']}, {appointment['start_time']} - {appointment['end_time']}: {appointment['description']}")
        else:
            print(f"No appointments scheduled for {date}")

    def display_calendar(self, username, year, month):
        appointment_dates = app_query.get_appointment_dates(username, year, month)
        cal = calendar.monthcalendar(year, month)
        appointment_days = {date['date'].day for date in appointment_dates}
        
        for week in cal:
            for day in week:
                if day == 0:
                    print("   ", end=" ")  # Print empty space for days that are part of the previous or next month
                else:
                    if day in appointment_days:
                        print(f"[{day:2d}]", end=" ")  # Print day with appointments in brackets
                    else:
                        print(f"{day:2d} ", end=" ")  # Print day with no appointments
            print()  # Move to the next line after each week
