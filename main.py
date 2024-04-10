from g4f.client import Client
from g4f.cookies import set_cookies
import g4f
from flask import Flask, Response, request, redirect, url_for, send_file, abort
import flask
import docs
import requests as req
import os



set_cookies(".huggingface.co", {
  "token": "EjbjHwZvZxAOnJzhbIlxgoFiwCNfjvoNrqTZKQkOOQJuatlkwRfiHFFNHkafngCLjJpjLaHZkbTCZDqaKjhmZiHZfTIxJDzqToZGaXMWqNcHKxfinerraVVerniaMPOn"
})
set_cookies(".google.com", eval(os.environ["GAPI"]))
client = Client()
app = Flask("JoveAPI")
        
        
        
def chat_s(rq):
    pvdr = "Gemini"
    if "provider" in rq.get_json():
      pvdr = rq.get_json()["provider"]
    else:
      pvdr = os.environ["CHAT_PROV"]
    response = client.chat.completions.create(
        provider=pvdr,
        model="",
        messages=rq.get_json()["messages"],
        stream=True
    )
    for chunk in response:
        if chunk.choices[0].delta.content:
            try:
                yield chunk.choices[0].delta.content or "�"
            except:
                yield "�"

@app.route('/ai/chat', methods=['POST'])
def ai_chat():
    return Response(flask.stream_with_context(chat_s(request)))
    
    
    
def image_s(rq):
    
    try:
        response = client.images.generate(
            model=os.environ["IMAGE_MODEL"],
            prompt=rq.get_json()["prompt"],
        )
        return response.data[0].url
    except Exception as e:
        return f"{e.__class__.__name__}: {e}"
    

@app.route('/ai/image', methods=['POST'])
def ai_image():
    return image_s(request)

@app.route('/ImageError.png', methods=["GET"])
def ImageError_png():
    return send_file("./ImageError.png")


@app.route('/ai', methods=['GET'])
def ai():
    return docs.ai
    
@app.route('/docs/<doc>', methods=["GET"])
def _docs(doc):
    try:
        html = getattr(docs.htmldocs, doc)
        html = html.replace("::IP::", request.remote_addr)
        if html:
            return html
        else:
            abort(404)
    except AttributeError:
        abort(404)

@app.route('/docs', methods=["GET"])
def docs_index():
    return redirect("/docs/index")

@app.route('/', methods=["GET"])
def index():
    return redirect("/docs/index")

@app.route("/abort/<code>")
def _abort(code):
    abort(int(code))



application = app
