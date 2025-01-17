""" Imported json and request library """
import requests

class Whether:
    """
        Description: Whether class to find the whether of particular city and store them in the csv file
    """
    def __init__(self):
        """
            Description: Constructor to initialize the city, api_key, base_url
        """
        self.city = input("Enter the city/State name: ")  # take the city form user 
        self.humidity = None
        self.temperature = None
        self.wind_speed = None
        self.api_response = None
        self.parse_data = None
        self.pressure = None

    def find_whether(self):
        """
            Description: Method to find the whether of the particular cit+y and extract the humidity, temperature, pressure, wind_speed
        """
        try:
            print("Fetching data...")
            self.api_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid=59800ef702cbdd4b0b4949f955e24f7f&units=metric").text  # pull the data from api
            self.parse_data = eval(self.api_response)  # parse the data 
            self.country = self.parse_data['sys']['country']
            if self.country == 'IN':
                main_data = self.parse_data.get('main', None)
                wind_data = self.parse_data.get('wind', None)
                self.humidity = main_data.get('humidity', main_data.get('Humidity', 'N/A'))  # Check both lowercase and capitalized
                self.temperature = main_data.get('temp', 'N/A')
                self.pressure = main_data.get('pressure', 'N/A')
                self.wind_speed = wind_data.get('speed', 'N/A')
                self.store_whether_details()  # call the store whether method to store whether details in csv file
                return f"Whether Details of {self.city}:\nHumidity: {self.humidity}\nTemprature: {self.temperature}\nPressure: {self.pressure}\nWind Speed:{self.wind_speed}"  # printing the extracted details
            else:
                return f"Please Enter city/state of India"
        except KeyError as key:
            return f"Error fetching data:{key}"

    def store_whether_details(self):
        """
            Description: This class store the whether details of the city to the csv file
        """
        try:
            print("saving whether details...")
            with open('whether.csv','a') as whether_file:
                if whether_file.tell() == 0:  # check if it is header or not, if it is header then write header in the file
                    whether_file.write("City-Name,Humidity,Temprature,Pressure,Wind Speed\n")
                whether_file.write(f"{self.city.lower()},{self.humidity},{self.temperature},{self.pressure},{self.wind_speed}\n")  #write details in each row 
                print("Whether Details saved successfully...")
        except IOError:
            return f"Error in saving the Whether details: {IOError}"
        
print(Whether().find_whether())  # callling the find_whether method
