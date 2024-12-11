import requests
import webbrowser
# from engine.features import chatBot  # Assuming this handles chatbot-related tasks
import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

def search_web(query):
    """Fallback to search on Google."""
    speak("Searching the web for you.")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"I've found some results on the web for: {query}"

def get_weather(city="Mumbai"):
    """Fetch weather information using OpenWeatherMap API."""
    try:
        api_key = "your_openweather_api_key"  # Replace with actual API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        if weather_data.get("cod") != 200:
            return "I couldn't fetch the weather data. Please try again."
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        return f"The temperature in {city} is {temperature}°C with {description}."
    except Exception as e:
        return "I encountered an error while retrieving the weather data."

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    
    try:
        if "temperature" in query or "weather" in query:
            speak("Let me check the weather.")
            city = "Mumbai"  # Modify to dynamically detect city if needed
            response = get_weather(city)
            speak(response)
        
        elif "search" in query or "google" in query:
            speak("What should I search for?")
            search_query = takecommand()
            response = search_web(search_query)
            speak(response)
        
        elif "play music" in query:
            from engine.features import playMusic
            playMusic()
        
        elif "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        else:
            return 
        #     # Use ChatBot for general questions
        #     response = chatBot(query)
        #     if response:
        #         speak(response)
        #     else:
        #         response = search_web(query)
                # speak(response)
    
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I encountered an error while processing your query.")
        eel.ShowHood()

    