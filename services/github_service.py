import git

def clone_repo_from_github(repo_url, local_path):
    try:
        git.Repo.clone_from(repo_url, local_path)
        print(f'Repository cloned to {local_path}')
    except Exception as e:
        print(f'An error occurred while cloning the repository: {e}')