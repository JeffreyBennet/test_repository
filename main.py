import flask
from services.clone_service import clone_repository
from services.upload_service import upload_to_s3

app = flask.Flask(__name__)

@app.route("/clone", methods=["POST"])
def clone_repo():
    request_data = flask.request.get_json()
    repo_url = request_data['repo_url']
    local_path = clone_repository(repo_url)
    return {"local_path": local_path}, 200

@app.route("/upload", methods=["POST"])
def upload_repo():
    request_data = flask.request.get_json()
    local_path = request_data['local_path']
    bucket_name = request_data['bucket_name']
    upload_to_s3(local_path, bucket_name)
    return {"status": "successfully uploaded"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

