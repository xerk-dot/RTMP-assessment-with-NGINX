## About this Repository

This repository hosts the code for a technical assessment. 

The project aims to create an application that receives audio and video streams over RTMP and provides diagnostic information about the streams.

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

To run the python locally, run the following:

```bash
pip3 install nicegui
python3 main.py
```

### Running the Nginx RTMP server using Docker

To run the Nginx RTMP server using Docker, follow these steps:

1. **Build the Docker Image**:
   Navigate to the directory containing the `Dockerfile` and run the following command to build the Docker image:

   ```bash
   docker build -t nginx-rtmp .
   ```

2. **Run the Docker Container**:
   After the image is built, you can run the Docker container with the following command:

   ```bash
   docker run -d -p 1935:1935 -p 8080:8080 --name my-nginx-rtmp nginx-rtmp
   ```

   This command will:
   - Run the container in detached mode (`-d`).
   - Map port `1935` for RTMP streaming.
   - Map port `8080` for HTTP access.

3. **Stream to the Nginx RTMP Server**:
   You can stream to the Nginx RTMP server using the following RTMP URL:

   ```bash
   rtmp://localhost:1935/live/mystream
   ```

6. **Use ffmpeg to Detect the Stream**:
   To test the stream and see the output, you can use `ffmpeg` with the following command:

   ```bash
   ffmpeg -i rtmp://localhost:1935/live/mystream -c copy -f null -
   ```

   This command will attempt to read the stream and output any diagnostic information to the console.


### Stopping the Nginx RTMP server using Docker

1. **Stop the Docker Container**:
   If you need to stop the running container, use the following command:

   ```bash
   docker stop my-nginx-rtmp
   ```

2. **Remove the Docker Container**:
   To remove the container after stopping it, run:

   ```bash
   docker rm my-nginx-rtmp
   ```
