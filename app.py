from flask import Flask, render_template, request, render_template_string, redirect
import os
import openai
from dotenv import load_dotenv
import json

# Load Environment Variables
load_dotenv()
oaikey = os.getenv("OPENAI_API_KEY")

# Set OpenAI API Key
openai.api_key = oaikey

# Initialize Flask App
app = Flask(__name__)

last_site = {'input': None, 'response': None }

# Render the Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        response = generate_chat_response(input_text)
        ress = render_template_string("{{ response | safe }}", response=response)
        last_site['input'] = input_text
        last_site['response'] = response
        return render_template('home.html', response= response, input = input_text)
    return render_template('home.html')

@app.route('/save', methods=['GET', 'POST'])
def save():
    with open('history.json', 'w') as f:
        json.dump(last_site, f)
    return

@app.route('/history', methods=['GET', 'POST'])
def history():
    return render_template('history.html')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    last_site['input'] = None
    last_site['response'] = None
    return redirect('/')

    # response = openai.Completion.create(
    #     engine="davinci",
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.7,
    # )

browse = "I want you to act as a text based web browser browsing an imaginary internet. You should only reply with the contents of the page, nothing else. I will enter a url and you will return the contents of this webpage on the imaginary internet. Don't write explanations. Links on the pages should have numbers next to them written between []. When I want to follow a link, I will reply with the number of the link. Inputs on the pages should have numbers next to them written between []. Input placeholder should be written between (). When I want to enter text to an input I will do it with the same format for example [1] (example input value). This inserts 'example input value' into the input numbered 1. When I want to go back i will write (b). When I want to go forward I will write (f). My first prompt is google.com"
stop = ["\"\"\""]
# start_prompt = "I want you to act as a web developer. You will respond to my prompts with HTML, CSS or JS code. all your responces will be in proper tag's so they can be rendered in a browser. My first prompt is " 
start_prompt = "Respond to the following prompt with only HTML, CSS and JS code which can be rendered inside the <body> of a flask template. All responces must have proper tags so they can be rendered directly  "
# Generate Chat Response using OpenAI API
# caviats = ". Make sure the css and js are in proper tags <style></style> <script></script> so they can be rendered in a single page. All images should be drawn in css or svgs"

# caviats = '. All results should be passed in a python dictionary format with the following keys. {"html": html, "css": css, "js": js, "image": {"prompt": prompt, "size":size } }."'

caviats = ''
start_message = [
    {"role": "system", "content": f"{start_prompt} {caviats}"},
    ]

messages = start_message  
def image_gen():
    response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def generate_chat_response(input_text):
    messages.append({"role": "user", "content": f'{input_text}'})
    prompt = f"{start_prompt}{input_text}{caviats}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=1000,
        top_p=0.5,
        # frequency_penalty=0.0,
        # presence_penalty=0.0,
        # finish_reason = "stop",
        messages=messages,
        stop=["\"\"\""]
    )
    print(response)
    messages.append(response.choices[0]['message'])
    result = response.choices[0]['message']['content']
    print(result)
    return result
    return render_template_string("{{ response | safe }}", response=result)

    return f"{result}"

if __name__ == '__main__':
    app.run(debug=True)