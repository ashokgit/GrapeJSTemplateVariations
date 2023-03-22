from bs4 import BeautifulSoup
import re

class ColorReplacer:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def replace_body_background_color(self, color):
        body = self.soup.body
        body['style'] = f"box-sizing: border-box; margin: 0; background-color: {color};"

    def replace_typography(self, new_font_family, new_font_style=None):
        # Replace the font family in the 'style' attributes
        elements = self.soup.select('[style*="font-family"]')
        for element in elements:
            old_style = element['style']
            new_style = re.sub(r'font-family: [^;]+', f'font-family: {new_font_family}', old_style)
            element['style'] = new_style

        # Replace the font style if provided
        if new_font_style is not None:
            elements = self.soup.select('[style*="font-style"]')
            for element in elements:
                old_style = element['style']
                new_style = re.sub(r'font-style: [^;]+', f'font-style: {new_font_style}', old_style)
                element['style'] = new_style

    def replace_element_color(self, selector, attribute, color):
        elements = self.soup.select(selector)
        for element in elements:
            if attribute in element.attrs:
                element[attribute] = element[attribute].replace(element[attribute], color)

    def replace_colors(self, colors):
        self.replace_body_background_color(colors['background'])
        self.replace_element_color('td.card-cell', 'bgcolor', colors['background'])
        self.replace_element_color('td.list-item-cell', 'bgcolor', colors['background'])

        self.replace_element_color('.top-cell', 'style', f"color: {colors['text']};")
        self.replace_element_color('.card-content', 'style', f"color: {colors['text']};")

        self.replace_element_color('.card-title', 'style', f"color: {colors['primary']};")

        self.replace_element_color('.button', 'style', f"background-color: {colors['secondary']};")

        self.replace_element_color('.link', 'style', f"color: {colors['accent']};")

    def get_updated_html(self):
        return str(self.soup)