import speech_recognition as sr


def recognize_speech():
    """
    Records audio from the microphone and converts it to text.
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Speak now...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:
        return "❌ Could not understand the audio."

    except sr.RequestError:
        return "❌ Speech Recognition service is unavailable."

    except Exception as e:
        return f"❌ Error: {e}"