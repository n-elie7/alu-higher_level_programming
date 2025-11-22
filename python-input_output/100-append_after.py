#!/usr/bin/python3
"""inserts line of text after each line containing specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string."""
    new_content = ""

    # Read file content
    with open(filename, "r") as f:
        for line in f:
            new_content += line
            if search_string in line:
                new_content += new_string

    # Rewrite the file with updated content
    with open(filename, "w") as f:
        f.write(new_content)
