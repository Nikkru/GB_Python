from random import randint


def get_temperature(senser):
    return randint(-20, 0) if senser else randint(0, 20)


def get_pressure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)


def get_wind_speed(sensor):
    if sensor:
        return randint(0, 30)
    else:
        return randint(30, 50)


def get_humidity(sensor):
    if sensor:
        return randint(50, 85)
    else:
        return randint(40, 50)


def data_collection():
    return (get_temperature(1), get_pressure(1), get_wind_speed(1), get_humidity(1))