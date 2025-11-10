import json
import uuid


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
        print(json.dumps(db_data, indent=4))
        return db_data

def get_data_by_id(id):
    with open("db.json", "r") as f:
        db_data = json.load(f)  
        for data in db_data:
            if data["id"] == id:
                return data
            
def delete_data_by_id(id):

    db_data  = get_all()

    with open("db.json", "w") as f:
        new_db = []
        for data in db_data:
            if data["id"] == id:
                continue
            new_db.append(data)
            json.dump(new_db, f, indent=4)




if __name__ == "__main__":
    print("1: Save info to db\n")
    print("2: Read all db info\n")
    print("3: Read data by id\n")
    print("4: delete data by id\n")
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
            get_all()

        elif resp == 3:
            id = input("id: ")
            data_info = get_data_by_id(id)
            print(json.dumps(data_info, indent=4))

        elif  resp == 4:
            id = input("id: ")
            delete_data_by_id(id)
            print(f"Data {id} has been deleted successfully")

        else:
            print("Choose between 1 and 2.")
    except Exception as e:
        print("Invalid input:", e)