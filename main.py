# main.py
from git_utils import get_git_diff
from llm import generate_commit_message
from prompt import PROMPT_TEMPLATE


diff = get_git_diff()

if not diff:
    print("No staged changes found.")
    exit()

message = generate_commit_message(
    diff,
    PROMPT_TEMPLATE
)

print("\nSuggested Commit Message:\n")
print(message)