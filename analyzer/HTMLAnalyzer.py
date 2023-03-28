import json
from collections import defaultdict

class HTMLAnalyzer:
    def __init__(self, json_data):
        self.json_data = json_data['html_structure']
        self.css_rules = json_data['css_rules']
        self.typography = set()
        self.color_schemes = defaultdict(set)
        self.layout_schemes = set()
        self.design_preferences = set()

    def get_critical_design_prefs(self):
        grouped_rules = defaultdict(lambda: defaultdict(list))

        for rule in self.css_rules:
            selector = rule['selector']
            for property, value in rule['rules'].items():
                grouped_rules[property][selector].append(value)

        critical_prefs = {}
        for property, selectors in grouped_rules.items():
            critical_prefs[property] = []
            for selector, values in selectors.items():
                critical_prefs[property].append({
                    'element': selector,
                    'values': values
                })

        return critical_prefs

    def process_json(self, json_obj):
        if json_obj.get('tag') is not None:
            attrs = json_obj.get('attrs', {})
            if 'class' in attrs:
                class_list = attrs['class']
                for class_name in class_list:
                    if 'font-' in class_name:
                        self.typography.add(class_name)
                    elif 'color-' in class_name:
                        color_type = class_name.split('-')[1]
                        self.color_schemes[color_type].add(class_name)
                    elif 'layout-' in class_name:
                        self.layout_schemes.add(class_name)
                    elif 'design-' in class_name:
                        self.design_preferences.add(class_name)

            for child in json_obj.get('children', []):
                self.process_json(child)

    def process_css_rules(self):
        for rule in self.css_rules:
            selector = rule['selector']
            if any(class_name in selector for class_name in self.typography):
                for name, value in rule['rules'].items():
                    if name == 'font-family':
                        self.typography.add(selector)
            # Add similar code blocks for processing color, layout, and design preferences
            # based on your specific requirements and the properties you want to extract

    def apply_changes(self, changes):
        for change in changes:
            selector = change['selector']
            property = change['property']
            new_value = change['new_value']

            # Find the CSS rule to update
            rule_to_update = None
            for rule in self.css_rules:
                if rule['selector'] == selector:
                    rule_to_update = rule
                    break

            # Update the CSS rule
            if rule_to_update:
                rule_to_update['rules'][property] = new_value
            else:
                # If the rule is not found, add a new rule
                self.css_rules.append({
                    'selector': selector,
                    'rules': {property: new_value}
                })

    def analyze(self):
        self.process_json(self.json_data)
        self.process_css_rules()
        # return self.get_critical_design_prefs()
        return {
            # 'typography': list(self.typography),
            # 'color_schemes': dict(self.color_schemes),
            # 'layout_schemes': list(self.layout_schemes),
            'design_preferences': self.get_critical_design_prefs()
        }

    def apply_css_rules(self, new_css_rules):
        # Update the css_rules attribute with the new rules
        self.css_rules = new_css_rules

        # Create a dictionary to store all the styles
        styles = {}

        # Iterate through the css_rules and create a dictionary of styles
        for rule in self.css_rules:
            selector = rule['selector']
            for property, value in rule['rules'].items():
                if selector not in styles:
                    styles[selector] = {}
                styles[selector][property] = value

        # Apply the styles to the html_structure
        self.apply_styles_to_json(self.json_data, styles)

        return self.json_data

    def apply_styles_to_json(self, json_obj, styles):
        if json_obj.get('tag') is not None:
            tag = json_obj.get('tag')
            attrs = json_obj.get('attrs', {})

            # Apply styles based on the tag name
            if tag in styles:
                if 'attrs' not in json_obj:
                    json_obj['attrs'] = {}
                if 'style' not in json_obj['attrs']:
                    json_obj['attrs']['style'] = {}
                for property, value in styles[tag].items():
                    json_obj['attrs']['style'][property] = value

            # Apply styles based on the classes
            if 'class' in attrs:
                class_list = attrs['class']
                for class_name in class_list:
                    selector = f".{class_name}"
                    if selector in styles:
                        if 'style' not in json_obj['attrs']:
                            json_obj['attrs']['style'] = {}
                        for property, value in styles[selector].items():
                            json_obj['attrs']['style'][property] = value

            for child in json_obj.get('children', []):
                self.apply_styles_to_json(child, styles)