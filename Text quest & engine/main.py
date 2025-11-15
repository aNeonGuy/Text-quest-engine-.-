import json
cur_id = "start"
game = "0"
text = ""
with open("data/locations.json", encoding="utf-8") as file:
    data = json.load(file)
while game != "1":
    name = data[cur_id]["name"]
    next = data[cur_id]["next"]
    user_next = data[cur_id]["user_next"]
    text = data[cur_id]["text"]
    for line in text:
        print(line)
    n = 1
    for next_id in user_next:
        print(f"{n}. {next_id}")
        n += 1
    new_cur_id = next[int(input()) - 1]
    cur_id = new_cur_id
    if "game" in data[cur_id]:
        game = data[cur_id]["game"]
        text = data[cur_id]["text"]
        for line in text:
            print(line)
    if game == "1":
        print("Хотите сыграть снова? Пишите 'да' если хотите.")
        if input().lower() == "да":
            cur_id = "start"
            game = "0"
    print("⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡\n")