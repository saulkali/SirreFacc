import firebase_admin
from firebase_admin import db
from firebase_admin.db import Reference

from helper import getFile,singleton

@singleton
class FireBase(object):
    credential:firebase_admin.credentials.Certificate
    app:firebase_admin.App
    db:Reference

    def __init__(self) -> None:
        self.credential = firebase_admin.credentials.Certificate(
            getFile("key_firebase.json")
        )
        self.app = firebase_admin.initialize_app(
            self.credential,
            {
                "databaseURL" : "https://refaccionaria-5244c-default-rtdb.firebaseio.com/"
            }
        )
        self.db = db.reference("/")