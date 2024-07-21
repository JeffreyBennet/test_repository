import git

def clone_repository(repo_url):
    local_path = "/tmp/repo"
    git.Repo.clone_from(repo_url, local_path)
    return local_path