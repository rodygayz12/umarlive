import subprocess

# Replace with your video path
video_path = "video.mp4"

# Replace with your Youtube stream key (get from Youtube Studio)
youtube_stream_key = "ptv1-prvf-rwe4-0wx9-99pm"

def start_stream():
  """Starts live stream using ffmpeg."""
  command = [
      "ffmpeg",
      "-re",  # Loop playback
      "-i", video_path,  # Input video file
      "-c:v", "copy",  # Copy video stream
      "-c:a", "aac",  # Encode audio to AAC
      "-b:a", "192k",  # Set audio bitrate
      "-f", "flv",  # Output format (RTMP compatible)
      f"rtmp://a.rtmp.youtube.com/live2/{youtube_stream_key}",  # Youtube RTMP URL
  ]

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

if __name__ == "__main__":
  print("Starting live stream...")
  start_stream()
