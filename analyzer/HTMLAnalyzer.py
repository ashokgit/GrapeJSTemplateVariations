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

    def analyze(self):
        self.process_json(self.json_data)
        self.process_css_rules()
        return {
            'typography': list(self.typography),
            'color_schemes': dict(self.color_schemes),
            'layout_schemes': list(self.layout_schemes),
            'design_preferences': list(self.design_preferences)
        }