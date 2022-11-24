import requests


# API wrapper class for the Tinder API
class TinderAPI:
    base_url = 'https://api.gotinder.com'

    # initializes TinderAPI class and saves own profile as self.profile
    def __init__(self, auth_token):

        # request headers
        self.headers = {'x-auth-token': auth_token,
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0',
                        'platform': 'web'}

        # tries to request user account
        try:
            r = requests.get(self.base_url + '/v2/profile?locale=en&include=account%2Cuser', headers=self.headers)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        data = r.json()
        self.profile = data['data']['user']

    # returns json data containing data of own profile
    def self_profile(self):
        return self.profile

    # returns json data containing nearby profiles
    def fetch_nearby_users(self):
        try:
            r = requests.get(self.base_url + '/v2/recs/core?locale=en', headers=self.headers)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        users = r.json()
        return users['data']['results']

    # takes user ID of valid tinder profile, returns json data of requested profile
    def fetch_user(self, user_id):
        try:
            r = requests.get(f"{self.base_url}/user/{user_id}", headers=self.headers)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return r.json()['results']

    # swipes left, or passes on given user and returns HTTP response
    def swipe_left(self, user_id):
        try:
            r = requests.get(f"{self.base_url}/pass/{user_id}", headers=self.headers)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return r

    # swipes right, or likes given user and returns HTTP response
    def swipe_right(self, user_id):
        try:
            r = requests.get(f"{self.base_url}/like/{user_id}", headers=self.headers)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        return r

    # super likes given profile and returns HTTP response
    def super_like(self, user_id):
        headers = {'x-auth-token': self.headers['x-auth-token'],
                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0',
                   'platform': 'web',
                   'Content-Type': 'application/json; charset=utf-8'
                   }
        try:
            r = requests.post(f"{self.base_url}/like/{user_id}/super", headers=headers)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        return r


# Object class for a Tinder profile
class TinderProfile:

    # init method for TinderProfile
    def __init__(self, profile):

        # saves the profile name
        self.name = profile['name']

        # saves the profiles user ID
        self.user_id = profile['_id']

        # attempts to save the distance to profile if distance is displayed, otherwise saves distance as -1
        try:
            self.distance = profile['distance']
        except KeyError:
            self.distance = -1
        self.bio = profile['bio']

        # saves all schools into a list
        self.schools = []
        try:
            for s in profile['schools']:
                self.schools.append(s['name'])
        except KeyError:
            pass

        # saves city if city is displayed on profile, otherwise saves city as None
        try:
            self.city = profile['city']['name']
        except KeyError:
            self.city = None

        # saves url to profile images in list
        self.images = []
        for p in profile['photos']:
            self.images.append(p['url'])

        # saves gender if given, else saves gender as None
        try:
            self.gender = profile['gender']
        except KeyError:
            self.gender = None

    # returns profile name
    def get_name(self):
        return self.name

    # returns profile ID
    def get_id(self):
        return self.user_id

    # returns profile distance
    def get_distance(self):
        return self.distance

    # returns profile bio
    def get_bio(self):
        return self.bio

    # returns list of schools profile has attended, returns empty list if none found
    def get_schools(self):
        return self.schools

    # returns profile of city if profile has city displayed, otherwise returns None
    def get_city(self):
        return self.city

    # returns list of image urls attached to profile
    def get_imgs(self):
        return self.images

    # returns gender of user, 1 is woman, 0 is man
    def get_gender(self):
        return self.gender
