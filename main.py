
import os
import random
import subprocess
from datetime import datetime, timedelta
from pathlib import Path


def get_positive_int(prompt, default=20):
    while True:
        user_input = input(f"{prompt} (default {default}): ").strip()

        if not user_input:
            return default

        try:
            value = int(user_input)
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a valid integer.")


def get_repo_path(prompt, default="."):
    while True:
        user_input = input(
            f"{prompt} (default current directory): "
        ).strip()

        path = Path(user_input or default).expanduser().resolve()

        if not path.is_dir():
            print("Directory does not exist.")
            continue

        try:
            subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                cwd=path,
                check=True,
                capture_output=True,
                text=True,
            )
            return path
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Please select a valid Git repository.")


def get_filename(prompt, default="data.txt"):
    while True:
        name = input(f"{prompt} (default {default}): ").strip() or default
        path = Path(name)

        if path.is_absolute() or ".." in path.parts:
            print("Use a relative filename inside the repository.")
            continue

        return path


def random_date_in_previous_month():
    today = datetime.now().astimezone()

    # First day of the current month
    first_this_month = today.replace(
        day=1, hour=0, minute=0, second=0, microsecond=0
    )

    # Last moment of the previous month
    end_previous_month = first_this_month - timedelta(seconds=1)

    # First moment of the previous month
    start_previous_month = end_previous_month.replace(
        day=1, hour=0, minute=0, second=0, microsecond=0
    )

    total_seconds = int(
        (end_previous_month - start_previous_month).total_seconds()
    )

    return start_previous_month + timedelta(
        seconds=random.randint(0, total_seconds)
    )


def make_commit(date, repo_path, filename, message):
    filepath = repo_path / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with filepath.open("a", encoding="utf-8") as file:
        file.write(f"Test record: {date.isoformat()}\n")

    subprocess.run(
        ["git", "add", "--", filename.as_posix()],
        cwd=repo_path,
        check=True,
    )

    # Set the Git author and committer dates for testing.
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S%z")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    subprocess.run(
        ["git", "commit", "-m", message],
        cwd=repo_path,
        env=env,
        check=True,
    )


def main():
    print("=" * 60)
    print("Previous-Month Git History Test")
    print("=" * 60)

    try:
        num_commits = get_positive_int("Number of commits", 20)
        repo_path = get_repo_path("Git repository path", ".")
        filename = get_filename("Filename to modify", "data.txt")
        message = input("Commit message: ").strip() or "Test Git history"

        print(
            f"\nCreating {num_commits} commits with dates "
            "randomly selected from the previous month.\n"
        )

        for i in range(num_commits):
            commit_date = random_date_in_previous_month()
            print(
                f"[{i + 1}/{num_commits}] "
                f"{commit_date.strftime('%Y-%m-%d %H:%M:%S %z')}"
            )
            make_commit(commit_date, repo_path, filename, message)

        print("\nAll commits created successfully.")

        push = input("Push to remote repository? (y/n): ").strip().lower()
        if push == "y":
            subprocess.run(["git", "push"], cwd=repo_path, check=True)
            print("Push completed successfully.")

    except subprocess.CalledProcessError as error:
        print(f"\nGit command failed: {error}")
    except (OSError, ValueError) as error:
        print(f"\nError: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


if __name__ == "__main__":
    main()
