import subprocess
import json

def get_stream_info(rtmp_url):
    # Use ffprobe to get stream information
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'stream=index,codec_name,codec_type,width,height,sample_rate,pix_fmt,duration,bit_rate',
        '-of', 'json',
        rtmp_url
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr.decode()}")
        return None

    return json.loads(result.stdout)

def print_stream_info(stream_info):
    for stream in stream_info.get('streams', []):
        print("Stream Index:", stream.get('index'))
        print("Codec Name:", stream.get('codec_name'))
        print("Codec Type:", stream.get('codec_type'))
        if 'width' in stream and 'height' in stream:
            print("Resolution:", f"{stream['width']}x{stream['height']}")
        if 'sample_rate' in stream:
            print("Sample Rate:", stream['sample_rate'])
        if 'pix_fmt' in stream:
            print("Pixel Format:", stream['pix_fmt'])
        print("Duration:", stream.get('duration'), "seconds")
        print("Bitrate:", stream.get('bit_rate'), "bps")
        print("-" * 30)

if __name__ == "__main__":
    rtmp_url = input("Enter the RTMP URL: ")
    stream_info = get_stream_info(rtmp_url)
    if stream_info:
        print_stream_info(stream_info)


 