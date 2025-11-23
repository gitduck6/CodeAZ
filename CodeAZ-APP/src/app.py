import requests

while True:
    command = input("> ")

    if command.startswith("!xp "):
        try:
            user_id_str = command.split(" ", 1)[1]
            user_id = int(user_id_str)
        except:
            continue

        try:
            response = requests.get(f"http://localhost:8000/xp/{user_id}")
            data = response.json()
            rank = data["rank"] if data["rank"] is not None else "N/A"
            print(f"User ID {data['user_id']} — XP: {data['xp']} — Rank: {rank}")
        except:
            continue