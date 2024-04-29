from g4f.client import Client
from g4f.cookies import set_cookies
import g4f
from flask import Flask, Response, request, redirect, url_for, send_file, abort
import flask
import docs
import requests as req
import os
import json
from io import BytesIO
set_cookies(".google.com", eval(os.environ["GAPI"]))
client = Client()
app = Flask("JoveAPI")
        
def twae(e):
    yield f"There was an error loading the response!\n{e.__class__.__name__}: {e}"
        
def chat_s(rq):
    pvdr = ""
    if "model" in rq.get_json():
      pvdr = rq.get_json()["model"]
    else:
      pvdr = os.environ["CHAT_M"]
    response = client.chat.completions.create(
        model=pvdr,
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
    try:
        return Response(flask.stream_with_context(chat_s(request)))
    except Exception as e:
        return Response(flask.stream_with_context(twae(e)))
    
    
    
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


@app.route("/tenor/<search_term>", methods=["GET"])
def tenorsearch(search_term):
    # set the apikey and limit
    apikey = os.environ["TENOR_KEY"]  # click to set to your apikey
    lmt = 1
    ckey = "joveapi"  # set the client_key for the integration and use the same value for all API calls

    # get the top 8 GIFs for the search term
    r = req.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = r.json()
        return send_file(BytesIO(req.get(top_8gifs["results"][0]["media_formats"]["mediumgif"]["url"]).content), as_attachment=True, mimetype="image/gif", download_name=search_term+".gif")
    else:
        abort(r.status_code)



application = app
