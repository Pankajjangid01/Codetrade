import requests
import json

class Whether:
    """
        Description: Whether class to find the whether of particular city and store them in the csv file
    """
    def __init__(self):
        """
            Description: Constructor to initialize the city, api_key, base_url
        """
        self.city = input("Enter the city name: ")
        self.api_key = "59800ef702cbdd4b0b4949f955e24f7f"  # open whether api key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"  # base url of the open whether api
        self.complete_url = self.base_url + "appid=" + self.api_key + "&q=" + self.city  # api to search on the basis of city name 

    def find_whether(self):
        """
            Description: Method to find the whether of the particular city and extract the humidity, temperature, pressure, wind_speed 
        """
        try:
            print("Fetching data...")
            self.api_response = requests.get(self.complete_url).text  # pull the data from api 
            self.parse_data = json.loads(self.api_response)  # parse the data into json format
            self.humidity = self.parse_data['main']['humidity']  # extract the humitdity
            self.temperature = self.parse_data['main']['temp']  # extract the temperature
            self.pressure = self.parse_data['main']['pressure']  # extract the pressure
            self.wind_speed = self.parse_data['wind']['speed']  # extract the wind speed
            print(f"Whether Details of {self.city}:\nHumidity: {self.humidity}, Temprature: {self.temperature}, Pressure: {self.pressure}, Wind Speed:{self.wind_speed}")  # printing the extracted details 
            self.store_whether_details()  # call the store whether method to store whether details in csv file 

        except requests.exceptions.HTTPError:
            print(f"Error fetching data:")

    def store_whether_details(self):
        """
            Description: This class store the whether details of the city to the csv file  
        """
        try:
            print("saving whether details...")
            with open('whether.csv','a') as whether_file:
                if whether_file.tell() == 0:  # check if it is header or not, if it is header then write header in the file 
                    whether_file.write("City Name,Humidity,Temprature,Pressure,Wind Speed\n")
                
                whether_file.write(f"{self.city},{self.humidity},{self.temperature},{self.pressure},{self.wind_speed}\n")  #write details in each row 
                print("Whether Details saved successfully...")
        
        except IOError:
            print(f"Error in saving the Whether details: {str(IOError)}")


Whether().find_whether()  # callling the find_whether method 

# pankaj-kumar@pankaj-kumar-HP-Pavilion-Gaming-Laptop-15-ec2xxx:~/Codetrade/api_integration$ /usr/bin/python3 /home/pankaj-kumar/Codetrade/api_integration/whether_details.py
# Enter the city name: cdgd
# Fetching data...
# Traceback (most recent call last):
#   File "/home/pankaj-kumar/Codetrade/api_integration/whether_details.py", line 52, in <module>
#     Whether().find_whether()  # callling the find_whether method 
#     ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/pankaj-kumar/Codetrade/api_integration/whether_details.py", line 25, in find_whether
#     self.humidity = self.parse_data['main']['humidity']  # extract the humitdity
#                     ~~~~~~~~~~~~~~~^^^^^^^^
# KeyError: 'main'


# here is the response of api-->>{"coord":{"lon":75.8167,"lat":26.9167},"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations","main":{"temp":288.77,"feels_like":288.14,"temp_min":288.77,"temp_max":288.77,"pressure":1019,"humidity":67,"sea_level":1019,"grnd_level":971},"visibility":1700,"wind":{"speed":2.57,"deg":210},"clouds":{"all":0},"dt":1737102423,"sys":{"type":1,"id":9170,"country":"IN","sunrise":1737078412,"sunset":1737116776},"timezone":19800,"id":1269515,"name":"Jaipur","cod":200}