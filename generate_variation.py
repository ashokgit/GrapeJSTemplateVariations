from bs4 import BeautifulSoup
from lib.color_replacer import ColorReplacer
from lib.openai_color_fetcher import OpenAIColorFetcher
from dotenv import load_dotenv
import os
import re
import json
import argparse

# Function to parse colors from the response
def parse_colors_from_response(color_response):
   # Replace single quotes with double quotes to make the string JSON-compatible
    color_string = color_response.replace("'", "\"")

    # Load the JSON string into a dictionary
    colors = json.loads(color_string)

    print(f"Parsed colors: {colors}")  # Add this print statement

    return colors

def main(style_for):
    input_file = './data/basetemplate.html'
    output_directory = './data/outputs/'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = f'{output_directory}{style_for.replace(" ", "_")}.html'

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    color_fetcher = OpenAIColorFetcher(api_key)
    color_response = color_fetcher.get_prompt(style_for)
    print("---- Style Response --------")
    print(color_response)
    colors = parse_colors_from_response(color_response)

    with open(input_file, 'r') as file:
        html = file.read()

    color_replacer = ColorReplacer(html)
    color_replacer.replace_colors(colors)
    color_replacer.replace_typography(colors['font'], colors['font_style'])
    updated_html = color_replacer.get_updated_html()

    with open(output_file, 'w') as file:
        file.write(updated_html)

    print(f'Updated HTML saved to {output_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--style_for', type=str, required=True, help='Who is this style for? for example: a traditional Mexican Resturant')
    args = parser.parse_args()
    main(args.style_for)