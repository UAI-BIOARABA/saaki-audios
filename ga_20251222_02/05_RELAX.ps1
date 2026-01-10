$lista = "05_RELAX_FULL_lista.txt"

@"
file '05_RELAX_A__PROC22.wav'
file 'child-laughing-90664.wav'
file 'silencio_0500ms.wav'
file '05_RELAX_B__PROC22.wav'

"@ | Set-Content -Encoding ASCII $lista

# Ejecutar ffmpeg
# ffmpeg -f concat -safe 0 -i $lista -c copy 02_Chiste_FULL.wav -y
ffmpeg -f concat -safe 0 -i $lista -ar 22050 -ac 1 -c:a pcm_s16le 05_RELAX_FULL.wav -y

# (Opcional) borrar la lista
Remove-Item $lista

