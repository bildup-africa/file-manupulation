import json

data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

def setup():
    with open('db.json', 'w') as f:
        json.dump([data], f, indent=4)

def view_db():
    with open('db.json', 'r') as f:
        print(f)
        db_data = json.load(f)
        print(db_data)
        db_data = json.dumps(db_data, indent=4)
        print(db_data)

def write_to_db(new_data):
    with open('db.json', 'r+') as f:
        db_data = json.load(f)
        db_data.append(new_data)
        f.seek(0)
        json.dump(db_data, f, indent=4)

def delete_from_db(index):
    with open('db.json', 'r+') as f:
        db_data = json.load(f)
        if 0 <= index < len(db_data):
            db_data.pop(index)
            f.seek(0)
            f.truncate()
            json.dump(db_data, f, indent=4)
        else:
            print("Index out of range")

def get_single_entry(index):
    with open('db.json', 'r') as f:
        db_data = json.load(f)
        if 0 <= index < len(db_data):
            return db_data[index]
        else:
            print("Index out of range")
            return None


if __name__ == "__main__":
    # setup()
    # view_db()
    new_entry = {
        "name": "Bob",
        "age": 30,
        "skills": ["JavaScript", "React", "Node.js"]
    }
    write_to_db(new_entry)
    # view_db()
    # delete_from_db(0)
    # view_db()
    # entry = get_single_entry(0)
    # print(entry)