FILE_COL_SEP = "\t"
SENSE_SEP = "<br>"
PHRASE_SEP = "; "
POS_SEP = ", "

def format(data):
    if ("word" in data["japanese"][0]) and ("reading" in data["japanese"][0]):
        word = data["japanese"][0]["word"]
        reading = data["japanese"][0]["reading"]
    elif ("word" in data["japanese"][0]):
        word = data["japanese"][0]["word"]
        reading = data["japanese"][0]["word"]
    elif ("reading" in data["japanese"][0]):
        word = data["japanese"][0]["reading"]
        reading = data["japanese"][0]["reading"]
    sense_strings = list()
    for sense in data["senses"]:
        sense_strings.append("(" + POS_SEP.join(sense["parts_of_speech"]) + ") " + PHRASE_SEP.join(sense["english_definitions"]))
    meaning = SENSE_SEP.join(sense_strings)
    return FILE_COL_SEP.join((word, meaning, reading))