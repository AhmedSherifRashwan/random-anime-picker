import requests
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    # Define the API endpoint
    endpoint = "https://kitsu.io/api/edge/anime"

    # Set up the request headers
    headers = {"Accept": "application/vnd.api+json"}

    # Set up the request parameters
    params = {"page[limit]": 20}

    # Send the request to the API
    response = requests.get(endpoint, headers=headers, params=params)

    # Parse the response JSON
    data = response.json()

    # Select a random anime from the list of results
    anime = random.choice(data["data"])
    # gathered data from html
    animeTitle = anime["attributes"]["titles"]["en_jp"]
    animeSynopsis = anime['attributes']['synopsis']
    animeImage = anime["attributes"]["posterImage"]["medium"]
    animeAgeRating = anime["attributes"]["ageRating"]
    animeEpisodes = str(anime["attributes"]["episodeCount"])
    # Return the title of the selected anime
    return render_template("index.html", animeTitle=animeTitle, animeImage=animeImage, animeSynopsis=animeSynopsis, animeAgeRating=animeAgeRating, animeEpisodes=animeEpisodes)

if __name__ == "__main__":
    app.run(debug=True)







