import win32com.client
import os
import wave
import sys

# Clase para silenciar la salida (stdout y stderr) a nivel de sistema operativo
# Esto es necesario porque AhoTTS imprime directamente a la consola saltándose Python
class SilenciarSalida:
    def __enter__(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        
        # Abrir dispositivo nulo (basurero de datos)
        self.devnull = open(os.devnull, 'w')
        
        # Guardar los file descriptors originales
        self._stdout_fd = sys.stdout.fileno()
        self._stderr_fd = sys.stderr.fileno()
        self._saved_stdout_fd = os.dup(self._stdout_fd)
        self._saved_stderr_fd = os.dup(self._stderr_fd)
        
        # Redirigir la salida real al nulo
        os.dup2(self.devnull.fileno(), self._stdout_fd)
        os.dup2(self.devnull.fileno(), self._stderr_fd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restaurar los file descriptors originales
        os.dup2(self._saved_stdout_fd, self._stdout_fd)
        os.dup2(self._saved_stderr_fd, self._stderr_fd)
        
        # Cerrar duplicados y nulo
        os.close(self._saved_stdout_fd)
        os.close(self._saved_stderr_fd)
        self.devnull.close()

def analizar_voces():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voces = speaker.GetVoices()
    
    print(f"{'NOMBRE DE LA VOZ (Para copiar)':<40} | {'DESCRIPCIÓN':<40} | {'HZ (SR)':<10}")
    print("-" * 100)

    archivo_temp = "test_probe.wav"

    for i in range(voces.Count):
        voz = voces.Item(i)
        
        try:
            nombre_id = voz.GetAttribute("Name")
        except:
            nombre_id = "Desconocido"
            
        desc = voz.GetDescription()
        
        framerate = "Error"
        
        # --- BLOQUE SILENCIOSO ---
        # Todo lo que ocurra aquí dentro no imprimirá basura en la consola
        try:
            with SilenciarSalida():
                speaker.Voice = voz
                stream = win32com.client.Dispatch("SAPI.SpFileStream")
                stream.Open(archivo_temp, 3, True)
                speaker.AudioOutputStream = stream
                speaker.Speak("a")
                stream.Close()
            
            # Leemos el archivo YA FUERA del bloque silencioso
            with wave.open(archivo_temp, 'rb') as wav_file:
                framerate = wav_file.getframerate()
                
        except Exception:
            framerate = "Error"
        # -------------------------
        
        print(f"{nombre_id:<40} | {desc:<40} | {framerate}")

    # Limpieza
    try:
        speaker.AudioOutputStream = None
    except:
        pass
        
    if os.path.exists(archivo_temp):
        os.remove(archivo_temp)

if __name__ == "__main__":
    analizar_voces()