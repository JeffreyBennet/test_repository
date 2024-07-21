
from flask import Flask
from services.github_service import clone_repository
from services.s3_service import upload_to_s3

app = Flask(__name__)

@app.route('/clone-and-upload', methods=['POST'])
def clone_and_upload():
    repo_url = request.json['repo_url']
    repo_path = clone_repository(repo_url)
    upload_to_s3(repo_path)
    return {'status': 'success'}

if __name__ == "__main__":
    app.run(debug=True)
