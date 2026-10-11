import os
import json
import firebase_admin
from firebase_admin import credentials, auth

if not firebase_admin._apps:
    cred_json = os.environ.get("FIREBASE_CREDENTIALS")
    if cred_json:
        info = json.loads(cred_json, strict=False)
        info["private_key"] = info["private_key"].replace("\\n", "\n")
        cred = credentials.Certificate(info)
    else:
        cred = credentials.Certificate("service_account.json")
    firebase_admin.initialize_app(cred)
