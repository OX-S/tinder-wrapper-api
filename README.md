# tinder-wrapper-api
TinderAPI is a Python class that provides a wrapper for the Tinder API. It allows you to perform various actions such as fetching your own profile, fetching nearby profiles, fetching a specific user's profile, swiping left or right on a user, and super liking a user.
Initialization

To use the TinderAPI, you will need to provide an auth_token. You can obtain this token by logging in to your Tinder account and inspecting the requests made by the Tinder web application.

To initialize the TinderAPI, you can do the following:

api = TinderAPI(auth_token)

Methods
self_profile()

This method returns the JSON data for your own profile.
fetch_nearby_users()

This method returns a list of JSON data for nearby users.
fetch_user(user_id)

This method takes a user ID of a valid Tinder profile and returns the JSON data for the requested profile.
swipe_left(user_id)

This method takes a user ID of a valid Tinder profile and swipes left, or passes, on that user. It returns the HTTP response.
swipe_right(user_id)

This method takes a user ID of a valid Tinder profile and swipes right, or likes, on that user. It returns the HTTP response.
super_like(user_id)

This method takes a user ID of a valid Tinder profile and super likes that user. It returns the HTTP response.

TinderProfile is a Python class that represents a Tinder profile. It contains the following attributes:

    name: the name of the profile
    user_id: the user ID of the profile
    distance: the distance to the profile, in miles
    bio: the profile's bio
    birth_date: the profile's birth date
    photos: a list of the profile's photos

The __init__ method of the TinderProfile class takes a dictionary of profile data as input and initializes the attributes of the profile.

You can create a TinderProfile object like this:

profile_data = {'name': 'John Smith', '_id': 'abc123', 'distance': 10, 'bio': 'I love hiking and good coffee.', 'birth_date': '1990-01-01', 'photos': ['photo1.jpg', 'photo2.jpg']}
profile = TinderProfile(profile_data)

