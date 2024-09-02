#! /usr/bin/env python3
import argparse
import os
from html_generator import HTMLGenerator
from parser import parse_potfile

def generate_html_report(data, max_username_length: int, title: str, output_html: str):
    """Generates and saves the HTML report using the HTMLGenerator."""
    html_generator = HTMLGenerator(title)
    html_generator.save_html(output_html, data, max_username_length)

def main():
    """Main function to parse arguments and generate the HTML report."""
    parser = argparse.ArgumentParser(description='Convert a potfile to a formatted HTML report.')
    parser.add_argument('-t', '--title', type=str, default="Cracked Passwords", help='Title for the HTML report')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input potfile')
    parser.add_argument('-o', '--output', type=str, default="output.html", help='Path to the output HTML file')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Input file '{args.input}' does not exist.")
        return

    parsed_data, max_username_length = parse_potfile(args.input)
    if parsed_data:
        generate_html_report(parsed_data, max_username_length, args.title, args.output)
        print(f"HTML file generated: {args.output}")
    else:
        print("No valid data found in the potfile.")

if __name__ == "__main__":
    main()
