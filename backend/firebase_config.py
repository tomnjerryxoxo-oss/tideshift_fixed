import os
import json
import firebase_admin
from firebase_admin import credentials, auth

if not firebase_admin._apps:
    cred_json = os.environ.get("FIREBASE_CREDENTIALS")
    if cred_json:
        # Di Railway: baca dari environment variable
        cred = credentials.Certificate(json.loads(cred_json, strict=False))
    else:
        # Di laptop: baca dari file lokal
        cred = credentials.Certificate("service_account.json")
    firebase_admin.initialize_app(cred)
