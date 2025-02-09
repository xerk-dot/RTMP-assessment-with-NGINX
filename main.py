from nicegui import ui
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
        return f"Error: {result.stderr.decode()}"
    
    return json.loads(result.stdout)

def print_stream_info(stream_info):
    output = []
    for stream in stream_info.get('streams', []):
        output.append(f"Stream Index: {stream.get('index')}")
        output.append(f"Codec Name: {stream.get('codec_name')}")
        output.append(f"Codec Type: {stream.get('codec_type')}")
        if 'width' in stream and 'height' in stream:
            output.append(f"Resolution: {stream['width']}x{stream['height']}")
        if 'sample_rate' in stream:
            output.append(f"Sample Rate: {stream['sample_rate']}")
        if 'pix_fmt' in stream:
            output.append(f"Pixel Format: {stream['pix_fmt']}")
        output.append(f"Duration: {stream.get('duration')} seconds")
        output.append(f"Bitrate: {stream.get('bit_rate')} bps")
        output.append("-" * 30)
    
    # Join the output list into a single string
    return "\n".join(output)

def analyze_stream():
    rtmp_url = url_input.value
    print(f"Analyzing RTMP URL: {rtmp_url}")  # Debugging line
    if not rtmp_url:
        result_output.value = "Please enter a valid RTMP URL."
        return

    stream_info = get_stream_info(rtmp_url)
    print(f"Stream Info: {stream_info}")  # Debugging line
    if isinstance(stream_info, dict):
        result_output.value = print_stream_info(stream_info)
    else:
        result_output.value = stream_info

# UI Elements
ui.label('RTMP Stream Diagnostics')
url_input = ui.input('Enter the RTMP URL:')
ui.button('Analyze Stream', on_click=analyze_stream)

# Section to display stream stats
result_output = ui.label('').style('white-space: pre-wrap;')  # Preserve formatting

ui.run(port=8082)