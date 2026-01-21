import win32com.client
import subprocess
import os

# ==========================================
# ⚙️ CONFIGURACIÓN
# ==========================================
CARPETA_SALIDA = "audios_locales"
FFMPEG_CMD = "ffmpeg"  # Asegúrate de que ffmpeg esté instalado y en el PATH

# Parámetros del efecto de voz
TEMPO = 0.90      # Velocidad
SEMITONOS = 2.8   # Cuánto agudizar la voz (Pitch)
INPUT_SR = 22050  # Frecuencia de muestreo de las voces AhoTTS 
OUTPUT_SR = 16000 # Cambiamos la frecuencia de salida, necesario 16000 para el robot programando a alto nivel


# Lista de audios a generar
# IMPORTANTE: El nombre de la voz debe coincidir EXACTAMENTE con el instalado (interno) en Windows
bloques = [
    {
        "voz": "AhoTTS_Alba_es", # Cambiar esto para usar otra voz
        "texto": "Hola, Soy Saaki, ¿que tal estáis?",
        "archivo": "Saludo_ES.wav"
    },
    {
        "voz": "AhoTTS_Ainara_eu",
        "texto": "Kaixo, Saaki naiz, zer moduz?",
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
        
        # 1. Buscar la voz en el sistema
        try:
            speaker.Voice = speaker.GetVoices(f"Name={nombre_voz}").Item(0)
        except:
            print(f"⚠️  AVISO: No se encontró la voz '{nombre_voz}'. Usando la predeterminada.")

        # 2. Generar archivo temporal (Voz normal)
        archivo_temp = os.path.join(CARPETA_SALIDA, "temp_" + archivo_final)
        
        stream = win32com.client.Dispatch("SAPI.SpFileStream")
        stream.Open(archivo_temp, 3, True)
        speaker.AudioOutputStream = stream
        speaker.Speak(texto)
        stream.Close()
        
        print(f"🎙️  TTS Base generado: {archivo_temp}")

        # 3. Procesar con FFmpeg (Aplicar efecto niño)
        ruta_final = os.path.join(CARPETA_SALIDA, archivo_final)
        
        # Fórmula matemática para subir el tono
        filtro = (
            f"asetrate={INPUT_SR}*pow(2\\,{SEMITONOS}/12),"
            f"aresample={OUTPUT_SR},"
            f"atempo={TEMPO}"
        )


        cmd = [FFMPEG_CMD, "-y", "-i", archivo_temp, "-af", filtro, ruta_final]

        try:
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