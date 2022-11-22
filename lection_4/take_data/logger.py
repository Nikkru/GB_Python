from datetime import datetime as dt


def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{};temperature;{} C ".
                   format(time, data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{};pressure;{} mm Hg ".
                   format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{};wind_speed;{} m/c ".
                   format(time, data))


def hunidity_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{};humidity;{} %\n".
                   format(time, data))