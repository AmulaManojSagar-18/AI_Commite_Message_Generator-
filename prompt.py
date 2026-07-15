# prompt.py
PROMPT_TEMPLATE = """
You are a senior software engineer.

Analyze the git diff and generate a conventional commit message.

Rules:
- Use feat, fix, docs, test, refactor, chore
- Maximum 70 characters
- Return only the commit message
- Do not include explanations

Git Diff:

{diff}
"""
