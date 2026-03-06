<div align="center">

<h1> Generador de voz para Saaki - Unitree G1 </h1>

<p>
  <a href="README.md">English</a> |
  <a href="README_es.md">Español</a>
</p>

[![Windows 11](https://img.shields.io/badge/Windows-11-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/windows/windows-11)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Tested on G1](https://img.shields.io/badge/Status-Tested%20on%20Unitree%20G1-success)](#-real-g1-robot)
</div>

## 📖 Descripción

Este repositorio contiene un script para ver las voces de nuestro sistema y otro para crear archivos de audio compatibles con el Unitree G1, que reproduce audio a 16000 Hz.

El script nos permite modificar y ajustar parámetros de voz para hacerla más grave/aguda o más rápida/lenta.

---

## 🛠️ Prerrequisitos

1.  **Python instalado**: Asegúrate de tener Python 3.10 o superior instalado.
2.  **Librerías necesarias**:
    Abre una terminal (CMD o PowerShell) y ejecuta:
    ```bash
    pip install pywin32
    ```
3. **Sistema operativo Windows**

---

## 🎤 Generador de audio

Utiliza las voces instaladas en tu PC y las modifica para ajustarlas al tono y la velocidad deseados.

### Requisitos adicionales

**Voces instaladas**: Debes tener voces de texto a voz instaladas en tu equipo.

- Hay servicios que ofrecen voces para uso personal o gratuito. Asegúrate de conocer los términos de licencia de la voz que quieras usar según tus objetivos.
- Puedes consultar las voces instaladas en tu sistema con el script [list_installed_voices.py](list_installed_voices.py). El script usará la voz predeterminada de Windows (David o Zira) si no encuentra la que se ha indicado.

**FFmpeg**: Debes tener `ffmpeg` instalado y configurado en las variables de entorno de Windows.
1.  **Descarga**: Ve a la página oficial de FFmpeg y en la sección de Windows selecciona los ejecutables de gyan.dev o BtbN. Descarga el archivo .zip o .7z (normalmente llamado "release-essentials" o "full").
2.  **Extrae**: Descomprime el contenido. Verás una carpeta con subcarpetas como bin, doc y presets.
3.  **Ubica**: Mueve la carpeta extraída a la raíz del disco duro (ejemplo: C:\ffmpeg) para localizarla fácilmente.
4.  **Configura PATH**:
        - Busca "Editar las variables de entorno del sistema" en el menú Inicio y ábrelo.
        - Haz clic en el botón Variables de entorno.
        - En "Variables del sistema", selecciona la fila Path y haz clic en Editar.
        - Haz clic en Nuevo y pega la ruta de la carpeta bin de FFmpeg (ejemplo: C:\ffmpeg\bin).
        - Acepta todos los cuadros de diálogo.
5.  **Verificación**: Para confirmar que todo funciona correctamente, abre una nueva ventana de comandos (CMD) y escribe:
        ```cmd
        ffmpeg -version
        ```

### Uso

1.  Abre el archivo `generator.py`.
2.  Modifica la lista `blocks`. Asegúrate de poner el **nombre interno** de la voz instalada en tu PC ([list_installed_voices.py](list_installed_voices.py)).
3.  Ejecuta el script:
    ```bash
    python generator.py
    ```
4.  Los archivos de audio aparecerán en la carpeta `audios`.

---

## 🧑‍💻 Autores

- **Project Manager:** [Juan Fernández](https://github.com/jfbioaraba)
- **Lead Developer:** [Andoni González](https://github.com/andoni92)

---

## Descargo de responsabilidad

Este software y los materiales asociados se proporcionan “tal cual”, sin garantías de ningún tipo, ni expresas ni implícitas, incluyendo —pero no limitándose a— garantías de comercialización, idoneidad para un propósito particular o ausencia de errores.

Los/as autores/as y Bioaraba – Instituto de Investigación Sanitaria no asumen responsabilidad alguna por el uso, la redistribución o la modificación de este repositorio ni por los posibles daños directos o indirectos derivados de su utilización.

Este proyecto tiene fines exclusivos de investigación y/o docencia.
