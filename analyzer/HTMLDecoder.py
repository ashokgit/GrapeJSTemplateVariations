import json

class HTMLDecoder:
    def process_json(self, json_obj):
        if 'tag' in json_obj:
            attrs = ''.join(f' {key}="{value}"' for key, value in json_obj.get('attrs', {}).items())
            html_elem = f'<{json_obj["tag"]}{attrs}>'
            for child in json_obj.get('children', []):
                html_elem += self.process_json(child)
            html_elem += f'</{json_obj["tag"]}>'
        else:
            html_elem = json_obj.get('text', '')
        return html_elem

    def decode(self, json_obj):
        return self.process_json(json_obj)