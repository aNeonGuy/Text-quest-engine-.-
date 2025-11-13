import json
cur_id = "start"
game = "0"
with open("data/locations.json", encoding="utf-8") as file:
    data = json.load(file)
while game != "1":
    name = data[cur_id]["name"]
    next = data[cur_id]["next"]
    user_next = data[cur_id]["user_next"]
    print("Какой хотите совершить переход? Впишите номер локации.")
    n = 1
    for next_id in user_next:
        print(f"{n}. {next_id}")
        n += 1
    new_cur_id = next[int(input()) - 1]
    cur_id = new_cur_id
    if "game" in data[new_cur_id]:
        game = data[new_cur_id]["game"]
    if game == "1":
        print("Хотите сыграть снова? Пишите 'да' если хотите.")
        if input().lower() == "да":
            cur_id = "start"
            game = "0"