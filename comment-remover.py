import re

def remove_comments(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove single-line comments
    content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)

    # Remove multi-line comments enclosed in single quotes
    content = re.sub(r"'''.*?'''.*?", '', content, flags=re.DOTALL)

    # Remove multi-line comments enclosed in double quotes
    content = re.sub(r'""".*?""".*?', '', content, flags=re.DOTALL)

    # Write the modified content to the file
    with open(filepath, 'w') as f:
        f.write(content)

    print(f"Comments removed from {filepath}")

# Example usage:
remove_comments('activation.py')
