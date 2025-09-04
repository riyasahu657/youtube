from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
