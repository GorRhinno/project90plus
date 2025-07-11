import os
import sys
from pathlib import Path
import string
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь к папке как аргумент.")
        sys.exit()
    else:
        folder_path = sys.argv[1]
        path = Path(folder_path)
        if not path.exists() or not path.is_dir():
            print("Такой папки не существует.")
            sys.exit()
        else:
            txt_files = list(path.glob("*.txt"))
            print(f"{len(txt_files)} .txt files was found")
            with open("summary.txt", "w", encoding="utf-8") as summary:
                for txt_file in txt_files:
                    with open(txt_file, "r", encoding="utf-8") as f:
                        content = f.read()
                        content_lines = len(content.splitlines())
                        content_words = len([word.strip(string.punctuation + "\n") for word in content.split() if word.strip(string.punctuation + "\n").isalpha()])
                        content_chars = len(content)
                        print(f"🔥 Обработка началась!")
                        print(f"📄 Файл: {txt_file.name}")
                        print(f"〽 Строк: {content_lines}")
                        print(f"🐍 Слов: {content_words}")
                        print(f"#️⃣Символов: {content_chars}")
                        print("✅ Готово!\n")

                        print(f"🔥 Обработка началась!", file=summary)
                        print(f"📄 Файл: {txt_file.name}", file=summary)
                        print(f"〽 Строк: {content_lines}", file=summary)
                        print(f"🐍 Слов: {content_words}", file=summary)
                        print(f"#️⃣Символов: {content_chars}", file=summary)
                        print("✅ Готово!\n", file=summary)

if __name__ == "__main__":
    main()





