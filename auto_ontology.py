#!/usr/bin/env python3
import os
import re
from datetime import datetime

VAULT_DIR = "/home/khyha/projects/Sunny"
IGNORE_DIRS = {".obsidian", ".git", ".agent", "scripts"}

MOC_CONTENT_TEMPLATE = """---
type: moc
tags: [moc, {domain}]
---
# {title} Map of Content

"""

def add_frontmatter_if_missing(filepath, rel_dir):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it already has frontmatter or properties, skip or update (simplified to skip if frontmatter exists)
    if content.startswith('---'):
        return False
    
    # Generate tags based on directory path
    parts = [p for p in rel_dir.split(os.sep) if p and p != '.']
    if not parts:
        domain = "root"
    else:
        domain = parts[0].lower().replace(" ", "-")
        
    frontmatter = f"""---
type: concept
tags:
  - {domain}
created: {datetime.now().strftime("%Y-%m-%d")}
summary: ""
---
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    return True

def generate_moc(rel_dir, files):
    parts = [p for p in rel_dir.split(os.sep) if p and p != '.']
    if not parts:
        return
        
    folder_name = parts[-1]
    moc_filename = f"00_{folder_name}_MOC.md"
    moc_path = os.path.join(VAULT_DIR, rel_dir, moc_filename)
    
    if os.path.exists(moc_path):
        return
        
    domain_tag = parts[0].lower().replace(" ", "-")
    content = MOC_CONTENT_TEMPLATE.format(domain=domain_tag, title=folder_name)
    
    for file in files:
        if file.endswith('.md') and file != moc_filename:
            content += f"- [[{file.replace('.md', '')}]]\n"
            
    with open(moc_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Created MOC: {moc_path}")

def process_vault():
    added_count = 0
    for root, dirs, files in os.walk(VAULT_DIR):
        # Exclude hidden and ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
        
        md_files = [f for f in files if f.endswith('.md')]
        rel_dir = os.path.relpath(root, VAULT_DIR)
        
        for file in md_files:
            filepath = os.path.join(root, file)
            # Skip MOC files
            if file.endswith('_MOC.md'):
                continue
                
            if add_frontmatter_if_missing(filepath, rel_dir):
                added_count += 1
                
        if md_files:
            generate_moc(rel_dir, md_files)
            
    print(f"Added metadata to {added_count} files.")

if __name__ == "__main__":
    print(f"Starting Agentic RAG Ontology Map restructuring for vault: {VAULT_DIR}")
    process_vault()
    print("Process complete.")
