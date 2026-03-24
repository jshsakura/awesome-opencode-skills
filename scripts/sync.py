import os
import sys
import shutil
import subprocess
import re
from pathlib import Path

# Try to import tomllib (Python 3.11+) or tomli fallback
try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        print("Warning: tomllib not found. Falling back to basic regex parsing.")
        tomllib = None

REPO_URL = "https://github.com/VoltAgent/awesome-codex-subagents.git"
TEMP_DIR = Path(".temp_sync")
SKILLS_DIR = Path("skills")

def parse_toml_fallback(content):
    """Fallback manual parser for basic TOML extraction if tomllib is missing"""
    data = {}
    
    # Extract simple string keys
    for key in ['name', 'description', 'model', 'model_reasoning_effort', 'sandbox_mode']:
        match = re.search(rf'{key}\s*=\s*(["\'])(.*?)\1', content)
        if match:
            data[key] = match.group(2)
            
    # Extract developer_instructions or instructions.text
    # using a simple approach since toml multiline strings can be tricky
    dev_inst_match = re.search(r'developer_instructions\s*=\s*"""(.*?)"""', content, re.DOTALL)
    if dev_inst_match:
        data['developer_instructions'] = dev_inst_match.group(1).strip()
    else:
        # Check for [instructions] block
        inst_text_match = re.search(r'\[instructions\]\s*text\s*=\s*"""(.*?)"""', content, re.DOTALL)
        if inst_text_match:
            data['developer_instructions'] = inst_text_match.group(1).strip()
            
    return data

def sync_skills():
    print("Syncing from upstream: awesome-codex-subagents...")
    
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)
        
    subprocess.run(["git", "clone", "--depth", "1", REPO_URL, str(TEMP_DIR)], check=True)
    
    categories_dir = TEMP_DIR / "categories"
    if not categories_dir.exists():
        print("Error: Could not find 'categories' directory in upstream repo.")
        sys.exit(1)
        
    if SKILLS_DIR.exists():
        print("Cleaning up old skills directory...")
        shutil.rmtree(SKILLS_DIR, ignore_errors=True)
        
    os.makedirs(SKILLS_DIR, exist_ok=True)
    
    count = 0
    for root, dirs, files in os.walk(categories_dir):
        for file in files:
            if file.endswith('.toml'):
                toml_path = Path(root) / file
                
                with open(toml_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse toml
                skill_data = {}
                if tomllib:
                    try:
                        data = tomllib.loads(content)
                        # Normalize parsed data
                        skill_data['name'] = data.get('name', '').replace(' ', '-').lower()
                        skill_data['description'] = data.get('description', '')
                        skill_data['model'] = data.get('model', 'gpt-4o')
                        skill_data['model_reasoning_effort'] = data.get('model_reasoning_effort', '')
                        skill_data['sandbox_mode'] = data.get('sandbox_mode', '')
                        
                        inst = data.get('developer_instructions', '')
                        if not inst and 'instructions' in data and 'text' in data['instructions']:
                            inst = data['instructions']['text']
                        skill_data['instructions'] = inst.strip()
                    except Exception as e:
                        print(f"Failed to parse {file} using tomllib. Error: {e}")
                        continue
                else:
                    data = parse_toml_fallback(content)
                    skill_data['name'] = data.get('name', '').replace(' ', '-').lower()
                    skill_data['description'] = data.get('description', '')
                    skill_data['model'] = data.get('model', 'gpt-4o')
                    skill_data['model_reasoning_effort'] = data.get('model_reasoning_effort', '')
                    skill_data['sandbox_mode'] = data.get('sandbox_mode', '')
                    skill_data['instructions'] = data.get('developer_instructions', '')

                if not skill_data.get('name'):
                    continue
                    
                # Create OpenCode Skill format
                skill_dir = SKILLS_DIR / skill_data['name']
                os.makedirs(skill_dir, exist_ok=True)
                
                skill_md_path = skill_dir / "SKILL.md"
                with open(skill_md_path, 'w', encoding='utf-8') as f:
                    f.write("---\n")
                    f.write(f"name: {skill_data['name']}\n")
                    
                    # Sanitize description (remove newlines formatting)
                    desc = skill_data['description'].replace('\n', ' ').strip()
                    f.write(f"description: \"{desc}\"\n")
                    f.write("compatibility: opencode\n")
                    f.write("metadata:\n")
                    if skill_data.get('model'):
                        f.write(f"  model: {skill_data['model']}\n")
                    if skill_data.get('model_reasoning_effort'):
                        f.write(f"  model_reasoning_effort: {skill_data['model_reasoning_effort']}\n")
                    if skill_data.get('sandbox_mode'):
                        f.write(f"  sandbox_mode: {skill_data['sandbox_mode']}\n")
                    f.write("---\n\n")
                    # Main content
                    f.write("## Instructions\n\n")
                    f.write(skill_data['instructions'])
                    f.write("\n")
                
                count += 1
                
    # Cleanup temp dir
    shutil.rmtree(TEMP_DIR, ignore_errors=True)
    print(f"Successfully synchronized and converted {count} skills from OpenCode Codex subagents.")

if __name__ == "__main__":
    sync_skills()
