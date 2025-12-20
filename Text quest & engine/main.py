import json, random
cur_id = "start"
game = "0"
text = ""
print("𝕺𝖕𝖊𝖓𝖎𝖓𝖌")
print("Это введение в сюжет.\nНа дворе 4823, разгар Средневековья. Вы - житель королевства Пельменум, города Сурград.\nВолшебник-недотёпа - это про вас.\nБудучи магом огня, вы не умеете кастовать атакующую магию!\nА также вы больны очень тяжёлой болезнью, название ей 'Ротум Вирусум'.\nПричём, так как вам было лень, вы настолько долго не выходили из дома, что если вы сегодня не получите лекарства, вы умрёте.\nУдачи!")
with open("data/locations.json", encoding="utf-8") as file:
    data = json.load(file)
while game != "1":
    k = 1
    name = data[cur_id]["name"]
    next = data[cur_id]["next"]
    user_next = data[cur_id]["user_next"]
    textstart = data[cur_id]["textstart"]
    textend = data[cur_id]["textend"]
    for line in textstart:
        print(line)
    if "quiz" in data[cur_id]:
        print("⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡\n")
        quiz = data[cur_id]["quiz"]
        text = data[quiz]["text"]
        print(text)
        answ = data[quiz]["answers"]
        for ans in answ:
            print(ans)
        print("(введите выбор целиком)")
        r = data[quiz]["r"]
        a = input()
        if a != r:
            new_cur_id = data[quiz]["d"]
            k = 0
    if k == 1:
        print("⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡\n")
        print(textend)
        n = 1
        for next_id in user_next:
            print(f"{n}. {next_id}")
            n += 1
        print("(введите число перед ответом без точки)")
        new_cur_id = next[int(input()) - 1]
    
    rand = random.randrange(0, 201)
    if 73 == rand:
        new_cur_id = "b_end"
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
            k = 1

    print("⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡⊡\n")
