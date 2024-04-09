class htmldocs:
    ai = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>/ai index</title>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
  header {
    background-color: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
  }
  main {
    padding: 20px;
  }
  footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
    position: fixed;
    bottom: 0;
    width: 100%;
  }
</style>
</head>
<body>
<header>
  <h1>[— /ai docs —]</h1>
  <h4>JoveAPI</h4>
</header>
<main>
  <h2>Endpoint list:</h2>
  <ul>
    <li><a href="#chat">/ai/chat</a></li>
    <li><a href="#image">/ai/image</a></li>
  </ul>
  <h2>Docs:</h2>
  <section id="chat">
    <h3>/ai/chat:</h3>
    <p><strong>Description:</strong> A simple text generation endpoint. Uses google gemini as the model.</p>
    <p><strong>Input type:</strong> application/json</p>
    <p><strong>Output type:</strong> text/plain (streamed)</p>
    <p><strong>Methods:</strong> [POST]</p>
    <p><strong>Saves data?</strong> False</p>
    <p><strong>Auth required?</strong> False</p>
    <p><strong>Input example:</strong></p>
    <pre>{
  "messages": [
    {"role": "user", "content": "hello"},
    ...
  ]
}</pre>
    <p><strong>Credits:</strong> Noah Wilhoite, Google Gemini, g4f</p>
  </section>
  <section id="image">
    <h3>/ai/image:</h3>
    <p><strong>Description:</strong> A simple image generation endpoint. Uses google gemini image generation as the model. Outputs the image URL.</p>
    <p><strong>Input type:</strong> application/json</p>
    <p><strong>Output type:</strong> text/plain</p>
    <p><strong>Methods:</strong> [POST]</p>
    <p><strong>Saves data?</strong> False</p>
    <p><strong>Auth required?</strong> False</p>
    <p><strong>Input example:</strong></p>
    <pre>{
  "prompt": "A medium grey domestic longhair dilute tortie cat."
}</pre>
    <p><strong>Credits:</strong> Noah Wilhoite, Google Gemini, g4f</p>
  </section>
</main>
<footer>
  Last updated: 4/9/2024 (M/D/Y) | ::IP::
</footer>
</body>
</html>
"""[1:-1]
    index = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>index</title>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
  header {
    background-color: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
  }
  main {
    padding: 20px;
  }
  footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
    position: fixed;
    bottom: 0;
    width: 100%;
  }
</style>
</head>
<body>
<header>
  <h1>[— table of contents —]</h1>
  <h4>JoveAPI</h4>
</header>
<main>
  <ul>
    <li><a href="/docs/ai">/ai</a></li>
    <li>/docs (you are here)</li>
    <li><a href="/docs/request">/request</a></li>
  </ul>
</main>
<footer>
  Last updated: 4/9/2024 (M/D/Y) | ::IP::
</footer>
</body>
</html>
"""[1:-1]

ai = """
<pre>
——————————————
[— /ai docs —]
——————————————

Endpoint list:
- /ai/chat
- /ai/image

Docs:
- /ai/chat:
    Description:
    "
    A simple text generation endpoint.
    Uses google gemini as the model.
    "
    Input type: application/json
    Output type: text/plain (streamed)
    Methods: [POST]
    Saves data? False
    Auth required? False
    Input example:
    {
        "messages": {
            [
                {"role": "user", "content": "hello"},
                ...
            ]
        }
    }
    Credits: Noah Wilhoite, Google Gemini, g4f
- /ai/image:
    Description:
    "
    A simple image generation endpoint.
    Uses google gemini image generation as the model.
    Outputs the image URL.
    "
    Input type: application/json
    Output type: text/plain
    Methods: [POST]
    Saves data? False
    Auth required? False
    Input example:
    {
        "prompt": "A medium grey domestic longhair dilute tortie cat."
    }
    Credits: Noah Wilhoite, Google Gemini, g4f

This document was made to fit CLI environments.
Last updated: 4/9/2024 (M/D/Y)
"""[1:-1]