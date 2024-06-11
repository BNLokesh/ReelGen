import logging
from app import download_video, process_video

# Configure logging to see the output in the console
logging.basicConfig(level=logging.DEBUG)

def main():
    try:
        # Test video download
        youtube_url = "https://youtu.be/D0UnqGm_miA?si=qVcX5PZiu5Sedu6M"
        video_path = download_video(youtube_url)
        print(f"Video downloaded successfully: {video_path}")

        # Test video processing
        duration = 15
        num_reels = 2
        reels = process_video(video_path, duration, num_reels)
        print(f"Reels generated successfully: {reels}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
