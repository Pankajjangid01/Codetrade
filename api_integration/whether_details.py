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

        except requests.exceptions.HTTPError as errh:
            print(f"Error fetching data: {str(errh)}")

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