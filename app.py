from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the name, username, and server time
    name = "Arulpathi A"
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown_user"
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    # Execute `top` command and capture the output
    top_output = subprocess.getoutput("top -bn1")

    # Render the output as plain text (simple HTML page)
    return f"""
    <html>
        <body>
            <h1>System Information</h1>
            <pre>
            Name: {name}
            Username: {username}
            Server Time (IST): {ist_time}

            TOP output:
            {top_output}
            </pre>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
