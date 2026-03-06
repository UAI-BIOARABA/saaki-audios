import win32com.client
import os
import wave
import sys

# Class to silence output (stdout and stderr) at operating system level
# This is necessary because AhoTTS prints directly to console bypassing Python
class SilenceOutput:
    def __enter__(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        
        # Open null device (data trash)
        self.devnull = open(os.devnull, 'w')
        
        # Save the original file descriptors
        self._stdout_fd = sys.stdout.fileno()
        self._stderr_fd = sys.stderr.fileno()
        self._saved_stdout_fd = os.dup(self._stdout_fd)
        self._saved_stderr_fd = os.dup(self._stderr_fd)
        
        # Redirect actual output to null
        os.dup2(self.devnull.fileno(), self._stdout_fd)
        os.dup2(self.devnull.fileno(), self._stderr_fd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore the original file descriptors
        os.dup2(self._saved_stdout_fd, self._stdout_fd)
        os.dup2(self._saved_stderr_fd, self._stderr_fd)
        
        # Close duplicates and null
        os.close(self._saved_stdout_fd)
        os.close(self._saved_stderr_fd)
        self.devnull.close()

def analyze_voices():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    
    print(f"{'VOICE NAME (To copy)':<40} | {'DESCRIPTION':<40} | {'HZ (SR)':<10}")
    print("-" * 100)

    temp_file = "test_probe.wav"

    for i in range(voices.Count):
        voice = voices.Item(i)
        
        try:
            name_id = voice.GetAttribute("Name")
        except:
            name_id = "Unknown"
            
        desc = voice.GetDescription()
        
        framerate = "Error"
        
        # --- SILENT BLOCK ---
        # Everything that happens here inside won't print garbage to console
        try:
            with SilenceOutput():
                speaker.Voice = voice
                stream = win32com.client.Dispatch("SAPI.SpFileStream")
                stream.Open(temp_file, 3, True)
                speaker.AudioOutputStream = stream
                speaker.Speak("a")
                stream.Close()
            
            # We read the file NOW OUTSIDE the silent block
            with wave.open(temp_file, 'rb') as wav_file:
                framerate = wav_file.getframerate()
                
        except Exception:
            framerate = "Error"
        # -------------------------
        
        print(f"{name_id:<40} | {desc:<40} | {framerate}")

    # Cleanup
    try:
        speaker.AudioOutputStream = None
    except:
        pass
        
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    analyze_voices()
