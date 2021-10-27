import requests

link = "https://www.gutenberg.org/cache/epub/66540/pg66540.txt"
file = "cosmic_saboteur.txt"
link = "https://www.gutenberg.org/files/65770/65770-0.txt"
file = "the_killer.txt"

with requests.get(link, stream=True) as response:
    with open(file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)