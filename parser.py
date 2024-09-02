# parser.py

def parse_potfile(potfile_path: str):
    """Parses the potfile and returns a list of (username, password) tuples and the max username length."""
    parsed_data = []
    max_username_length = 0

    with open(potfile_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) >= 3:
                username = parts[0]
                password = parts[-1]
                parsed_data.append((username, password))
                username_length = len(username) * 3
                max_username_length = max(max_username_length, username_length)
    max_page_width = 210 - 40
    max_username_length = min(max_username_length, max_page_width - 95)
    return parsed_data, max_username_length
