import requests

class GetInfo:
    def __init__(self):
        self.KEY = 'STEAM_KEY'

    def user_games(self, steamid):
        response = requests.get(url='http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001', params={'key':self.KEY, 'steamid':steamid, 'include_appinfo':True}).json()
        games = ''
        for game in response['response']['games']:
            games += game['name'] + '\n'
        return games
