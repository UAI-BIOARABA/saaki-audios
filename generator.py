import win32com.client
import subprocess
import os

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
OUTPUT_FOLDER = "audios"
FFMPEG_CMD = "ffmpeg"  # Make sure ffmpeg is installed and in the PATH

# Voice effect parameters
TEMPO = 0.90      # Speed
SEMITONES = 2.8   # How much to sharpen the voice (Pitch)
INPUT_SR = 22050  # Sample rate of AhoTTS voices
OUTPUT_SR = 16000 # Change the output frequency, 16000 is required for the robot

# List of audios to generate
blocks = [
    {
        "voice": "", # Write the exact name of the voice you want to use installed on your system, or leave empty for the default
        "text": "Today is Thursday, welcome to your local voice assistant.",
        "file": "Greeting_EN.wav"
    },
    {
        "voice": "", # Write the exact name of the voice you want to use installed on your system, or leave empty for the default
        "text": "Ostegun da, ongi etorri zure ahots-laguntzaile lokalera.",
        "file": "Greeting_EU.wav"
    }

    # More blocks can be added here, just follow the same structure. 
    # The "file" field is the name of the output file that will be generated in the OUTPUT_FOLDER. 
    # Make sure to include the .wav extension.
]

def generate_local_audio():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    for item in blocks:
        voice_name = item["voice"]
        text = item["text"]
        final_file = item["file"]
        
        # 1. Find the voice in the system (Silencing load warnings)
        try:
            speaker.Voice = speaker.GetVoices(f"Name={voice_name}").Item(0)
        except:
            print(f"\n⚠️   WARNING: Voice '{voice_name}' not found. Using default voice.   ⚠️")

        # 2. Generate temporary file (Normal voice)
        temp_file = os.path.join(OUTPUT_FOLDER, "temp_" + final_file)
        
        stream = win32com.client.Dispatch("SAPI.SpFileStream")
        stream.Open(temp_file, 3, True)
        speaker.AudioOutputStream = stream
        speaker.Speak(text)    
        stream.Close()
        
        print(f"Base TTS generated: {temp_file}")

        # 3. Process with FFmpeg (Apply child effect)
        final_path = os.path.join(OUTPUT_FOLDER, final_file)
        
        # Mathematical formula to raise the pitch
        filter_str = (
            f"asetrate={INPUT_SR}*pow(2\\,{SEMITONES}/12),"
            f"aresample={OUTPUT_SR},"
            f"atempo={TEMPO}"
        )

        cmd = [FFMPEG_CMD, "-y", "-i", temp_file, "-af", filter_str, final_path]

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Successfully processed: {final_path}")
        except FileNotFoundError:
            print("⚠️   CRITICAL ERROR: 'ffmpeg' not found. Install it or check the PATH.   ⚠️")
            break
        except Exception as e:
            print(f"⚠️   Error processing audio: {e}   ⚠️")

        # 4. Cleanup
        if os.path.exists(temp_file):
            os.remove(temp_file)

    print("\nProcess completed.")

if __name__ == "__main__":
    generate_local_audio()
