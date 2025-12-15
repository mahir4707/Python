# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# from openai import OpenAI

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = "85956cb77d3f4c9a9645629e245da4bc"

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def aiProcess(command):
#     client = OpenAI(api_key= "OPEN_AI_KEY")

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a virtual assistant, skilled in performing general tasks like alexa and google cloud."
#         },
#         {
#             "role": "user",
#             "content": "what is coding?"
#         }
#     ]
# )

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("http://google.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("http://youtube.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("http://linkedin.com")
#     elif c.lower().startswith("plays"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link)

#     elif "news" in c.lower():
#         r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
#         if r.status_code == 200:
#             #parse the JSON response
#             data = r.json()

#             #extract the article
#             articles = data.get('articles', [])

#             #print the headlines
#             for article in articles:
#                 speak(article['title'])



# if __name__ == "__main__":
#     speak("Initializing Jarvis...")
#     while True:
#         # Listen for the word "Jarvis"
#         # obtain audio from the microphone
            
#         r = sr.Recognizer()
#         print("recognizing...")

#         try:
#             with sr.Microphone() as source:
#                 print("Listening..")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if(word.lower() == "hello"):
#                 speak("Ya")
#                 #Listen for command
#                 with sr.Microphone() as source:
#                     print("Listening...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processCommand(command)
                

#         except Exception as e:
#                 print("Error: {0}".format(e))


import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

# ------------------ INITIALIZATION ------------------

recognizer = sr.Recognizer()
engine = pyttsx3.init()

NEWS_API_KEY = "85956cb77d3f4c9a9645629e245da4bc"   # move key to variable


# ------------------ SPEAK FUNCTION ------------------

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ------------------ AI PROCESS FUNCTION ------------------

def aiProcess(command):
    client = OpenAI(api_key="OPENAI_API_KEY")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant, skilled in performing general tasks like Alexa and Google Assistant."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content

# ------------------ COMMAND PROCESSING ------------------

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        link = musicLibrary.music.get(song)

        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in library")

    elif "news" in c:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            for article in articles[:5]:   # limit news
                speak(article.get("title", "No title available"))
        else:
            speak("Unable to fetch news")

    else:
        # fallback to AI
        response = aiProcess(c)
        speak(response)

# ------------------ MAIN LOOP ------------------

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)

            if word.lower() == "hello":
                speak("Yes")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.WaitTimeoutError:
            continue
        except Exception as e:
            print("Error:", e)
