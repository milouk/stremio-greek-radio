from radio_data import RADIO_DATA

def get_streams():
    streams = {}
    for entry in RADIO_DATA:
        streams[entry["id"]] = {
                 'title': "Listen to %s" % entry["name"],
                 'url': entry["url"], }
    return streams


def get_catalog():
    catalog = []
    for entry in RADIO_DATA:
        catalog.append({
            "id": entry["id"],
            "name": entry["name"],
            "genres": entry["genres"],
            "poster": entry["poster"],
        })
    return catalog


def get_genres():
    genres = set()
    for item in RADIO_DATA:
        genres.add(itm for itm in item["genres"])
