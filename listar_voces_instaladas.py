import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()

print("Voces SAPI instaladas:\n")

for i in range(voices.Count):
    v = voices.Item(i)

    nombre_visible = v.GetDescription()
    try:
        nombre_interno = v.Id.split("\\")[-1]
    except:
        nombre_interno = "Desconocido"

    print(f"- Visible : {nombre_visible}")
    print(f"  Interno : {nombre_interno}\n")
