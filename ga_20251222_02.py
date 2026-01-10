# import win32com.client
# import subprocess
# import os

# bloques = [
#     (
#         "AhoTTS_Alba_es",
#         "Hola a todas y todos. Soy Saaki. Os quiero dar las gracias por venir a verme, tenía muchas ganas de conoceros. Hoy vamos a jugar juntos y a hacer cosas muy divertidas. Esto es un juego, y como en todos los juegos hay unas normas. La más importante: no podeís tocarme. Solo se puede tocar si Juan lo dice. Dejad un poco de espacio delante mío, pero acercaros, así jugaremos mejor. Si algo no os gusta u os da un poco de miedo, decídselo a Juan, que está aquí para ayudar. ¿Estáis preparadas y preparados?",
#         "01_INTRO.wav",
#         0.90,  # tempo
#         2.8,  # semitonos
#         44100,  # sample rate
#     ),
# ]

# FFMPEG = "ffmpeg"  # o ruta completa si no está en PATH
# INPUT_SR = 22050  # el SR real del WAV SAPI

# for voz, texto, archivo, tempo, semitonos, sr in bloques:
#     # ========================
#     # 1️⃣ Generar TTS
#     # ========================
#     speaker = win32com.client.Dispatch("SAPI.SpVoice")
#     speaker.Voice = speaker.GetVoices(f"Name={voz}").Item(0)

#     stream = win32com.client.Dispatch("SAPI.SpFileStream")
#     stream.Open(archivo, 3, True)
#     speaker.AudioOutputStream = stream

#     speaker.Speak(texto)
#     stream.Close()

#     print(f"TTS generado: {archivo}")

#     # ========================
#     # 2️⃣ Procesar con FFmpeg
#     # ========================
#     base, _ = os.path.splitext(archivo)
#     salida = f"{base}__PROC22.wav"

#     # filtro = (
#     #     f"atempo={tempo}," f"asetrate={sr}*pow(2\\,{semitonos}/12)," f"aresample={sr}"
#     # )
#     filtro = (
#         f"asetrate={INPUT_SR}*pow(2\\,{semitonos}/12),"
#         f"aresample={INPUT_SR},"
#         f"atempo={tempo}"
#     )

#     cmd = [FFMPEG, "-y", "-i", archivo, "-af", filtro, salida]

#     subprocess.run(cmd, check=True)

#     print(f"Audio procesado: {salida}")


import win32com.client
import subprocess
import os
from datetime import datetime

# ========================
# Configuración de carpeta
# ========================
carpeta_output = "ga_20251222_02"

# Crear carpeta si no existe
if not os.path.exists(carpeta_output):
    os.makedirs(carpeta_output)
    print(f"Carpeta creada: {carpeta_output}")

