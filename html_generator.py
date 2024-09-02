# html_generator.py

class HTMLGenerator:
    """Generates an HTML report from parsed hashcat data."""

    def __init__(self, title: str):
        self.title = title

    def generate_html_content(self, data, max_username_length: int) -> str:
        """Generates the HTML content as a string."""
        html_content = [
            "<html><head><title>{}</title>".format(self.title),
            "<style>",
            "body { font-family: Arial, sans-serif; margin: 20px; }",
            "table { width: 100%; border-collapse: collapse; margin-top: 20px; }",
            "th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }",
            "th { background-color: #4682B4; color: white; }",
            "h1 { text-align: center; }",
            ".highlight { background-color: #ffcccb; }",
            "</style>",
            "</head><body>",
            "<h1>{}</h1>".format(self.title),
            "<table>",
            "<tr><th>No</th><th>Username</th><th>Password</th></tr>"
        ]

        for idx, (username, password) in enumerate(data, start=1):
            if 'admin' in username.lower() or 'admin' in password.lower():
                html_content.append(
                    "<tr class='highlight'><td>{}</td><td>{}</td><td>{}</td></tr>".format(idx, username, password)
                )
            else:
                html_content.append(
                    "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(idx, username, password)
                )
        html_content.extend(["</table>", "</body></html>"])

        return "\n".join(html_content)

    def save_html(self, output_file: str, data, max_username_length: int):
        """Saves the generated HTML content to a file."""
        html_content = self.generate_html_content(data, max_username_length)
        with open(output_file, 'w') as file:
            file.write(html_content)
