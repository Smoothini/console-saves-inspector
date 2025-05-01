import json

def get_titleids():
    ids = {}
    with open("datafiles/psv.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for game in data:
            code = game["title_id"]
            title = game["title"]
            region = game["region"]
            ids[code] = title, region
    return ids

def parse_title(title, ids):
    media = { #first
        "PCS": "Game",
        "NPX": "System"
    }
    region = { #fourth
        "eu": "Europe",
        "us": "USA",
        "jp": "Japan",
        "ch": "China",
        "as": "Asia",
        "hk": "Hong Kong",
        "ko": "Korea",
    }

    title_id = title

    print(media.keys(), title[0:3])

    if title[0:3] in media.keys():
        media_type = media[title[0:3]]
        title_id = f"{title[0:4]}-{title[4:]}"
    else:
        media_type = "Unknown/Homebrew"


    if title_id in ids.keys():
        game, reg = ids[title_id]
    else:
        game, reg = "Unknown", "Unknown"


    if reg in region.keys():
        region_type = region[reg]
    else:
        region_type = "Unknown"



    return game, media_type, region_type