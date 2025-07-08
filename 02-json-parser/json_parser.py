from pathlib import Path
import json

def main():
    with open("people.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"🔥 Люди старше 25")
        for elem in data:
            if elem["age"] > 25:
                print(f"{elem["name"]} : {elem["age"]}")
                
if __name__ == "__main__":
    main()






