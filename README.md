**I am The Astro Goose. I detect Asteroids. Honk!**

More specifically, I am a twitter bot which tweets automatically about Near Earth Objects (NEOs). I get my data from NASA JPL's NEO database utilizing a REST API. The code uses the Tweepy library to connect to the twitter account (@theAstroGoose check it out) and send the tweet contents. 


**AsteroidDetection.py:**

Processes data from database and categorizes into object for easy data organization. The object stores the following for each asteroid: name (NEO name), time (time of passing), date (date of passing), missDist (distance from Earth), speed (NEO speed), hazard (is it hazardous), and size (size of NEO).

**AsteroidDetection.py:**

Contains the tweet() method that I created to simplify connecting to the twitter account. It stores the credentials (now redacted) for logging into the account.

**AsteroidGoose.py:**

Does the hard work of compiling the tweet content and passing it to the tweet() method. It contains a series of settings for processing data, for example tweetWeeklySummary(false) would create a string for the tweet, but because the false boolean was passed the tweet will not be published.

**Usage**

I used a Raspberry Pi 4 that runs a daily cron job for running the AstroGoose program. I also created a series of preset commands to simplify the process of running the script, so for example the server simply runs the command 'python3 AsteroidGoose.py 0' to run the daily report, and 'python3 AsteroidGoose.py 1' to run the weekly report.

Finally, this was just a fun project incorporating a series of things 
