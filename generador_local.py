import win32com.client
import subprocess
import os
import sys

# ==========================================
# 🔇 CLASE PARA SILENCIAR AVISOS DURANTE EL PROCESO: [aHoTTS warn]: Can't use HDic database '.dic'
# ==========================================
class SilenciarSalida:
    """
    Redirige temporalmente stdout y stderr a devnull para ocultar
    los warnings de bajo nivel (C++) de las voces AhoTTS.
    """
    def __enter__(self):
        self._stdout_fd = sys.stdout.fileno()
        self._stderr_fd = sys.stderr.fileno()
        self._saved_stdout_fd = os.dup(self._stdout_fd)
        self._saved_stderr_fd = os.dup(self._stderr_fd)
        
        self.devnull = open(os.devnull, 'w')
        os.dup2(self.devnull.fileno(), self._stdout_fd)
        os.dup2(self.devnull.fileno(), self._stderr_fd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.dup2(self._saved_stdout_fd, self._stdout_fd)
        os.dup2(self._saved_stderr_fd, self._stderr_fd)
        os.close(self._saved_stdout_fd)
        os.close(self._saved_stderr_fd)
        self.devnull.close()

# ==========================================
# ⚙️ CONFIGURACIÓN
# ==========================================
CARPETA_SALIDA = "audios_locales"
FFMPEG_CMD = "ffmpeg"  # Asegúrate de que ffmpeg esté instalado y en el PATH

# Parámetros del efecto de voz
TEMPO = 0.92      # Velocidad
SEMITONOS = 1.75   # Cuánto agudizar la voz (Pitch)
INPUT_SR = 22050  # Frecuencia de muestreo de las voces AhoTTS 
OUTPUT_SR = 16000 # Cambiamos la frecuencia de salida, necesario 16000 para el robot

# Lista de audios a generar
bloques = [
    {
        "voz": "AhoTTS_Alba_es",
        "texto": "Hoy es jueves, bienvenido a tu asistente de voz local.",
        "archivo": "Saludo_ES.wav"
    },
    {
        "voz": "AhoTTS_Ainara_eu",
        "texto": "Ostegun da, ongi etorri zure ahots-laguntzaile lokalera.",
        "archivo": "Saludo_EU.wav"
    }
]

def generar_audio_local():
    if not os.path.exists(CARPETA_SALIDA):
        os.makedirs(CARPETA_SALIDA)

    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    for item in bloques:
        nombre_voz = item["voz"]
        texto = item["texto"]
        archivo_final = item["archivo"]
        
        # 1. Buscar la voz en el sistema (Silenciando warnings de carga)
        try:
            with SilenciarSalida():
                speaker.Voice = speaker.GetVoices(f"Name={nombre_voz}").Item(0)
        except:
            # Si falla, el bloque 'with' termina y restaura la consola, así que este print SÍ se ve.
            print(f"⚠️  AVISO: No se encontró la voz '{nombre_voz}'. Usando la predeterminada.")

        # 2. Generar archivo temporal (Voz normal)
        archivo_temp = os.path.join(CARPETA_SALIDA, "temp_" + archivo_final)
        
        stream = win32com.client.Dispatch("SAPI.SpFileStream")
        stream.Open(archivo_temp, 3, True)
        speaker.AudioOutputStream = stream
        
        # Silenciamos el momento de hablar, que es donde AhoTTS suele quejarse del diccionario
        with SilenciarSalida():
            speaker.Speak(texto)
            
        stream.Close()
        
        print(f"\n🎙️  TTS Base generado: {archivo_temp}")

        # 3. Procesar con FFmpeg (Aplicar efecto niño)
        ruta_final = os.path.join(CARPETA_SALIDA, archivo_final)
        
        filtro = (
            f"asetrate={INPUT_SR}*pow(2\\,{SEMITONOS}/12),"
            f"aresample={OUTPUT_SR},"
            f"atempo={TEMPO}"
        )

        cmd = [FFMPEG_CMD, "-y", "-i", archivo_temp, "-af", filtro, ruta_final]

        try:
            # subprocess también tiene sus propios streams, los mandamos a DEVNULL para que FFmpeg no llene la pantalla
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✨ Procesado con éxito: {ruta_final}")
        except FileNotFoundError:
            print("❌ ERROR CRÍTICO: No se encontró 'ffmpeg'. Instálalo o revisa el PATH.")
            break
        except Exception as e:
            print(f"❌ Error procesando audio: {e}")

        # 4. Limpieza
        if os.path.exists(archivo_temp):
            os.remove(archivo_temp)

    print("\n🏁 Proceso local completado.")

if __name__ == "__main__":
    generar_audio_local()