import json
import uuid


def clear_db():
    print("i am clear db")
    with open("db.json", "w") as f:
        json.dump([], f, indent=4)

def save_to_db(name, age, skills):
    with open("db.json", "r+") as f:
        db_data = []
        data = {
            "id": str(uuid.uuid4()),
            "name": name,
            "age": age,
            "skills": skills
        }
        try:
            db_data = json.load(f)
        except:
            pass
        db_data.append(data)
        f.seek(0)
        json.dump(db_data, f, indent=4)

def get_all():
    with open("db.json", "r") as f:
        db_data = json.load(f)  # fixed json.loads(f) misuse
        return db_data

def get_data_by_id(id):
    with open("db.json", "r") as f:
        db_data = json.load(f)  
        for data in db_data:
            if data["id"] == id:
                return data
            
def delete_data_by_id(id):
    
    db_data  = get_all()
    new_db = []
    for data in db_data:
        if data["id"] == id:
            continue
        new_db.append(data)
    clear_db()

    # loop through the new db and save the data
    for data in new_db:
        save_to_db(data["name"], data["age"], data["skills"])

def update_data_by_id(id, **kwargs):
    name = kwargs.get("name", None)
    age = kwargs.get("age", None)
    skills = kwargs.get("skills", None)
    
    db_data  = get_all()
    new_db = []
    for data in db_data:
        if data["id"] == id:
            updated_info = {
                "name": name if name is not None else data["name"],
                "age": age if age is not None else data["age"],
                "skills": skills if skills is not None else data["skills"]
            }
            new_db.append(updated_info)
        else:
            new_db.append(data)
    clear_db()

    # loop through the new db and save the data
    for data in new_db:
        save_to_db(data["name"], data["age"], data["skills"])


if __name__ == "__main__":
    print("1: Save info to db\n")
    print("2: Read all db info\n")
    print("3: Read data by id\n")
    print("4: delete data by id\n")
    print("5: update data by id\n")
    resp = input("What do you want to do?: ")

    try:
        resp = int(resp)
        if resp == 1:
            print("\nEnter the following details:\n")
            name = input("Name: ")
            age = input("Age: ")
            skills = input("Enter skills (comma separated): ").split(",")
            skills = [s.strip() for s in skills]

            save_to_db(name, age, skills)
        elif resp == 2:
            data = get_all()
            print(json.dumps(data, indent=4))

        elif resp == 3:
            id = input("id: ")
            data_info = get_data_by_id(id)
            print(json.dumps(data_info, indent=4))

        elif  resp == 4:
            id = input("id: ")
            delete_data_by_id(id)
            print(f"Data {id} has been deleted successfully")

        elif resp == 5:
            id = input("id: ")
            print("Enter new details (leave blank to keep current value):")
            name = input("Name: ")
            age = input("Age: ")
            skills_input = input("Enter skills (comma separated): ")
            skills = [s.strip() for s in skills_input.split(",")] if skills_input else None

            update_data_by_id(id, name=name if name else None, age=age if age else None, skills=skills)
            print(f"Data {id} has been updated successfully")

        else:
            print("Choose between 1 and 2.")
    except Exception as e:
        print("Invalid input:", e)