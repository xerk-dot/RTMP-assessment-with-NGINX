## About this Repository

This repository hosts the code for a technical evaluation project. The project aims to create an application that receives audio and video streams over RTMP and provides diagnostic information about the streams. The diagnostic information includes details such as sample rate, pixel format, timestamps, resolution, and codec used.

The application is designed to be compatible with both Windows and Linux operating systems. It handles both audio and video streams, analyzes the streams to extract necessary diagnostic information, and presents the extracted data in a readable format. This project serves as a comprehensive assessment of the ability to work with RTMP streams and extract meaningful diagnostic data. 

## Application Requirements

Create an application that:

- Accepts audio and video input over RTMP.
- Prints out diagnostic information about the received audio/video, including:
  - Sample rate
  - Pixel format
  - Timestamp/PTS/DTS
  - Resolution
  - Codec

## My Implementation

I implemented the application in Python using the `ffmpeg` library to handle the RTMP streams.

### Running the Application

To run the application, you can use the following command:

```bash
python main.py
```

