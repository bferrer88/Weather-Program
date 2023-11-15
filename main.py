import json, requests
import pprint

# Get all the specifications to build the URL
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "0031bc48948fbd8c353cc301f166b366"
city = input("Please enter the city or zip code you want to look at: ")

# Validate that user entered the information
while (city == ""):
    print("\nNo data has been entered.\n")
    city = input("Please enter the city or zip code you want to look at: ")


def main():

    # Build the URL
    url = f"{base_url}?q={city}&units=imperial&appid={appid}"
    print("\n")
    print(url)

    # Get data from the URL and use try except block to see if a connection was   #stablished
    try:
        response = requests.get(url)
        unformated_data = response.json()
       
    except:
        print("There was a problem when stablishing connection with the service")
    else:
        #formated_data = str(unformated_data.splitlines('\t'))
        print("\n")
        #pprint.pprint(unformated_data)
            
        def Retrieve_and_display_data():           
            # Retrieve data from the web page.
            feels_like = unformated_data['main']['feels_like']
            humidity = unformated_data['main']['humidity']
            pressure = unformated_data['main']['pressure']
            temp = unformated_data['main']['temp']
            max_temp = unformated_data['main']['temp_max']
            min_temp = unformated_data['main']['temp_min']
            wind_derees = unformated_data['wind']['deg']
            wind_speed = unformated_data['wind']['speed']

            # Display data in a readable style
            print(f"The temperature in {city} feels like {feels_like}")
            print(f"\nThe humidity in {city} is {humidity}")
            print(f"\nThe pressure in {city} is {pressure}")
            print(f"\nThe temperature in {city} is {temp}")
            print(f"\nThe maximum temperature in {city} is {max_temp}")
            print(f"\nThe minimum temperature in {city} is {min_temp}")
            print(f"\nThe wind in {city} has a speed of {wind_speed} m/s in {wind_derees} degrees")
        Retrieve_and_display_data()
        
main()
