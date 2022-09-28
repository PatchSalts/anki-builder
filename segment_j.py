from fugashi import Tagger

tagger = Tagger()

def segment_japanese(text: str) -> list[str]:
    return [word.surface for word in tagger(text)]