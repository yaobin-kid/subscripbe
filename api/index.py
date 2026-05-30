import base64
from flask import Flask, Response
import requests

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def fetch_and_decode(path):
    url = "https://316.sub987.top/weibo/ipx/client/dy?token=230ed32d8d0bf90cbebfae979dc8db4e"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        raw_content = response.text.strip()

        missing_padding = len(raw_content) % 4
        if missing_padding:
            raw_content += "=" * (4 - missing_padding)

        decoded_bytes = base64.b64decode(raw_content)
        try:
            decoded_text = decoded_bytes.decode("utf-8")
            return Response(decoded_text, mimetype="text/plain; charset=utf-8")
        except UnicodeDecodeError:
            return Response(decoded_bytes, mimetype="application/octet-stream")
    except Exception as e:
        return f"错误: {str(e)}", 500
