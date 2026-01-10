# Generador de Voces para SAAKI (Robot Humanoide)

Este paquete contiene dos herramientas para generar audios.

## 📋 Requisitos Previos

1.  **Python Instalado**: Asegúrate de tener Python 3.x instalado.
2.  **Librerías necesarias**:
    Abre una terminal (CMD o PowerShell) y ejecuta:
    ```bash
    pip install edge-tts pywin32
    ```
3. **Sistema operativo Windows para la versión local**



## 🛠️ OPCIÓN A: Generador Local

Usa las voces instaladas en tu PC (como AhoTTS) y las modifica con un programa externo.

### Requisitos Extra para Opción B

1.  **FFmpeg**: Debes tener instalado `ffmpeg` y configurado en las variables de entorno de Windows.
    * *Prueba*: Escribe `ffmpeg -version` en la terminal. Si sale error, no funcionará.
2.  **Voces Instaladas**: Debes tener las voces instaladas (ej. `AhoTTS_Ainara_eu`). Si no las tienes, el script usará la voz por defecto de Windows (David o Zira).

### Pasos

1.  Abre el archivo `generador_local.py`.
2.  Modifica la lista `bloques`. Asegúrate de poner el **nombre exacto** de la voz instalada en tu PC (puedes verlas ejecutando el archivo PowerShell `_get_pc_voices.ps1` si lo conservas).
3.  Ejecuta el script:
    ```bash
    python generador_local.py
    ```
4.  Los audios aparecerán en la carpeta `audios_locales`.

---

## 🚀 OPCIÓN B: Generador Online

Usa voces neuronales de internet.

1.  Abre el archivo `generador_moderno.py`.
2.  Ve a la sección `LISTA DE FRASES A GENERAR` (hacia el final del archivo).
3.  Añade o modifica los textos que quieras.
4.  Ejecuta el script:
    ```bash
    python generador_moderno.py
    ```
5.  Los audios aparecerán en la carpeta `audios_modernos`.

---