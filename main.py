from g4f.client import Client
from g4f.cookies import set_cookies
import g4f
from flask import Flask, Response, request, redirect, url_for, send_file, abort
import flask
import docs
import requests as req



set_cookies(".huggingface.co", {
  "token": "EjbjHwZvZxAOnJzhbIlxgoFiwCNfjvoNrqTZKQkOOQJuatlkwRfiHFFNHkafngCLjJpjLaHZkbTCZDqaKjhmZiHZfTIxJDzqToZGaXMWqNcHKxfinerraVVerniaMPOn"
})
set_cookies(".google.com", {
  "__Secure-1PSID": "g.a000iQgvk0UaP-w9698atETg2E8bLu7B2HHbA1Yfnh_Hae0XKAw5Jj7r_i-inqnGoW76ofhyJAACgYKAWoSAQASFQHGX2MiA8QkEADSfYvETERbtjaK-xoVAUF8yKqrfQdqFH7Ex3Y7RSopr_Y00076"
})
client = Client()
app = Flask("JoveAPI")
        
        
        
def chat_s(rq):
    
    response = client.chat.completions.create(
        provider="Gemini",
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
            model="gemini",
            prompt=rq.get_json()["prompt"],
        )
        return response.data[0].url
    except Exception as e:
        return url_for("ImageError.png")+"?error="+e.__class__.__name__
    

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



if __name__ == '__main__':
    app.run(debug=True)