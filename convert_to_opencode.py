#!/usr/bin/env python3
"""
Script to convert agency-agents format to OpenCode agent format.
Usage:
  python3 convert_to_opencode.py [--input INPUT_DIR] [--output OUTPUT_DIR]

Default:
  INPUT_DIR: Current directory (agency-agents)
  OUTPUT_DIR: ~/.config/opencode/agents/
"""

import os
import re
import argparse
import shutil


def clean_description(desc):
    """Clean up description by replacing newlines and extra spaces."""
    if not desc:
        return ""
    # Replace literal \n with space
    desc = desc.replace("\\n", " ")
    # Collapse multiple spaces
    desc = re.sub(r' +', ' ', desc)
    return desc.strip()


def convert_agent_file(input_path, output_path):
    """Convert a single agent file to OpenCode format."""
    with open(input_path, 'r') as f:
        content = f.read()
    
    # Extract frontmatter
    description = None
    color = None
    
    # Match YAML frontmatter
    yaml_match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        
        # Extract description (handle multi-line, but stop at new line or end of string)
        desc_match = re.search(r'description:\s*(.*?)(?=\n|$)', yaml_content, re.DOTALL)
        if desc_match:
            description = clean_description(desc_match.group(1))
        
        # Extract color
        color_match = re.search(r'color:\s*(.*)', yaml_content)
        if color_match:
            color = color_match.group(1).strip()
    
    # Default description if not found
    if not description:
        filename = os.path.basename(input_path)
        description = f"Agent for {filename[:-3]}"
    
    # Build new frontmatter
    new_frontmatter = f"""---
description: {description}
"""
    if color:
        new_frontmatter += f"color: {color}\n"
    new_frontmatter += """mode: subagent
permission:
  edit: allow
  bash: allow
---

"""
    
    # Remove old frontmatter (including all lines between --- markers)
    # Use a more robust pattern that handles newlines in values
    new_content = re.sub(r'---\n(?:[^\n]*\n)*?---', '', content, flags=re.DOTALL)
    
    # Remove any remaining frontmatter-like lines at the start
    new_content = re.sub(r'^(name:.*\n)?', '', new_content)
    new_content = re.sub(r'^(description:.*\n)?', '', new_content)
    new_content = re.sub(r'^(color:.*\n)?', '', new_content)
    
    # Remove any lines that look like frontmatter (name:, description:, color:) at the start
    new_content = re.sub(r'^(name:.*\n|description:.*\n|color:.*\n)+', '', new_content)
    
    # Also remove standalone frontmatter lines anywhere in the content
    new_content = re.sub(r'^name:.*\n', '', new_content)
    new_content = re.sub(r'^description:.*\n', '', new_content)
    new_content = re.sub(r'^color:.*\n', '', new_content)
    
    # Remove leading/trailing whitespace
    new_content = new_content.strip()
    
    # Combine
    final_content = new_frontmatter + new_content
    
    # Write to output
    with open(output_path, 'w') as f:
        f.write(final_content)


def main():
    parser = argparse.ArgumentParser(description='Convert agency-agents to OpenCode format')
    parser.add_argument('--input', default='.', help='Input directory (default: current directory)')
    parser.add_argument('--output', default=os.path.expanduser('~/.config/opencode/agents/'), 
                        help='Output directory (default: ~/.config/opencode/agents/)')
    parser.add_argument('--clean', action='store_true', help='Clean output directory before conversion')
    args = parser.parse_args()
    
    # Ensure output directory exists
    os.makedirs(args.output, exist_ok=True)
    
    # Clean output directory if requested
    if args.clean:
        for item in os.listdir(args.output):
            item_path = os.path.join(args.output, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    
    # Find all markdown files in input directory (recursively)
    converted = 0
    for root, _, files in os.walk(args.input):
        for file in files:
            if file.endswith('.md') and file not in ['README.md', 'CONTRIBUTING.md', 'LICENSE']:
                input_path = os.path.join(root, file)
                
                # Flatten structure: use just the filename
                output_path = os.path.join(args.output, file)
                
                convert_agent_file(input_path, output_path)
                converted += 1
                print(f"Converted: {file}")
    
    print(f"\nDone! Converted {converted} agent files to {args.output}")


if __name__ == '__main__':
    main()
