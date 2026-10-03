import datetime
import webbrowser

NAME = "Prashik"

def jarvis():
    print("=" * 35)
    print("       JARVIS AI V1")
    print("   Personal AI Assistant")
    print("=" * 35)
    print(f"Hello {NAME}! JARVIS is online.")

    while True:
        command = input("\nYou: ").lower().strip()

        if command in ["exit", "quit", "stop"]:
            print("JARVIS: Goodbye, Prashik!")
            break

        elif command in ["hello", "hi", "hey"]:
            print("JARVIS: Hello! How can I help you?")

        elif "time" in command:
            now = datetime.datetime.now()
            print("JARVIS:", now.strftime("%I:%M %p"))

        elif "date" in command:
            today = datetime.date.today()
            print("JARVIS:", today.strftime("%d %B %Y"))

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            print("JARVIS: Opening YouTube.")

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            print("JARVIS: Opening Google.")

        elif "your name" in command:
            print("JARVIS: I am JARVIS, your assistant.")

        else:
            print("JARVIS: I don't understand that yet.")

if __name__ == "__main__":
    jarvis()