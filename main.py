# importing libraries
import dotenv 
import os
import base64
from requests import post, get
import json
import pickle as pk

# loading env variables, that are saved in other .env file
dotenv.load_dotenv()
id = os.getenv('c_id')
secret = os.getenv('c_secret')

# generating token, by sending these credentials to endpoint
def get_token():
    """
    Create token to use later
    """
    #Generating Authorization String and encoding it to base64
    auth_string = id + ":" + secret
    auth_string = auth_string.encode('utf-8')
    auth_string = str(base64.b64encode(auth_string), 'utf-8')
    #
    url = 'https://accounts.spotify.com/api/token'
    #
    header = {
        'Authorization': 'Basic ' + auth_string,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    #
    data = {'grant_type': 'client_credentials'}
    # Posting our client credentials in order to authorize ourselves and generate a token
    result = post(url, headers= header, data= data)
    # this result is a kind of response code, we can't use it
    # to use it we'll need to convert this into json
    result = json.loads(result.content)
    # understanding the result:
    # it contains 3 keys, they are access_token, token_type, expires_in
    # since we only need access_token we'll retrieve only that part

    return result['access_token']

# Generating token
v = get_token()


# generate auth header for future calls
def get_auth_header(token):
    return {'Authorization': 'Bearer '+ token}


# to work around our artists and tracks we need Spotify ID for tracks and artists


# get spotify id for artists and tracks
def search(token, artist_name, track_name):
    # currently set for searching tracks
    # for searching artists, we'll modify query
    # remove the part +artist:{}
    # replace type=track to type=artist
    url = 'https://api.spotify.com/v1/search'
    headers= get_auth_header(token)

    #modifying our search query by adding artist name filter for more accuracy
    q = f"?q=track:{track_name}+artist:{artist_name}&type=track&limit=1"

    query_url = url+q
    result = get(query_url, headers= headers)
    # leaving our result as a response object
    # result = json.loads(result.content)
    # id = ['tracks']['items'][0]['id']
    return result

# reading aritstNames and trackNames
with open('artists101.pkl', 'rb') as f:
    artistNames = pk.load(f)
with open('tracks101.pkl', 'rb') as f:
    trackNames = pk.load(f)


# getting ids for each artist and saving it as a pkl, so that next time we don't have to go through this process again, same for the tracks
id_of_artist = {}
c = 0

for index, name in enumerate(artistNames):
    print(c)
    #3
    if search(v, name).status_code == 200:
        try:
            result = search(v, name)
            result = json.loads(result.content)
            id = result['artists']['items'][0]['id']
            id_of_artist[name] = id
            print(index)
            print(name)
        except KeyError:
            c += 1
            continue  
    c += 1

# saving it as a pkl file to use it later
with open('artistWithIDs.pkl', 'wb') as f:
    pk.dump(id_of_artist,f)


# getting ids for tracks
# understanding tracks101 it contains a dictionary in which tracks are keys and artists are values
# since we've the search function in query we can filter a track on the basis of artist who made that for more accuracy

tracksWithIDs = {}

for track, artist in trackNames.items():
    if search(v, artist, track).status_code == 200:
        try:
            result = search(v, artist, track)
            result = json.loads(result.content)
            id = result['tracks']['items'][0]['id']
            tracksWithIDs[track] = id
            print(track)
        except IndexError:
            continue
        except KeyError:
            continue

# saving it so that we can use it later on
with open('tracksWithIDs.pkl', 'wb') as f:
    pk.dump(tracksWithIDs, f)


# reading the saved pkl file for extracting data related to tracks
with open('tracksWithIDs.pkl', 'rb') as f:
    tracksWithIDs = pk.load(f)


# let's define a function that gives the track information
def getTrackStats(token, trackId):

    """
    This will fetch stats for each track
    """

    url = f"https://api.spotify.com/v1/tracks/{trackId}"
    header = get_auth_header(token)
    result = get(url, headers= header)
   
    
    #img = ['album']['images'][0]['url']
    #popularity = ['popularity']
    #explicit = ['explicit']
    #duration = ['duration_ms']
    #albumName = if(['album']['total_tracks'] > 3): ['album']['name']
    # we'll pull artists later on

    return result

# container for storing data temporarily
trackImage = {}
trackPopularity = {}
trackExplicit = {}
trackDuration = {}
trackAlbumName = {}

for track, id in tracksWithIDs.items():
    try:
        temp = getTrackStats(v, id)
        img = temp['album']['images'][0]['url']
        if img:
            trackImage[track] = img
            print('Image Pull Success')
            print(track)
        
        explicit = temp['explicit']
        if explicit:
            trackExplicit[track] = explicit
            print('Explicit Pull Success')
            print(track)
        
        popularity = temp['popularity']
        if popularity:
            trackPopularity[track] = popularity
            print('Popularity pull success')
            print(track)
        
        duration = temp['duration_ms']
        if duration:
            trackDuration[track] = duration
            print('Duration Pull Success')
            print(track)
        
        if temp['album']['total_tracks'] >= 3:
            albumName = temp['album']['name']
            trackAlbumName[track] = albumName
            print("Album Pull Successfull")
    except IndexError:
        print(f"Index ERROR occured for {track}")
        continue
    except KeyError:
        print(f"Key ERROR occured for {track}")
        continue

# Saving it as .pkl to use it later, or read them in jupyter notebook
with open('trackImages.pkl', 'wb') as f:
    pk.dump(trackImage, f)
with open('trackExplicit.pkl', 'wb') as f:
    pk.dump(trackExplicit, f)
with open('trackPopularity.pkl', 'wb') as f:
    pk.dump(trackPopularity, f)
with open('trackDuration.pkl', 'wb') as f:
    pk.dump(trackDuration, f)
with open('trackAlbum.pkl', 'wb') as f:
    pk.dump(trackAlbumName, f)

# retrieving feature artists for a particular track

allArtists = {}

for track, id in tracksWithIDs.items():
    try:
        artists = getTrackStats(v, id)['artists']
        ft = ''
        if artists:
            if len(artists) > 1:
                for i in range(1, len(artists)):
                    if i == len(artists)-1:
                        ft += artists[i]['name']
                    else:
                        ft += artists[i]['name'] + ', '
                allArtists[track] = ft
                print(track)
                print(ft)
    except KeyError:
        continue
    except IndexError:
        continue

# saving it to .pkl to use it later
with open('featureArtists.pkl', 'wb') as f:
    pk.dump(allArtists, f)




# Artist Stats

def getArtistStats(token, artistID):
    endpoint = f"https://api.spotify.com/v1/artists/{artistID}"
    header = get_auth_header(token)
    result = get(endpoint, headers=header)
    result = json.loads(result.content)
    # img = ['images'][0]['url']
    # genre = ['genres'][0]
    # popularity = ['popularity']
    return result

# reading the pkl file containing artist name and ids
with open('artistWithIDs.pkl', 'rb') as f:
    artID = pk.load(f)

# extracing data
artImg = {}
artGenre = {}
artPopularity = {}

for name, id in artID.items():
    try:
        body = getArtistStats(v, id)

        img = body['images'][0]['url']
        if img:
            artImg[name] = img
            print(f"Image for {name}")
        genre = body['genres'][0]
        if genre:
            artGenre[name] = genre
            print(f"Genre for {name}")
        pop = body['popularity']
        if pop:
            artPopularity[name] = pop
            print(f"Popularity for {name}")
    except KeyError:
        continue
    except IndexError:
        continue

# storing all of this data to use it later
with open('imageArtist.pkl', 'wb') as f:
    pk.dump(artImg, f)
with open('genreArtist.pkl', 'wb') as f:
    pk.dump(artGenre, f)
with open('popularityArtist.pkl', 'wb') as f:
    pk.dump(artPopularity, f)

# Thanks!
