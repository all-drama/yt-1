from fastapi import FastAPI
from fastapi.params import Query
import yt_dlp

app = FastAPI()

@app.get("/download")
async def download_video(url: str = Query(...)):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'best',
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    
    return {"filename": filename}
