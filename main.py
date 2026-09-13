import os
import random
import subprocess
from datetime import datetime, timedelta

def get_positive_int(prompt, default=20):
    while True:
        try:
            user_input = input(f"{prompt} (default {default}): ")
            if not user_input.strip():
                return default
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_repo_path(prompt, default="."):
    while True:
        user_input = input(f"{prompt} (default current directory): ")
        if not user_input.strip():
            return default
        if os.path.isdir(user_input):
            return user_input
        else:
            print("Directory does not exist. Please enter a valid path.")

def get_filename(prompt, default="data.txt"):
    user_input = input(f"{prompt} (default {default}): ")
    if not user_input.strip():
        return default
    return user_input

def random_date_in_last_year():
    today = datetime.now()
    start_date = today - timedelta(days=365)
    random_days = random.randint(0, 364)
    random_seconds = random.randint(0, 23*3600 + 3599)
    commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return commit_date

def make_commit(date, repo_path, filename, message="graph-greener!"):
    filepath = os.path.join(repo_path, filename)
    with open(filepath, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")
    subprocess.run(["git", "add", filename], cwd=repo_path)
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env)

def main():
    print("="*60)
    print("Welcome to graph-greener - GitHub Contribution Graph Commit Generator")
    print("="*60)
    print("This tool will help you fill your GitHub contribution graph with custom commits.\n")

    num_commits = get_positive_int("How many commits do you want to make", 20)
    repo_path = get_repo_path("Enter the path to your local git repository", ".")
    filename = get_filename("Enter the filename to modify for commits", "data.txt")

    print(f"\nMaking {num_commits} commits in repo: {repo_path}\nModifying file: {filename}\n")

    for i in range(num_commits):
        commit_date = random_date_in_last_year()
        print(f"[{i+1}/{num_commits}] Committing at {commit_date.strftime('%Y-%m-%d %H:%M:%S')}")
        make_commit(commit_date, repo_path, filename)

    print("\nPushing commits to your remote repository...")
    subprocess.run(["git", "push"], cwd=repo_path)
    print("✅ All done! Check your GitHub contribution graph in a few minutes.\n")
    print("Tip: Use a dedicated repository for best results. Happy coding!")

if __name__ == "__main__":
    main()Commit at 2026-01-24T09:19:11.530071
Commit at 2026-01-14T18:55:48.254409
Commit at 2026-07-21T10:10:30.009073
Commit at 2026-05-31T14:02:00.685769
Commit at 2026-01-04T04:22:49.363570
Commit at 2026-03-21T12:12:34.909865
Commit at 2026-06-29T22:59:33.593429
Commit at 2026-01-24T02:34:52.227106
Commit at 2026-07-11T04:46:30.825335
Commit at 2025-11-28T18:04:16.453007
Commit at 2026-09-24T19:02:21.097204
Commit at 2026-05-11T23:40:52.720225
Commit at 2026-01-10T03:45:15.403645
Commit at 2026-01-19T21:18:19.046543
Commit at 2026-06-03T19:42:22.700497
Commit at 2026-02-12T18:07:31.379455
Commit at 2026-08-07T22:56:26.002334
Commit at 2026-01-12T19:01:52.639118
Commit at 2026-03-24T22:26:04.262691
Commit at 2026-10-14T15:52:41.936232
Commit at 2026-05-02T06:17:38.601487
Commit at 2025-12-08T09:20:50.249429
Commit at 2026-06-09T15:27:13.902971
Commit at 2026-08-25T11:45:35.593854
Commit at 2026-02-11T01:17:09.254008
Commit at 2026-08-31T05:35:02.878229
Commit at 2025-12-16T22:03:05.467933
Commit at 2026-05-24T06:48:36.161751
Commit at 2025-12-15T19:25:15.844970
Commit at 2026-02-26T11:42:31.514366
Commit at 2025-11-20T20:13:41.185529
Commit at 2026-05-10T12:34:50.835919
Commit at 2025-12-15T08:18:01.471945
Commit at 2026-09-14T00:18:40.144295
