from datetime import datetime
from pathlib import Path
import shutil


def save_temp_file(file):
    temp_folder = Path(__file__).resolve().parent / "temp"
    folder_name = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    folder_path = temp_folder / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

    # save file to folder_path
    with open(folder_path / file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return folder_path / file.filename


def clear_temp_folder():
    try:
        temp_folder = Path(__file__).resolve().parent / "temp"
        for folder in temp_folder.iterdir():
            if folder.is_dir():
                shutil.rmtree(folder)
        return True
    except Exception as e:
        print(e)
        return False
