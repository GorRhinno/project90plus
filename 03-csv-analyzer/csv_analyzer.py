import csv
from collections import Counter


def log_result(line, file=None):
    print(line)
    if file:
        print(line, file = file)


def main():
    with open("movies.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        film_count = 0
        rating = 0
        row_genre = []
        for row in reader:
            film_count += 1
            rating += float(row["rating"])
            row_genre.append(row["genre"])
        counter = Counter(row_genre)
        with open("summary.txt", "w", encoding="utf-8") as summary:
            log_result("🎬 Анализ завершён", summary)
            log_result(f"Количество фильмов: {film_count}", summary)
            log_result(f"Средний рейтинг: {round(rating / film_count, 2)}", summary)
            log_result(f"Самый популярный жанр: {counter.most_common(1)[0][0]}", summary)
if __name__ == "__main__":
    main()