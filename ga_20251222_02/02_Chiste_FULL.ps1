$lista = "02_Chiste_FULL_lista.txt"

@"
file '02_Chiste_1_A__PROC22.wav'
file 'silencio_1000ms.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_1_B__PROC22.wav'
file 'silencio_0300ms.wav'
file 'bad-joke-drum-352439.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_2_A__PROC22.wav'
file 'silencio_1000ms.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_2_B__PROC22.wav'
file 'silencio_0300ms.wav'
file 'child-laughing-90664.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_3_A__PROC22.wav'
file 'silencio_1000ms.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_3_B__PROC22.wav'
file 'silencio_0300ms.wav'
file 'bad-joke-drum-352439.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_4_A__PROC22.wav'
file 'silencio_1000ms.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_4_B__PROC22.wav'
file 'silencio_0300ms.wav'
file 'child-laughing-90664.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_5_A__PROC22.wav'
file 'silencio_1000ms.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_5_B__PROC22.wav'
file 'silencio_0300ms.wav'
file 'bad-joke-drum-352439.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_6_A__PROC22.wav'
file 'silencio_1000ms.wav'
file 'silencio_1000ms.wav'
file '02_Chiste_6_B__PROC22.wav'
file 'silencio_0300ms.wav'
file 'child-laughing-90664.wav'
file 'silencio_1000ms.wav'

"@ | Set-Content -Encoding ASCII $lista

# Ejecutar ffmpeg
# ffmpeg -f concat -safe 0 -i $lista -c copy 02_Chiste_FULL.wav -y
ffmpeg -f concat -safe 0 -i $lista -ar 22050 -ac 1 -c:a pcm_s16le 02_Chiste_FULL.wav -y

# (Opcional) borrar la lista
Remove-Item $lista

