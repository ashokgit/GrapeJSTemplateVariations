Generate Grape.js Template Variations using GPT-4
==================

This script generates variations of a grape.js newsletter template HTML file by using OpenAI's GPT-4 API to fetch color and typography suggestions based on a provided style.

Installation
------------

1.  Clone this repository.
2.  Install the required packages using `pip install -r requirements.txt`.
3.  Rename `.env.example` to `.env` and replace the placeholder API key with your own.

Usage
-----

To use the script, run the following command:

pythonCopy code

`python generate_variation.py --style_for "my restaurant style"`

This will generate a new HTML file with the specified style applied. The output file will be saved to the `./data` directory with a filename based on the provided `--style_for` argument.

For example, if you run `python generate_variation.py --style_for "modern fusion restaurant"`, the output file will be saved to `./data/modern_fusion_restaurant.html`.

Data
----

This script uses a base HTML template file located in the `./data` directory. You can modify this file to change the structure and content of the output HTML files.

The script also uses OpenAI's GPT-4 API to fetch color and typography suggestions. You will need to provide your own API key in the `.env` file.

Features
--------

- Change Color Scheme
- Change Typography
- Prompt Completion Logging for RLHF and Finetuning

TODO
----

- Change Layout Structure
- Change Design
- Implement a Tailwind CSS based template
- Build a HTML Interrogator to navigate into the template to better control the prompt and suggestions
- Prompt Chaining, Langchain Implementation (* if necessary)
- and much more, stay tuned

License
-------

This project is licensed under the MIT License. Feel free to modify and use it however you like!
