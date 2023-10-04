import moviepy.editor as mp
import cv2
import numpy as np

# Define the factors for color grading
brightness_factor = 1 # Adjust as needed
contrast_factor = 2    # Adjust as needed
saturation_factor = 1  # Adjust as needed

# Load the input video
input_video = mp.VideoFileClip('videoplayback.mp4')

# Extract the audio from the original video
audio = input_video.audio

# Define a function to adjust brightness, contrast, and saturation
def adjust_color(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to BGR format
    frame = cv2.convertScaleAbs(frame, alpha=brightness_factor, beta=0)
    frame = cv2.addWeighted(frame, contrast_factor, frame, 0, 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * saturation_factor, 0, 255)
    frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)  # Convert back to RGB format
    return frame

# Apply color grading effects to each frame
graded_frames = [adjust_color(frame) for frame in input_video.iter_frames(fps=30)]

# Create a new video with the graded frames
graded_video = mp.ImageSequenceClip(graded_frames, fps=30)

# Set the audio of the graded video to the extracted audio
graded_video = graded_video.set_audio(audio)

# Write the graded video with audio to a file
graded_video.write_videofile('output_video.mp4', codec='libx264', fps=30)

# Close the video objects
input_video.close()
graded_video.close()






