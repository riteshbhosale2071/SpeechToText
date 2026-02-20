# 🎙 Speech-to-Text Transcription Tool (GUI)

A simple Python-based GUI application that converts audio files into
text using SpeechRecognition and automatic format conversion via FFmpeg.

------------------------------------------------------------------------

## 🚀 Features

-   🎧 Supports multiple audio formats (MP3, WAV, M4A, FLAC, OGG, AAC)
-   🔄 Automatic audio format conversion to WAV
-   🖥 Simple Tkinter GUI
-   🌐 Uses Google Speech Recognition API
-   🧾 Displays transcribed text inside the app
-   🗑 Temporary file cleanup after processing

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python 3.11
-   Tkinter (GUI)
-   SpeechRecognition
-   Pydub
-   FFmpeg
-   Google Speech Recognition API

------------------------------------------------------------------------

## 📂 Project Structure

SpeechToTextGUI/
 │ 
 ├── app.py
 ├── requirements.txt 
 └── README.md

------------------------------------------------------------------------

## 📦 Installation

### 1️⃣ Clone the Repository

git clone https://github.com/riteshbhosale2071/SpeechToText.git cd
SpeechToText

### 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv venv`\Scripts`{=tex}`\activate`{=tex}

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Install FFmpeg

Download from: https://ffmpeg.org/download.html

Add FFmpeg bin folder to your system PATH.

Verify installation:

ffmpeg -version

------------------------------------------------------------------------

## ▶️ Usage

Run the application:

python app.py

Steps: 1. Click **Browse** 2. Select an audio file 3. Click **Convert to
Text** 4. View transcription in the text box

------------------------------------------------------------------------

## ⚠️ Requirements

-   Internet connection (for Google Speech Recognition)
-   FFmpeg installed and added to PATH
-   Python 3.11 (recommended)

------------------------------------------------------------------------

## 🔮 Future Improvements

-   🎙 Live microphone recording
-   🌍 Multi-language support
-   💾 Save transcription as .txt file
-   🎨 Modern UI design (CustomTkinter)
-   🤖 Offline speech recognition (Vosk)

------------------------------------------------------------------------

## 👨‍💻 Author

Ritesh Bhosale

------------------------------------------------------------------------

⭐ If you found this project helpful, consider giving it a star!