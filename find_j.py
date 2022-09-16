import re

J_SPCE = r"\u3000"
J_PUNC = r"\u3001-\u303F"
J_HIRA = r"\u3040-\u309F"
J_KATA = r"\u30A0-\u30FF"
J_KANJ = r"\u4E00-\u9FFF"
J_HWFW = r"\uFF00-\uFFEF"
j_regex = re.compile("["+J_SPCE+J_PUNC+J_HIRA+J_KATA+J_KANJ+J_HWFW+"]+")

def find_japanese(text: str) -> list[str]:
    return j_regex.findall(text)