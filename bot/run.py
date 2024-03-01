import time
from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    time.sleep(3)
    bot.change_currency()
    bot.select_place_to_go("Phú Quốc")
    bot.select_dates("2023-12-16", "2023-12-18")
    bot.select_adults(7)
    print("Existing...")
time.sleep(1)