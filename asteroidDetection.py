import json
from re import S
import requests
from datetime import datetime, timedelta
from collections import OrderedDict
import pprint

class asteroid():
    def __init__(self, name, time, date, missDist, speed, hazard, size):  
        self.name = name 
        self.time = time
        self.date = date
        self.missDist = missDist
        self.speed = speed
        self.hazard = hazard
        self.size = size

def get_asteroids(duration = 1):
    end = (datetime.now() + timedelta(days=duration)).strftime('%Y-%m-%d')
    start = datetime.now().strftime('%Y-%m-%d')

    nasa_keys = '****************'
    apiLink = 'https://api.nasa.gov/neo/rest/v1/feed?start_date='+ start + '&end_date=' + end + '&api_key=' + nasa_keys

    response = requests.get(apiLink)
    data = json.loads(response.content)
    data = data['near_earth_objects']
    listOfAsteroids = sorted(data.items(), key = lambda x:datetime.strptime(x[0], '%Y-%m-%d'), reverse=True)

    astList = []
    for day in listOfAsteroids:
        for ast in day[1]:
            astName = ast['name']
            dateAndTime = (ast['close_approach_data'][0]['close_approach_date_full']).split()
            astApproachTime = dateAndTime[1]
            astApproachDate = dateAndTime[0]
            astMissDistance = float(ast['close_approach_data'][0]['miss_distance']['kilometers'])
            astSpeed = float(ast['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
            astMissDistance = str("{:.2f}".format(astMissDistance))
            astSpeed = str("{:.2f}".format(astSpeed))
            hazard = ast['is_potentially_hazardous_asteroid']
            size = str("{:.2f}".format(float(ast['estimated_diameter']['kilometers']['estimated_diameter_max'])))
            
            a = asteroid(astName, astApproachTime, astApproachDate, astMissDistance, astSpeed, hazard, size)
            astList.append(a)
    
    return astList

def get_nearest(asteroid_list):
    nearestAsteroid = asteroid('blank', 0, 0, '99000000000', 0, 0, 0)
    for ast in asteroid_list:
        if float(ast.missDist) < float(nearestAsteroid.missDist):
            nearestAsteroid = ast
    return nearestAsteroid

def get_largest(asteroid_list):
    nearestAsteroid = asteroid('blank', 0, 0, '99000000000', 0, 0, '0')
    for ast in asteroid_list:
        if float(ast.size) > float(nearestAsteroid.size):
            nearestAsteroid = ast
    return nearestAsteroid

def get_hazards(asteroid_list):
    hazards = []
    for ast in asteroid_list:
        if ast.hazard:
            hazards.append(ast)
    return hazards

if __name__ == '__main__':
    list = get_asteroids(0) #0 is day 1
    
