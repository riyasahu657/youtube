from flask import Flask, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>YouTube Downloader</title>
      <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background: #f4f4f4; }
        h1 { color: #333; }
        input { padding: 10px; width: 300px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 10px 20px; margin-left: 10px; border: none; background: #007BFF; color: white; border-radius: 5px; cursor: pointer; }
        button:hover { background: #0056b3; }
      </style>
    </head>
    <body>
      <h1>YouTube Video Downloader</h1>
      <form action="/download" method="post">
        <input type="text" name="url" placeholder="Enter YouTube URL" required />
        <button type="submit">Download</button>
      </form>
    </body>
    </html>
    '''

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    yt = YouTube(url)

    # Get highest resolution
    stream = yt.streams.get_highest_resolution()

    # Save to downloads folder
    os.makedirs("downloads", exist_ok=True)
    file_path = stream.download(output_path="downloads")

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
