"""
A sample Chat App server
"""
import os
import openai

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():


    # Set your API key
    openai.api_key = ""

    prompt = "Hello, my name is"
    response = openai.Completion.create(
        engine="ada",
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the response
    #print(response.choices[0].text.strip())



    """Return a friendly HTTP greeting."""
    message = response.choices[0].text.strip()

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
