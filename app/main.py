from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from helpers import (
    get_genres,
    get_catalog,
    get_streams,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


LOGO_URL = \
 "https://upload.wikimedia.org/wikipedia/commons/8/83/Circle-icons-radio.svg"

MANIFEST = {
    'id': 'com.milouk.greekRadio',
    'version': '1.0.0',
    'logo': LOGO_URL,
    'name': 'Greek Radio',
    'description': 'Stremio Add-On to listen to all Greek Radio Stations',
    'types': ['radio'],
    'catalogs': [
        {
          "type": "radio",
          "id": "radios",
          "name": "Greek Radio",
          "extra": [{"genres": get_genres()}]
        }
    ],
    "resources": [
        "catalog",
        "meta",
        "stream",
    ],
    "idPrefixes": [""]
}


@app.get('/manifest.json')
def addon_manifest():
    return JSONResponse(content=MANIFEST)


@app.get('/catalog/radio/radios.json')
def addon_catalog():

    catalog = get_catalog()
    metaPreviews = {
        'metas': [
            {
                'id': item['id'],
                'type': "radio",
                'name': item['name'],
                'genres': item["genres"],
                'poster': item["poster"],
                'description': "",
            } for item in catalog
        ]
    }

    return JSONResponse(content=metaPreviews)


@app.get('/meta/radio/{id}.json')
def addon_meta(id: str):

    def mk_item(item):
        meta = {}
        meta['id'] = item['id']
        meta['type'] = "radio"
        meta['name'] = item['name']
        meta['genres'] = item['genres']
        meta['poster'] = item["poster"]
        meta["background"] = item["poster"]
        meta["posterShape"] = "square"
        return meta

    meta = {
        'meta': next((mk_item(item)
                      for item in get_catalog() if item['id'] == id),
                     None)
    }
    return JSONResponse(content=meta)


@app.get('/stream/radio/{id}.json')
def addon_stream(id: str):

    streams = {'streams': []}
    if id in get_streams():
        streams['streams'].append(get_streams()[id])

    return JSONResponse(content=streams)
