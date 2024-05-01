from flask import Flask, request

app = Flask(__name__)


def htmlGen(method):
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Form Data</title>
            <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
            <style>
                body {{
                    font-family: 'Pretendard';
                    padding: 20px;
                }}
                h1 {{
                    margin-bottom: 20px;
                }}
                p {{
                    margin-bottom: 5px;
                }}
            </style>
        </head>
        <body>
            <h1>Form Data ({method})</h1>
        </body>
    </html>
    """


@app.route("/", methods=["GET", "POST"])
def formPrint():
    if request.method == "GET":
        data = request.args.to_dict()
        html = htmlGen("GET")
    if request.method == "POST":
        data = request.form.to_dict()
        html = htmlGen("POST")

    for key, value in data.items():
        html += f"<p>{key}: {value}</p>"

    return html


app.run(host="0.0.0.0", port=8000)
