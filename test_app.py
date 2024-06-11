import pytest
from unittest.mock import patch
from pymongo import MongoClient
from app import app, reels_collection

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_generate_reels_success(client):
    with patch('app.YouTube') as MockYouTube:
        MockYouTube.return_value.streams.filter.return_value.first.return_value.download.return_value = 'dummy_video.mp4'
        with patch('app.VideoFileClip') as MockVideoFileClip:
            MockVideoFileClip.return_value.duration = 60
            MockVideoFileClip.return_value.subclip.return_value.write_videofile.return_value = None

            response = client.post('/generate', json={
                'youtubeURL': 'https://www.youtube.com/watch?v=dummy_video',
                'duration': 15,
                'numReels': 2
            })
            data = response.get_json()
            assert response.status_code == 200
            assert 'youtube_url' in data
            assert 'reels' in data

def test_generate_reels_invalid_url(client):
    with patch('app.YouTube') as MockYouTube:
        MockYouTube.side_effect = Exception("Invalid URL")
        response = client.post('/generate', json={
            'youtubeURL': 'invalid_url',
            'duration': 15,
            'numReels': 2
        })
        assert response.status_code == 500
        data = response.get_json()
        assert 'Failed to download video' in data['message']

def test_get_reel_success(client):
    reel_id = str(reels_collection.insert_one({
        'youtube_url': 'https://www.youtube.com/watch?v=dummy_video',
        'duration': 15,
        'num_reels': 2,
        'reels': ['reel_0.mp4', 'reel_1.mp4']
    }).inserted_id)

    response = client.get(f'/reels/{reel_id}')
    data = response.get_json()
    assert response.status_code == 200
    assert 'youtube_url' in data
    assert data['_id'] == reel_id

def test_get_reel_not_found(client):
    response = client.get('/reels/60e6c8b2c13f3c6d98fa1e34')
    assert response.status_code == 404
    data = response.get_json()
    assert 'Reel not found' in data['error']
