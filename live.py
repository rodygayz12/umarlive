import subprocess
import time

# Replace with your video path (or adjust for URL download as discussed)
video_path = "video.mp4"  # Or URL if using download approach

# Replace with your Youtube stream key (get from Youtube Studio)
youtube_stream_key = "ptv1-prvf-rwe4-0wx9-99pm"

def start_stream():
  """Starts live stream using ffmpeg."""
  command = [
      "ffmpeg",
      "-re",  # Loop playback
      "-i", video_path,  # Input video file (or URL if downloaded)
      "-c:v", "copy",  # Copy video stream
      "-c:a", "aac",  # Encode audio to AAC
      "-b:a", "192k",  # Set audio bitrate
      "-f", "flv",  # Output format (RTMP compatible)
      f"rtmp://a.rtmp.youtube.com/live2/{youtube_stream_key}",  # Youtube RTMP URL
  ]

  # Run ffmpeg in a loop with error handling
  while True:
    # Run ffmpeg with the constructed command
    process = subprocess.Popen(command, stderr=subprocess.PIPE)

    # Capture and print ffmpeg output and errors
    while True:
      output = process.stderr.readline().decode("utf-8").strip()
      if output:
        print(output)
      if process.poll() is not None:
        break

    # Check ffmpeg exit code
    exit_code = process.wait()
    if exit_code != 0:
      print(f"Error streaming video. Exited with code: {exit_code}")

    # Introduce a delay between retries (set to 2 hours)
    time.sleep(2 * 60 * 60)  # Sleep for 2 hours (adjust as needed)

if __name__ == "__main__":
  print("Starting live stream loop...")
  start_stream()
  
