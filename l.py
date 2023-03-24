import json
def json_to_obj(json_file):
    with open(json_file, "r") as file:
        data = json.loads(file.read())
    return data
def obj_to_json(obj, json_file):
    with open(json_file, "w") as file:
        file.write(json.dumps(obj, indent=4))
todos = json_to_obj("todos.json")
users = json_to_obj("users.json")
users_tasks = {}
for task in todos:
    id = task["userId"]
    name = users[id]
    if task["completed"]:
        if name not in users_tasks:
            users_tasks[name] = {"completed": 1, "not_completed": 0}
        else:
            users_tasks[name]["completed"] += 1
    if not task["completed"]:
        if name not in users_tasks:
            users_tasks[name] = {"completed": 0, "not_completed": 1}
        else:
            users_tasks[name]["not_completed"] += 1
print(users_tasks)
