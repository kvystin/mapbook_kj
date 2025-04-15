def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów.")

def add_user(users_data: list) -> None:
        new_name: str = input("podaj imię nowego znajomego: ")
        new_location: str = input("podaje lokalizacje: ")
        new_post: str = input("podaj ilość postów nowego znajomego: ")
        users_data.append({"name": new_name, "location": new_location, "posts": new_post})

def remove_user(users_data: list) ->None:
    users_name:str=input("Podaj imie znajomego do usunięcia: ")
    for user in users_data:
        if user["name"] == users_name:
            users_data.remove(user)