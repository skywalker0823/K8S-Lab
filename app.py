from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/healthy")
def healthy():
    return "healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)


# Step by step record :)

# Install requirements
# pip3 install -r requirements.txt

# Local test app
# python3 app.py

# Build image for this app
# docker build -t eddiepxl/sample-app:latest .   

# local test flight 
# docker run -dp 3000:3000 --name sample-app eddiepxl/sample-app:latest

# Push to docker hub
# docker push eddiepxl/sample-app:latest
# Remember to check if it's successed






