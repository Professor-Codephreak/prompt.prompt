# Script to parse and display rules from rules.prompt

import re
import yaml

def extract_yaml_metadata(content):
    """Extract YAML metadata from the prompt file."""
    yaml_pattern = r"^---\n(.*?)\n---\n"
    match = re.search(yaml_pattern, content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        try:
            return yaml.safe_load(yaml_content)
        except Exception as e:
            print(f"Error parsing YAML: {e}")
    return {}

def extract_language_rules(content):
    """Extract the LANGUAGE_RULES list from the prompt file."""
    # Find the start of the LANGUAGE_RULES list
    start_pattern = r"LANGUAGE_RULES = \["
    start_match = re.search(start_pattern, content)
    if not start_match:
        return []
    
    start_idx = start_match.start()
    
    # Find the end of the list by counting brackets
    bracket_count = 0
    end_idx = start_idx
    
    for i in range(start_idx, len(content)):
        if content[i] == '[':
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_idx = i + 1
                break
    
    rules_str = content[start_idx:end_idx]
    
    # Convert to Python code and evaluate
    try:
        # Replace the variable name with a list literal
        rules_str = rules_str.replace("LANGUAGE_RULES = ", "")
        # Use eval to convert the string to a Python list
        rules = eval(rules_str)
        return rules
    except Exception as e:
        print(f"Error parsing rules: {e}")
        return []

class RuleViewer:
    def __init__(self, rules_data):
        self.rules = rules_data
        self.categories = self._get_categories()

    def _get_categories(self):
        cats = []
        for rule in self.rules:
            if rule['category'] not in cats:
                cats.append(rule['category'])
        return cats

    def display_rules(self):
        print("\n# --- prompt Language Rules v one point one point zero Specification ---")
        for category in self.categories:
            print(f"\n## {category}")
            category_rules = [rule['description'] for rule in self.rules if rule['category'] == category]
            for description in category_rules:
                print(f"  - {description}")
        print("\n# --- End Rules Specification ---")

def main():
    print("[SCRIPT START] Displaying prompt language conceptual rules specification")
    
    # Read the rules.prompt file
    try:
        with open('rules.prompt', 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Extract metadata and rules
    metadata = extract_yaml_metadata(content)
    rules = extract_language_rules(content)
    
    # Display metadata
    print("\n# --- Metadata ---")
    for key, value in metadata.items():
        print(f"  - {key}: {value}")
    
    # Display rules
    if rules:
        viewer = RuleViewer(rules_data=rules)
        viewer.display_rules()
    else:
        print("No rules found in the file.")
    
    print("[SCRIPT END]")

if __name__ == "__main__":
    main()
