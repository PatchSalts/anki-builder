# anki-builder
A set of tools to help build Japanese flash card decks for Japanese vocabulary.

## Foreword

I started this project with the goal of automating the process of extracting vocabulary from text dumps of games and the like, so that I may be able to study vocabulary I would need to learn to play them in Japanese.

Of course, this tool can be used to find Japanese vocabulary in any block of text. I would love to use this for things like song lyrics and books in the future.

I had an older version of this program in progress but I decided to restart from scratch with a better mindset and after I learned some more skills in school.

## Requirements

I'm not an expert, so please message me if I am missing something here.

Please ensure that you have installed:
- Python 3 (I used 3.10.7 but I'm sure there are plenty of earlier versions that will work just fine)
- fugashi (again, I have 1.2.0 but other versions should be fine... probably)
- unidic-lite (see fugashi's instructions on how to do this; I can't guarantee interoperability between unidic-lite and other dictionaries)

At the very least, running `pip install fugashi fugashi[unidic-lite]` will probably work for you.

## Usage

USAGE SUBJECT TO CHANGE IN FUTURE VERSIONS

This project is a work in progress. I may change the usage interface at some point, but I will update the usage message here if that occurs.

Currently, the usage looks like this:  
    python anki-builder.py <file> ...

Just pass in each file you want to read as a command line argument and it will scan through each file in turn. It will output a file called "anki.txt" in your current working directory. I know this isn't ideal but I haven't quite figured out how I would want to handle other kinds of arguments on the command line so this is what I've settled on for now.

## Output

The output file is formatted as a TSV file. To import into Anki, follow the instructions Anki gives for importing. The settings you should use are:  
- Fields separated by: Tab
- ☑️ Allow HTML in fields

I designed the file to be used with the "Japanese recognition & recall" card types, with the fields of the file representing the `Expression`, `Meaning`, and `Reading` fields, but you can use the fields however you like.

Some entries will be a bit buggy. I only use the data directly from jisho.org's API, so the entries will never be wrong or anything like that, but for a btter formatting and viewing experience, you may have to manually modify some entries to suit your liking.

## Afterword

This is probably my first personal project I can be proud of. This is the kind of thing I wanted to get into programming for. I'm happy that my education and experience built into something I can consider valuable, and I hope I can go even further in the future. More features, more programs... Anything, really.

Thank you for reading! Happy studying!