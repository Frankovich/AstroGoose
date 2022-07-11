import asteroidDetection as detector
from asteroidMonitoring import tweet
import tweepy
import sys


def tweetWeeklySummary(tweetLive):
    asteroidList = detector.get_asteroids(6)

    nearest = detector.get_nearest(asteroidList)
    largest = detector.get_largest(asteroidList)

    tweetContent = f'This week, there are {len(asteroidList)} "Near Earth Objects" ☄️🔭 passing Earth. \nThe closest object is {nearest.name} which will pass on {(nearest.date)} at {nearest.time} GMT. It will be {float(nearest.missDist):,} kms from Earth. The biggest object is {largest.name}, which has a max size of {largest.size} kilometers. Woah🪨👽! \n#NASA #asteroid #SPACE'

    print(tweetContent)

    if (tweetLive == True):
        try:
            tweet(tweetContent)
            print(f'\nTweet sent successfully HASHTAGS: Yes')
        except tweepy.errors.BadRequest:
            tweetContent = f'This week, there are {len(asteroidList)} "Near Earth Objects" ☄️🔭 passing Earth. \nThe closest object is {nearest.name} which will pass on {(nearest.date)} at {nearest.time} GMT. It will be {float(nearest.missDist):,} kms from Earth. The biggest object is {largest.name}, which has a max size of {largest.size} kilometers. Woah🪨👽! \n'

            tweet(tweetContent)
            print(f'\nTweet sent successfully HASHTAGS: Yes')
    else:
        print(f'\nTweet was not posted because tweetLive is set to "False"')


def tweetDailySummary(tweetLive):
    asteroidList = detector.get_asteroids(0)

    nearest = detector.get_nearest(asteroidList)

    tweetContent = f'☄️🔭 Today, there are {len(asteroidList)} "Near Earth Objects" passing Earth.\nThe closest object is {nearest.name} which will pass at {nearest.time} GMT. It will be {float(nearest.missDist):,} kms from Earth 🌎. Honk. \n#NASA #asteroid #SPACE'

    print(tweetContent)

    if (tweetLive == True):
        try:
            tweet(tweetContent)
            print(f'\nTweet sent successfully HASHTAGS: Yes')
        except tweepy.errors.BadRequest:
            tweetContent = f'☄️🔭 Today, there are {len(asteroidList)} "Near Earth Objects" passing Earth.\n The closest object is {nearest.name} which will pass at {nearest.time} GMT. It will be {float(nearest.missDist):,} kms from Earth 🌎. Honk. \n#NASA #asteroid #SPACE'

            tweet(tweetContent)
            print(f'\nTweet sent successfully HASHTAGS: Yes')
    else:
        print(f'\nTweet was not posted because tweetLive is set to "False"')


def tweetNearPotentiallyHazardous(tweetLive):
    asteroidList = detector.get_asteroids(2)

    hazards = detector.get_hazards(asteroidList)
    nearest = detector.get_nearest(hazards)
    missDistVar = f'{float(nearest.missDist):,}'

    tweetContent = f'👽POTENTIALLY HAZARDOUS OBJECT REPORT🚀 \n\nThere are {len(hazards)} hazardous objects in the next three days. \nThe closest will be {nearest.name} will pass at {nearest.time} on {nearest.date}. It will be {float(nearest.missDist):,} kms from Earth 🌎. Stay safe. \n#NASA #asteroid #SPACE'

    print(tweetContent)

    if (tweetLive == True):
        try:
            tweet(tweetContent)
            print(f'Tweet sent successfully HASHTAGS: Yes')
        except tweepy.errors.BadRequest:
            tweetContent = f'👽POTENTIALLY HAZARDOUS OBJECT REPORT🚀 \n\nThere are {len(hazards)} hazardous objects in the next three days. \nThe closest will be {nearest.name} will pass at {nearest.time} on {nearest.date}. It will be {float(nearest.missDist):,} kms from Earth 🌎. Stay safe.\n'

            tweet(tweetContent)
            print(f'Tweet sent successfully HASHTAGS: No')
    else:
        print(f'Tweet was not posted because tweetLive is set to "False"')


def testTweet(tweetLive):
    asteroidList = detector.get_asteroids(0)

    nearest = detector.get_nearest(asteroidList)

    tweetContent = f'☄️🔭 Today, there are {len(asteroidList)} "Near Earth Objects" passing Earth. The closest object is {nearest.name} which will pass at {nearest.time} GMT. \nIt will be {float(nearest.missDist):,} kms from Earth 🌎. Honk. #NASA #asteroid #SPACE'

    print(tweetContent)

    if (tweetLive == True):
        try:
            tweet(tweetContent)
            print(f'Tweet sent successfully HASHTAGS: Yes')
        except tweepy.errors.BadRequest:
            tweetContent = f'☄️🔭 Today, there are {len(asteroidList)} "Near Earth Objects" passing Earth. The closest object is {nearest.name} which will pass at {nearest.time} GMT. \nIt will be {float(nearest.missDist):,} kms from Earth 🌎. Honk.'

            tweet(tweetContent)
            print(f'Tweet sent successfully HASHTAGS: No')
    else:
        print(f'Tweet was not posted because tweetLive is set to "False"')


def tempTweet(tweetLive):
    tweetContent = f'Please Ignore'
    print(tweetContent)
    if (tweetLive == True):
        tweet(tweetContent)
    else:
        print(f'Tweet was not posted because tweetLive is set to "False"')


if sys.argv[1] == '0':
    tweetDailySummary(True)
elif sys.argv[1] == '1':
    tweetWeeklySummary(True)
elif sys.argv[1] == '2':
    tweetNearPotentiallyHazardous(True)
elif sys.argv[1] == '3':
    testTweet(False)
elif sys.argv[1] == '4':
    tweetNearPotentiallyHazardous(False)
else:
    print(f"invalid option")
