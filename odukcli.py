import requests
import click

@click.command()
def cli():
	draw_header()
	# get the location of the user
	location = requests.get("http://ipinfo.io")
	location_dict = location.json()
	location_arr = location_dict['loc'].split(',')
	lat = location_arr[0]
	lon = location_arr[1]
	# make an API call to open weather map
	API_KEY = "53354025be63db77ec719572983b851d"
	weather = requests.get("http://api.openweathermap.org/data/2.5/weather?units=metric&lat={}&lon={}&APPID={}".format(lat,lon,API_KEY))
	weather_dict = weather.json()
	description = weather_dict['weather'][0]['description']
	country = weather_dict['sys']['country']
	city = weather_dict['name']
	temperature = weather_dict['main']['temp']



	click.echo("You are currently in {},{}\n".format(city,country))
	click.echo("The temperature is {} degrees celcius\n".format(temperature))
	click.echo("You have {}\n".format(description))

def draw_header():
    click.echo('\n')
    click.echo('*' * 100)
    click.echo('*' + ' ' * 98 + '*')
    click.echo('*' + ' ' * 98 + '*')
    click.echo('*' + ' ' * 40 + 'THE WEATHER MAN!! ' + ' ' * 40+ '*')
    click.echo('*' + ' ' * 98 + '*')
    click.echo('*' + ' ' * 98 + '*')
    click.echo('*' * 100)
    click.echo('\n')