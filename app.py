# Speech-to-Text Converter (All Formats)
import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from pydub import AudioSegment
import os
import tempfile

def browse_audio():
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.wav *.mp3 *.m4a *.flac *.ogg")]
    )
    audio_path.set(file_path)

def convert_to_wav(input_file):
    sound = AudioSegment.from_file(input_file)
    temp_wav = tempfile.mktemp(suffix=".wav")
    sound.export(temp_wav, format="wav")
    return temp_wav

def transcribe_audio():
    path = audio_path.get()
    if not path:
        messagebox.showerror("Error", "Please select an audio file")
        return

    recognizer = sr.Recognizer()

    try:
        # Convert any format to WAV
        wav_file = convert_to_wav(path)

        with sr.AudioFile(wav_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)

        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

        os.remove(wav_file)  # Delete temp file

    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio")
    except sr.RequestError:
        messagebox.showerror("Error", "Internet connection required")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Speech to Text Converter (All Formats)")
root.geometry("650x420")
root.resizable(False, False)

audio_path = tk.StringVar()

tk.Label(root, text="Speech-to-Text Transcription", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Entry(frame, textvariable=audio_path, width=50).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Browse", command=browse_audio).pack(side=tk.LEFT)

tk.Button(root, text="Convert to Text", command=transcribe_audio,
          bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

text_box = tk.Text(root, height=12, width=75)
text_box.pack(pady=10)

root.mainloop()