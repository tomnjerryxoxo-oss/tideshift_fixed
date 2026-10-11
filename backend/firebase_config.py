import os
import json
import base64
import firebase_admin
from firebase_admin import credentials, auth

if not firebase_admin._apps:
    b64 = os.environ.get("FIREBASE_CREDENTIALS_B64")
    raw = os.environ.get("FIREBASE_CREDENTIALS")
    if b64:
        info = json.loads(base64.b64decode(b64).decode("utf-8"))
        cred = credentials.Certificate(info)
        print("FIREBASE SOURCE: B64", info.get("client_email"), info.get("private_key_id"))
    elif raw:
        info = json.loads(raw, strict=False)
        info["private_key"] = info["private_key"].replace("\\n", "\n")
        cred = credentials.Certificate(info)
        print("FIREBASE SOURCE: ENV", info.get("client_email"), info.get("private_key_id"))
    else:
        cred = credentials.Certificate("service_account.json")
        print("FIREBASE SOURCE: FILE")
    firebase_admin.initialize_app(cred)
