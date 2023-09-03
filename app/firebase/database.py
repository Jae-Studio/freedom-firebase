# Interacts with the Firebase Realtime Database or Firestore.
from .authentication import authenticate as auth, database as db

def create_item(db, item_name):
    new_item = {"name": item_name}
    db.child("items").push(new_item)

def read_items(db):
    items = db.child("items").get()
    if items.each():
        for item in items.each():
            print("Key:", item.key())
            print("Name:", item.val()["name"])
    else:
        print("No items found.")

def update_item(db, item_key, new_name):
    db.child("items").child(item_key).update({"name": new_name})

def delete_item(db, item_key):
    db.child("items").child(item_key).remove()

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        return user
    except Exception as e:
        print("Authentication failed:", e)