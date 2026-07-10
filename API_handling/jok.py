import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()

    setup = data["setup"]
    punchline = data["punchline"]

    return setup, punchline


def main():
    try:
        setup, punchline = fetch_joke()
        print(f"Joke: {setup}")
        print(f"Answer: {punchline}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()