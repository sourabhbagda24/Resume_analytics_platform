from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


def download_files(folder_id):

    os.makedirs("output", exist_ok=True)

    gauth = GoogleAuth()

    # Agar credentials pehle se saved hain to load karo
    # Nahi hain to browser se login karo aur save karo
    if os.path.exists("credentials.json"):
        gauth.LoadCredentialsFile("credentials.json")

    if gauth.credentials is None:
        # Pehli baar — browser khulega
        gauth.LocalWebserverAuth()

    elif gauth.access_token_expired:
        # Token expire ho gaya — automatically refresh karo
        gauth.Refresh()

    else:
        # Credentials valid hain — seedha use karo
        gauth.Authorize()

    # Credentials save karo taaki agli baar browser na khule
    gauth.SaveCredentialsFile("credentials.json")

    drive = GoogleDrive(gauth)

    files = drive.ListFile(
        {'q': f"'{folder_id}' in parents and trashed=false"}
    ).GetList()

    downloaded_files = []

    for file in files:

        filename = file['title']

        print("Found:", filename)

        save_path = os.path.join("output", filename)

        file.GetContentFile(save_path)

        downloaded_files.append(save_path)

    return downloaded_files