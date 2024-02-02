from datetime import datetime
from api import register_booking    # Взаимодействие с бд у нас уже описано нашим коллегой в соседнем файле api.py
import json


class Booking:
    def __init__(self, room_name: str, start: datetime, end: datetime):
        if end < start:
            raise ValueError('datetime конца брони оказался раньше, чем datetime начала')
        self.room_name = room_name
        self.start = start
        self.end = end
        self.booking = {
            'room_name': self.room_name,
            'start_date': self.start_date,
            'start_time': self.start_time,
            'end_date': self.end_date,
            'end_time': self.end_time,
            'duration': self.duration
        }

    @property
    def start_date(self):
        return datetime.strftime(self.start, "%Y-%m-%d")

    @property
    def end_date(self):
        return datetime.strftime(self.end, "%Y-%m-%d")

    @property
    def start_time(self):
        return datetime.strftime(self.start, "%H:%M")

    @property
    def end_time(self):
        return datetime.strftime(self.end, "%H:%M")

    @property
    def duration(self):
        return int((self.end - self.start).total_seconds()/60)


def create_booking(room_name, start, end) -> str:
    b = {}
    print('Начинаем создание бронирования')
    booking = Booking(room_name, start, end)
    try:
        if not register_booking(booking):
            b['created'] = False
            b['msg'] = 'Комната занята'
        else:
            b['created'] = True
            b['msg'] = 'Бронирование создано'
    except KeyError:
        b['created'] = False
        b['msg'] = "Комната не найдена"
    finally:
        print("Заканчиваем создание бронирования")
    b['booking'] = booking.booking
    return json.dumps(b)
