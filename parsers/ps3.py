def get_titleids():
    ids = {}
    with open("datafiles/ps3.txt", "r", encoding="utf-8") as file:
        for line in file:
            code = line[:9]
            title = line[10:]
            ids[code] = title
    return ids

def parse_title(title, ids):
    media = { #first
        "B": "Physical",
        "N": "Digital"
    }
    region = { #third
        "A": "Asia",
        "C": "China",
        "E": "Europe",
        "H": "Hong Kong",
        "J": "Japan",
        "K": "Korea",
        "U": "USA"
    }

    if title[0] in media.keys():
        media_type = media[title[0]]
    else:
        media_type = "Unknown"

    if title[2] in region.keys():
        region_type = region[title[2]]
    else:
        region_type = "Unknown"

    if title in ids.keys():
        game = ids[title]
    else:
        game = "Unknown"

    return game, media_type, region_type