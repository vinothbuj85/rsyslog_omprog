#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

GIT_REPO_PATH = "/path/to/your/repo"
TEXT_FILE = os.path.join(GIT_REPO_PATH, "file.txt")

def run_git_command(commands, cwd):
    try:
        result = subprocess.run(commands, cwd=cwd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e.stderr}")
        return None

def git_add_commit_push():
    run_git_command(["git", "add", "."], cwd=GIT_REPO_PATH)
    commit_msg = f"Automated commit by rsyslog at {datetime.now().isoformat()}"
    run_git_command(["git", "commit", "-m", commit_msg], cwd=GIT_REPO_PATH)
    run_git_command(["git", "push"], cwd=GIT_REPO_PATH)

def file_has_changes():
    result = run_git_command(["git", "status", "--porcelain"], cwd=GIT_REPO_PATH)
    return bool(result)

def main():
    if file_has_changes():
        git_add_commit_push()

if __name__ == "__main__":
    main() 