bloques = [
    # (
    #     "AhoTTS_Alba_es",
    #     "Hola a todas y todos. Soy Saaki. Os quiero dar las gracias por venir a verme, tenía muchas ganas de conoceros. Hoy vamos a jugar juntos y a hacer cosas muy divertidas. Esto es un juego, y como en todos los juegos hay unas normas. La más importante: no podeís tocarme. Solo se puede tocar si Juan lo dice. Dejad un poco de espacio delante mío, pero acercaros, así jugaremos mejor. Si algo no os gusta u os da un poco de miedo, decídselo a Juan, que está aquí para ayudar. ¿Estáis preparadas y preparados?",
    #     "01_INTRO.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "¿Qué hace una vaca cuando sale el sol?",
    #     "02_Chiste_1_A.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Sombra.",
    #     "02_Chiste_1_B.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "¿Qué le dice un semáforo a otro?",
    #     "02_Chiste_2_A.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "“No me mires, que me pongo rojo.",
    #     "02_Chiste_2_B.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "¿Qué le dice una pared a la otra?",
    #     "02_Chiste_3_A.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Nos vemos en la esquina.",
    #     "02_Chiste_3_B.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "¿Sabéis por qué el matemático estaba tranquilo?",
    #     "02_Chiste_4_A.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Porque ya lo tenía todo calculado.",
    #     "02_Chiste_4_B.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "¿Qué le dice un techo a otro?",
    #     "02_Chiste_5_A.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Techo de menos.",
    #     "02_Chiste_5_B.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "¿Por qué el robot no podía dormir?",
    #     "02_Chiste_5_A.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Porque tenía demasiadas ventanas abiertas.",
    #     "02_Chiste_5_B.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "¿Cuál es el río más moderno de España?",
    #     "02_Chiste_6_A.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "El río, E, Bro.",
    #     "02_Chiste_6_B.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Ahora, miradme bien. Todo lo que yo haga, lo teneis que copiar y hacerlo igual igual. ¿Preparadas y preparados?. Vamos allá.",
    #     "03_IMITAR.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Muy bien. Lo habéis hecho genial. Ha llegado el momento de hacer algo muy especial. Algo mágico. Lo que pasa es, que sólo va a funcionar si me ayudais todas y todos vosotros. Voy a poner una canción. Pero, solo tendré energía suficiente para bailar si todas y todos bailáis. Si lo hacéis bien, entonces podré bailar, pero si no lo dais todo, no tendré energía suficiente para bailar. ¿Os atrevéis a intentarlo?",
    #     "04_BAILE.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Bufffffff, es increíble la energía que tenéis, cómo se nota que soís jóvenes, no como Juan, que no me oiga...",
    #     "05_RELAX_A.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Ahora paramos un momento. Vamos a estar tranquilas y tranquilos. Nos vamos a sentar en el suelo, vamos a respirar despacio y a relajarnos un poco. Juan nos va a decir el ritmo que tenemos que seguir. Cuando hayamos terminado, nos levantaremos muy muy despacio.",
    #     "05_RELAX_B.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Gracias por jugar conmigo. Me lo he pasado muy bien, espero que vosotras y vosotros también. Ahora si queréis, podemos hacernos unas fotos por grupos. Esperad un poco para que os digan como nos organizamos. Os quiero. Hasta pronto.",
    #     "06_CIERRE.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
    (
        "AhoTTS_Ainara_eu",
        "Kaixo. Zer moduz? Gustatu zaizue ni ezagutzea? Nik oso ondo pasatu dut. Nigana hurbildu zaitezkete geldirik banago. Mesedez, ez bultzatu.",
        "10_ARGAZKI.wav",
        0.80,  # tempo
        2.7,  # semitonos
        44100,  # sample rate
    ),
    # (
    #     "AhoTTS_Alba_es",
    #     "Hola. ¿Qué tal? ¿Os ha gustado conocerme? Yo me lo he pasado muy bien. Podéis acercaros a mí si estoy quieto. Por favor, no me empujéis.",
    #     "10_FOTO.wav",
    #     0.90,  # tempo
    #     2.8,  # semitonos
    #     44100,  # sample rate
    # ),
]

FFMPEG = "ffmpeg"  # o ruta completa si no está en PATH
INPUT_SR = 22050  # el SR real del WAV SAPI

for voz, texto, archivo, tempo, semitonos, sr in bloques:
    # ========================
    # 1️⃣ Generar TTS
    # ========================
    # Ruta completa para el archivo temporal en carpeta de salida
    archivo_temp = os.path.join(carpeta_output, archivo)

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Voice = speaker.GetVoices(f"Name={voz}").Item(0)

    stream = win32com.client.Dispatch("SAPI.SpFileStream")
    stream.Open(archivo_temp, 3, True)
    speaker.AudioOutputStream = stream

    speaker.Speak(texto)
    stream.Close()

    print(f"TTS generado: {archivo_temp}")

    # ========================
    # 2️⃣ Procesar con FFmpeg
    # ========================
    base, _ = os.path.splitext(archivo)
    salida_final = f"{base}__PROC22.wav"
    salida_final_path = os.path.join(carpeta_output, salida_final)

    filtro = (
        f"asetrate={INPUT_SR}*pow(2\\,{semitonos}/12),"
        f"aresample={INPUT_SR},"
        f"atempo={tempo}"
    )

    cmd = [FFMPEG, "-y", "-i", archivo_temp, "-af", filtro, salida_final_path]

    subprocess.run(cmd, check=True)

    print(f"Audio procesado: {salida_final_path}")

    # ========================
    # 3️⃣ Eliminar archivo temporal
    # ========================
    if os.path.exists(archivo_temp):
        os.remove(archivo_temp)
        print(f"Archivo temporal eliminado: {archivo_temp}")

print(
    f"\nProceso completado. Solo queda el archivo __PROC22.wav en la carpeta '{carpeta_output}'"
)
