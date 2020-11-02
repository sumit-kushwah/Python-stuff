import webbrowser
import sys

if len(sys.argv) > 1:
    city = ' '.join(sys.argv[1:])
else:
    print("Please enter city name.")

url = 'https://www.accuweather.com/en/in/' + city + '/'
webbrowser.open(url)


