import json

my_dict = {"name": "Ahmed", "Age": 21, "Field": "Computer Science"}
with open("data.json", "a+", encoding="utf-8") as json_file:
    for i in range(5):
        json.dump(my_dict, json_file, sort_keys=True, indent=2)
        json_file.write(",\n")
        json_file.seek(0)
        json_data = json_file.read()
    print(json_data, end="")
