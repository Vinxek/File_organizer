import shutil
import os

image_formats = [".jpg", ".png", ".jpeg", ".gif", ".webp", ".tiff"]
audio_formats = [".mp3", ".wav", ".FLAC"]
video_formats = [".mp4", ".avi", ".webm", ".mkv"]
docs_format = [".docx", ".pdf", ".txt", ".xlsx"]
exe_files = ".exe"

current_dir = r"C://Users//Vinxek//Downloads"

for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)
    print (file_ext)

    try:
        if not file_ext:
            pass
        elif file_ext in image_formats:
            shutil.move(
                os.path.join(current_dir, f"{filename}{file_ext}"),
                os.path.join(r"C://Users//Vinxek//Pictures", f"{filename}{file_ext}")
            )
        elif file_ext in audio_formats:
                shutil.move(
                os.path.join(current_dir, f"{filename}{file_ext}"),
                os.path.join(r"C://Users//Vinxek//Music", f"{filename}{file_ext}")
            )
            
    
    except (FileNotFoundError, PermissionError):
        pass
