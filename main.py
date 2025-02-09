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
    with ui.card().classes('no-shadow border-[1px]'):
        with ui.grid(columns=2):  # Create a grid layout for displaying stream info
            for stream in stream_info.get('streams', []):
                with ui.element('div').classes('p-2 bg-blue-300'):
                    output.append(f"Stream Index: {stream.get('index')}")
                    ui.label("Stream Index:").style('font-weight: bold')
                with ui.element('div').classes('p-2 bg-blue-100'):
                    output.append(f"{stream.get('index')}")
                    ui.label(f"{stream.get('index')}")
                output.append(f"Codec Name: {stream.get('codec_name')}")
                ui.label("Codec Name:").style('font-weight: bold')
                ui.label(f"{stream.get('codec_name')}")
                output.append(f"Codec Type: {stream.get('codec_type')}")
                ui.label("Codec Type:").style('font-weight: bold')
                ui.label(f"{stream.get('codec_type')}")
                if 'width' in stream and 'height' in stream:
                    resolution = f"{stream['width']}x{stream['height']}"
                    output.append(f"Resolution: {resolution}")
                    ui.label("Resolution:").style('font-weight: bold')
                    ui.label(f"{resolution}")
                if 'sample_rate' in stream:
                    output.append(f"Sample Rate: {stream['sample_rate']}")
                    ui.label("Sample Rate:").style('font-weight: bold')
                    ui.label(f"{stream['sample_rate']}")
                if 'pix_fmt' in stream:
                    output.append(f"Pixel Format: {stream['pix_fmt']}")
                    ui.label("Pixel Format:").style('font-weight: bold')
                    ui.label(f"{stream['pix_fmt']}")
                output.append(f"Duration: {stream.get('duration')} seconds")
                ui.label("Duration:").style('font-weight: bold')
                ui.label(f"{stream.get('duration')} seconds")
                output.append(f"Bitrate: {stream.get('bit_rate')} bps")
                ui.label("Bitrate:").style('font-weight: bold')
                ui.label(f"{stream.get('bit_rate')} bps")
                output.append("-" * 30)

    # Join the output list into a single string
    return "\n".join(output)

def update_stream_info(info):
    stream_info_display.value = info

# Update the analyze_stream function to use the new display
def analyze_stream():
    rtmp_url = url_input.value
    print(f"Analyzing RTMP URL: {rtmp_url}")  # Debugging line
    if not rtmp_url:
        result_output.value = "Please enter a valid RTMP URL."
        return

    stream_info = get_stream_info(rtmp_url)
    print(f"Stream Info: {stream_info}")  # Debugging line
    if isinstance(stream_info, dict):
        update_stream_info(print_stream_info(stream_info))  # Update the detailed stream info display
    else:
        result_output.value = stream_info


# UI Elements
with ui.card().classes('no-shadow border-[1px]'):

    ui.label('RTMP Stream Diagnostics').style('display: block; margin-left: auto; margin-right: auto;')
    url_input = ui.input('Enter the RTMP URL:').style('display: block; margin-left: auto; margin-right: auto;')
    ui.button('Analyze Stream', on_click=analyze_stream).style('display: block; margin-left: auto; margin-right: auto;')


ui.query('body').classes('bg-gradient-to-t from-blue-600 to-blue-300')

ui.run()
# Run the UI
ui.run(port=8080)  # Change the port as needed