from datetime import datetime
from api import register_booking    # Взаимодействие с бд у нас уже описано нашим коллегой в соседнем файле api.py
import json


class Booking:
    def __init__(self, room_name: str, start: datetime, end: datetime):
        self.room_name = room_name
        self.start = start
        self.end = end
        self.start_date = datetime.strftime(self.start, "%Y-%m-%d")
        self.end_date = datetime.strftime(self.start, "%Y-%m-%d")
        self.start_time = datetime.strftime(self.start, "%H:%M")
        self.end_time = datetime.strftime(self.end, "%H:%M")
        self.duration = int((self.end - self.start).total_seconds()/60)
        self.booking = {
            'room_name': self.room_name,
            'start_date': self.start_date,
            'start_time': self.start_time,
            'end_date': self.end_date,
            'end_time': self.end_time,
            'duration': self.duration
        }
        # self.booking_json = str(json.dumps(self.booking))

        if end < start:
            raise ValueError('datetime конца брони оказался раньше, чем datetime начала')


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


# result = create_booking("Sun", datetime(2022, 9, 1, 14), datetime(2022, 9, 1, 15, 15))
# print(result)

booking = Booking('Солнышко', datetime(2022, 9, 1, 14), datetime(2022, 9, 1, 15, 15))
print(booking.start_time)
booking.start = datetime(2022, 9, 1, 9)
print(booking.start_time)