import urllib.request
import sys
import wordfreq


def main():
    # Läs in stopwords
    stopwords = []

    with open(sys.argv[1], encoding="utf-8") as file:
        for line in file:
            stopwords.append(line.strip())

    source = sys.argv[2]

    # Hämta text från webben om det är en URL
    if source.startswith("http://") or source.startswith("https://"):
        response = urllib.request.urlopen(source)
        lines = response.read().decode("utf8").splitlines()
        words = wordfreq.tokenize(lines)

    # Annars läs från fil
    else:
        with open(source, encoding="utf-8") as file:
            words = wordfreq.tokenize(file)

    # Räkna orden
    frequencies = wordfreq.countWords(words, stopwords)

    # Antal ord som ska visas
    n = int(sys.argv[3])

    wordfreq.printTopMost(frequencies, n)


main()
