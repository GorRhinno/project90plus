import string
from collections import Counter


def main():
    with open("sample.txt", "r", encoding="utf-8") as f:
        content = f.read()
        words = content.split()
        clean_words = [word.strip(string.punctuation).lower() for word in words]
        filtered_words = [word for word in clean_words if len(word) > 3]
        counter = Counter(filtered_words)
        with open("output.txt", "w", encoding="utf-8") as out_files:
            for word, count in counter.most_common():
                out_files.write(f"{word}: {count}\n")

if __name__ == "__main__":
    main()