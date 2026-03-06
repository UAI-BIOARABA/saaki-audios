<div align="center">

<h1> Voice Generator for Saaki - Unitree G1 </h1>

[![Windows 11](https://img.shields.io/badge/Windows-11-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/windows/windows-11)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Tested on G1](https://img.shields.io/badge/Status-Tested%20on%20Unitree%20G1-success)](#-real-g1-robot)
</div>

---

## 📖 Description

This repository contains a script to view the voices in our system and another to create audio files compatible with the Unitree G1, which plays audio at 16000 Hz.

The script allows us to modify and adjust voice parameters to make it deeper/higher-pitched or faster/slower.

## 🛠️ Prerequisites

1.  **Python Installed**: Make sure you have Python 3.10 or higher installed.
2.  **Required Libraries**:
    Open a terminal (CMD or PowerShell) and run:
    ```bash
    pip install pywin32
    ```
3. **Windows Operating System**

---

## 🚀 Local Generator

Uses voices installed on your PC and modifies them to adjust to the desired tone and speed.

### Extra Requirements

**Installed Voices**: You must have Text-To-Speech voices installed on your computer.

- There are services that offer voices for personal or free use. Make sure you know the license usage terms of the voice you want to use depending on your objectives.
- You can check the voices installed on your system using the [list_installed_voices.py](list_installed_voices.py) script. The script will use the default Windows voice (David or Zira) if it doesn't find the specified one.

**FFmpeg**: You must have `ffmpeg` installed and configured in Windows environment variables.
1.  **Download**: Go to the official FFmpeg page and in the Windows section select the executables from gyan.dev or BtbN. Download the .zip or .7z file (usually called "release-essentials" or "full").
2.  **Extract**: Decompress the contents. You'll see a folder with subfolders like bin, doc and presets.
3.  **Locate**: Move the extracted folder to the root of your hard drive (example: C:\ffmpeg) to make it easy to find.
4.  **Configure PATH**:
        - Search for "Edit environment variables for your system" in the Start menu and open it.
        - Click the Environment variables button.
        - Under "System variables", select the Path row and click Edit.
        - Click New and paste the path to the FFmpeg bin folder (example: C:\ffmpeg\bin).
        - Accept all dialog boxes.
5.  **Verification**: To confirm everything is working correctly, open a new command window (CMD) and type: 
        ```cmd
        ffmpeg -version
        ```

### Usage

1.  Open the `generator.py` file.
2.  Modify the `blocks` list. Make sure to put the **internal name** of the voice installed on your PC ([list_installed_voices.py](list_installed_voices.py)).
3.  Run the script:
    ```bash
    python generator.py
    ```
4.  The audio files will appear in the `audios` folder.

---

## 🧑‍💻 Authors

- **Project Manager:** [Juan Fernández](https://github.com/jfbioaraba)
- **Lead Developer:** [Andoni González](https://github.com/andoni92)

---

## Disclaimer

This software and associated materials are provided "as is", without any warranties of any kind, either express or implied, including—but not limited to—warranties of merchantability, fitness for a particular purpose, or absence of errors.

The authors and Bioaraba – Health Research Institute assume no responsibility for the use, redistribution, or modification of this repository nor for any direct or indirect damages resulting from its use.

This project is intended exclusively for research and/or teaching purposes.

It is not intended for clinical, diagnostic, therapeutic or care use,
nor does it replace certified tools or professional evaluation in healthcare settings.
