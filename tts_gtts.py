from gtts import gTTS
import os
import platform
import tempfile
import sys

def play_file_cross_platform(path):
    """Play an audio file in the default player across OSes."""
    plat = platform.system()
    try:
        if plat == "Windows":
            os.startfile(path)               # Windows
        elif plat == "Darwin":
            os.system(f"open \"{path}\"")   # macOS
        else:
            # Linux
            # try xdg-open (most distros), otherwise try mpg123
            if os.system(f"xdg-open \"{path}\"") != 0:
                os.system(f"mpg123 \"{path}\"")  # may fail if not installed
    except Exception as e:
        print("Play error:", e)

def tts_gtts(text: str, lang: str = "hi", filename: str = None, play: bool = True):
    """
    text: text to convert
    lang: language code, 'hi' for Hindi, 'en' for English, etc.
    filename: if provided, save mp3 to this filename; otherwise use a temp file
    """
    if not filename:
        fd, filename = tempfile.mkstemp(suffix=".mp3")
        os.close(fd)

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"Saved TTS to: {filename}")

    if play:
        play_file_cross_platform(filename)

    return filename

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Namaste! It's a demo of gtts."
    tts_gtts(text, lang="hi", play=True)
