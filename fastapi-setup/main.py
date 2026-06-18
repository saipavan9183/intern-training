from fastapi import FastAPI

app = FastAPI()

users = {}

# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

# Hello Route
@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Vanakkam {name}"}

# Create User
@app.post("/users/{user_id}")
def create_user(user_id: int, name: str):
    users[user_id] = name
    return {"message": f"User {name} created"}

# Get All Users
@app.get("/users")
def get_users():
    return users

# Get One User
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id in users:
        return {"user": users[user_id]}
    return {"error": "User not found"}

# Update User
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str):
    if user_id in users:
        users[user_id] = name
        return {"message": f"User updated to {name}"}
    return {"error": "User not found"}

# Delete User
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return {"message": f"{deleted_user} deleted"}
    return {"error": "User not found"}