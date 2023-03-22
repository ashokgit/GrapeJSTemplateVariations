import openai

class OpenAIColorFetcher:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_prompt(self, style_for):
        font_schemes = (
            "Arial, Helvetica, sans-serif; "
            "Arial Black, Gadget, sans-serif; "
            "Brush Script MT, sans-serif; "
            "Comic Sans MS, cursive, sans-serif; "
            "Courier New, Courier, monospace; "
            "Georgia, serif; "
            "Helvetica, sans-serif; "
            "Impact, Charcoal, sans-serif; "
            "Lucida Sans Unicode, Lucida Grande, sans-serif; "
            "Tahoma, Geneva, sans-serif; "
            "Times New Roman, Times, serif; "
            "Trebuchet MS, Helvetica, sans-serif; "
            "Verdana, Geneva, sans-serif"
        )

        font_styles = "normal, italic, bold, bold italic"

        message = (
            f"Create a color palette for a {style_for} that includes a color scheme for a newsletter template. "
            f"These color palettes will be used for restaurant menu designs. Please take into consideration advanced color theory, "
            f"and what other menus of that style use. Also, suggest an appropriate font family from the following list: {font_schemes} "
            f"and a font style from the following options: {font_styles}. "
            f"Generate background, text, primary, secondary, and accent color schemes. "
            f"Also provide an explanation for the color and font choice"
            f"Response strictly in the following format: {{ 'font': '', 'font_style': '', 'background': '#', 'text': '#', 'primary': '#', 'secondary': '#', 'accent': '#', 'reason':'' }}"
        )

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a UI/UX Expert. You have a deep understanding of advanced color theory."},
                {"role": "user", "content": message},
            ],
            max_tokens=350,
            n=1,
            temperature=0.7,
        )

        return response.choices[0].message['content'].strip()