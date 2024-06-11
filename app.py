from flask import Flask, request, jsonify, send_file
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import tempfile
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

# Use a persistent directory for temporary files
persistent_temp_dir = tempfile.mkdtemp()

def download_video(youtube_url):
    yt = YouTube(youtube_url)
    video = yt.streams.filter(file_extension='mp4').first().download()
    return video

def process_video(video_path, duration, num_reels):
    clip = VideoFileClip(video_path)
    reels = []
    for i in range(num_reels):
        start_time = i * duration
        end_time = min(start_time + duration, clip.duration)
        if start_time >= clip.duration:
            break
        reel_clip = clip.subclip(start_time, end_time)
        reel_filename = os.path.join(persistent_temp_dir, f'reel_{uuid.uuid4().hex}.mp4')
        reel_clip.write_videofile(reel_filename)
        reels.append(reel_filename)
    return reels

@app.route('/generate', methods=['POST'])
def generate_reels():
    data = request.get_json()
    youtube_url = data.get('youtubeURL')
    duration = data.get('duration')
    num_reels = data.get('numReels')

    video_path = download_video(youtube_url)
    reels = process_video(video_path, duration, num_reels)

    reel_urls = []
    for reel in reels:
        reel_id = os.path.basename(reel)
        reel_urls.append(f'http://localhost:5000/temp/{reel_id}')

    return jsonify({'reels': reel_urls})

@app.route('/temp/<path:filename>', methods=['GET'])
def temp_files(filename):
    return send_file(os.path.join(persistent_temp_dir, filename))

if __name__ == '__main__':
    app.run(debug=True)
