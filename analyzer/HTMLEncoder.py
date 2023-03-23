from bs4 import BeautifulSoup
import json
import cssutils

class HTMLEncoder:
    def process_node(self, node):
        if node.name is not None:
            attrs = {k: v for k, v in node.attrs.items() if v}
            children = [self.process_node(child) for child in node.children]

            result = {
                'tag': node.name,
                'attrs': attrs if attrs else None,
                'children': children if children else None,
                'text': None
            }
        else:
            result = {
                'text': str(node.string).strip() if node.string else None
            }

        # Remove keys with null values
        result = {k: v for k, v in result.items() if v is not None}
        return result

    def encode(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        json_structure = self.process_node(soup.body)

        # Extract CSS rules from the HTML
        css_rules = []
        for style_tag in soup.find_all('style'):
            stylesheet = cssutils.parseString(style_tag.string)
            for rule in stylesheet:
                if isinstance(rule, cssutils.css.CSSStyleRule):
                    css_rules.append({
                        'selector': rule.selectorText,
                        'rules': {p.name: p.value for p in rule.style}
                    })

        return {
            'html_structure': json_structure,
            'css_rules': css_rules
        }