from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view
from user_interface import humidity_view

def create(device = 1):
    style = 'style = "font-size:22px;"'
    html = '<html>\n  <head></head>\n'
    html += '    <p {}>Temperature: {} C</p>\n'\
        .format(style, temperature_view(device))
    html += '    <p {}>Pressure: {} m/s</p>\n' \
        .format(style, pressure_view(device))
    html += '    <p {}>Winter_speed: {} mmHg</p>\n' \
        .format(style, wind_speed_view(device))
    html += '    <p {}>Humidity: {} %</p>\n' \
        .format(style, humidity_view(device))
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html


def new_create(data):
    t, p, w, h = data
    t = t * 1.8 + 32
    style = 'style = "font-size:22px;"'
    html = '<html>\n  <head></head>\n'
    html += '    <p {}>Temperature: {} F</p>\n'\
        .format(style, t)
    html += '    <p {}>Pressure: {} m/s</p>\n' \
        .format(style, p)
    html += '    <p {}>Winter_speed: {} mmHg</p>\n' \
        .format(style, w)
    html += '    <p {}>Humidity: {} %</p>\n' \
        .format(style, h)
    html += '  </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data