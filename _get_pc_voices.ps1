Add-Type -AssemblyName System.Speech

$speech = New-Object System.Speech.Synthesis.SpeechSynthesizer

# Obtener las voces instaladas
$voces = $speech.GetInstalledVoices() | ForEach-Object { $_.VoiceInfo.Name }

# Exportar a un archivo de texto
$voces | Out-File -FilePath ".\_get_pc_voices.txt" -Encoding UTF8

Write-Host "Voces exportadas a _get_pc_voices.txt"
