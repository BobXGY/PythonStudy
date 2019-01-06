import json
import csv


def json_to_csv():
    with open("1.json", "rt", encoding="utf-8") as f:
        content = f.read()
    li = json.loads(content)
    print(li)
    with open("out.csv", "wt", encoding="utf-*", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "id"])
        for item in li:
            writer.writerow([item["name"], item["id"]])


def csv_to_json():
    li = []
    with open("out.csv", "rt", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            obj = {"name": line[0], "id": line[1]}
            li.append(obj)
    with open("to_json.json", "wt") as f:
        json_str = json.dumps(li)
        f.write(json_str)


if __name__ == "__main__":
    csv_to_json()
