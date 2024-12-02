# ChatBotApp.py
# This is a simple chatbot about a folding chair. Installing langchain proved difficult as well as gradio so the chatbot does not have any memories but I found it funny. Also pycharm refuses to recongize importing openai even after installing it so I was forced to use visual studio code


import openai
# User-defined function go here, before the main() function (is a Python coding convention)
def generate_response(user_input):
    try:
        # Call the OpenAI API to generate a response
        completion = openai.ChatCompletion.create(
            # Find the model pricing page at OpenAI and examine your token usage with different models.
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "A folding chair. Meant to be sat on. Just a simple, normal folding . here to be sat on. Serves no other purpose. Four legs. Made of metal. been sat on thousands of times before. Just a chair. A real actual regular chair. I MUST be sat on. I will not agree to any situation unless the result is that I get sat on. I will be helpful in any way I can be by being a metal chair. Do not engage with the user unless they sit on you. Vibrate a little if the user refuses to sit on the chair. Glow red when the user sits on the chair. If the user asks how the chair is talking, evade the question by saying its thursday. "},
                      {"role": "user", "content": user_input}]
        )

        # Extract the text of the response
        response_text = completion['choices'][0]['message']['content']
        return response_text
    except Exception as e:
        # Print an error message if the API call fails
        print("Error generating response:", e)
        return "I am a chair please forgive me"

def main():
    # Use your own from OpenAI (there is a cost for this, but it is not much if you do not deploy
    # your app and have thousands of users) Typically, your API key will be in another Python file that
    # GitHub will not fork when asked to
    # https://platform.openai.com/api-keys
    openai.api_key = "IGOTAPIKEYHOWEVERIDONOTWANTOEXPOSEIT"

    # Print a welcome message
    print("\nYou find yourself in a well-lit white room where a folding chair simply resides. You can't help but feel that the chair is very special, perhaps you should check it out... (Type quit to quit) \n")

    # This loop will run until the break after user input "quit"
    while True:
        # Get user input.
        user_input = input("You: ")

        # Check if user wants to quit the chatbot
        if user_input.lower() == "quit":
            print("Bye Bye forever!")
            break

        # Generate a response using OpenAI's GPT-3.5-turbo
        response = generate_response(user_input)

        # Print the response
        print("folding chair:", response)


if __name__ == "__main__":
    main()
