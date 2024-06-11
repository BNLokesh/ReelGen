# ReelGen - Reel Video Generator

## Overview

ReelGen is a web application that allows users to generate short reels from YouTube videos. Users can input a YouTube URL, specify the duration for each reel, and the number of reels they want to generate. The application processes the video and provides download links for each generated reel.

## Features

- Input a YouTube URL to generate reels
- Specify the duration of each reel (15, 30, or 45 seconds)
- Generate multiple reels from the same video
- Download the generated reels
- Preview the reels before downloading

## Installation

To run this project locally, follow these steps:

### Backend Setup

1. Ensure you have Python installed on your system.
2. Install the required Python packages:

    ```bash
    pip install flask pytube moviepy flask-cors
    ```

3. Run the Flask server:

    ```bash
    python app.py
    ```

### Frontend Setup

1. Ensure you have Node.js and npm installed on your system.
2. Install the required packages:

    ```bash
    npm install
    ```

3. Run the React development server:

    ```bash
    npm start
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:3000`.
2. Enter a valid YouTube URL.
3. Specify the duration and number of reels.
4. Click the 'Generate Reels' button and wait for the process to complete.
5. Preview and download the generated reels.

## Technologies Used

- React
- Flask
- pytube
- moviepy
- CSS

## License

This project is licensed under the MIT License.

## Footer

ReelGen &copy; 2024
