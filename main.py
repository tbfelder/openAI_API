import os
import openai


def chat(message):
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= "You:" + message,
        temperature=0.6,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )

    return response


if __name__ == "__main__":
    response = chat(
        "provide a code example in phyton how to run a flask server with Sqalchemy connection to a postgres database and a dash app frontend",
    )
    message = response.choices[0].text  # main text response
    print(message)
    
