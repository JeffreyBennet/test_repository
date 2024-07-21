import os
from git import Repo

def clone_repository(repo_url):
    repo_path = "/tmp/repo"
    if os.path.exists(repo_path):
        os.system(f'rm -rf {repo_path}')
    Repo.clone_from(repo_url, repo_path)
    return repo_path