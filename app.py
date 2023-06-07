from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file.mymusic']
    file.save('D:\music')  # Save the file on the server

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()
