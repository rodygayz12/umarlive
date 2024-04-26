const { spawn } = require('child_process');

// Replace with your video path
const videoPath = 'video.mp4';
// Replace with your Youtube stream key (get from Youtube Studio)
const youtubeStreamKey = 'ptv1-prvf-rwe4-0wx9-99pm';

function startStream() {
  const ffmpegProcess = spawn('ffmpeg', [
    '-re',  // Loop playback
    '-i', videoPath,  // Input video file
    '-c:v copy',  // Copy video stream
    '-c:a aac',  // Encode audio to AAC
    '-b:a 192k',  // Set audio bitrate
    '-f flv',  // Output format (RTMP compatible)
    `rtmp://a.rtmp.youtube.com/live2/${youtubeStreamKey}`,  // Youtube RTMP URL
  ]);

  ffmpegProcess.stdout.on('data', (data) => {
    console.log(`FFmpeg Output: ${data}`);
  });

  ffmpegProcess.stderr.on('data', (data) => {
    console.error(`FFmpeg Error: ${data}`);
  });

  ffmpegProcess.on('close', (code) => {
    console.log(`FFmpeg exited with code: ${code}`);
    if (code !== 0) {
      // Handle errors, restart stream if needed
      console.error('Error streaming video. Restarting...');
      startStream();
    }
  });
}

// Start the stream in a loop (adjust delay as needed)
setInterval(startStream, 1000 * 60 * 60); // Start every hour

console.log('Starting live stream loop...');
