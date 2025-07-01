import json
cur_id = "0"
name = "start"
next = ["1", "2"]
finish = "0"
while finish != "1":
    print("want transition? type number:")
    for next_id in next:
        print(f"{next_id}. loc{next_id}")
    new_cur_id = str(input())
    with open("data/locations.json") as file:
        data = json.load(file)
    cur_id = new_cur_id
    name = data[new_cur_id]["name"]
    next = data[new_cur_id]["next"]
    if "finish" in data[new_cur_id]:
        finish = data[new_cur_id]["finish"]
    if finish == "1":
        print("want to play again? type 'Yes' if you want, else type something else")
        if input() == "Yes":
            cur_id = "0"
            name = "start"
            next = ["1", "2"]
            finish = "0"