import os
import sys
import shutil
import subprocess
import re
from pathlib import Path

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
README_PATH = Path("README.md")

CATEGORY_TITLES = {
    '01-core-development': '01. Core Development',
    '02-language-specialists': '02. Language Specialists',
    '03-infrastructure': '03. Infrastructure',
    '04-quality-security': '04. Quality & Security',
    '05-data-ai': '05. Data & AI',
    '06-developer-experience': '06. Developer Experience',
    '07-specialized-domains': '07. Specialized Domains',
    '08-business-product': '08. Business & Product',
    '09-meta-orchestration': '09. Meta & Orchestration',
    '10-research-analysis': '10. Research & Analysis',
    '11-ai-governance-safety': '11. AI Governance & Safety',
    '12-platform-engineering-idp': '12. Platform Engineering & IDP',
    '13-llmops-evals-observability': '13. LLMOps, Evals & Observability',
}

def parse_toml_fallback(content):
    data = {}
    for key in ['name', 'description', 'model', 'model_reasoning_effort', 'sandbox_mode']:
        match = re.search(rf'{key}\s*=\s*(["\'])(.*?)\1', content)
        if match:
            data[key] = match.group(2)
            
    dev_inst_match = re.search(r'developer_instructions\s*=\s*"""(.*?)"""', content, re.DOTALL)
    if dev_inst_match:
        data['developer_instructions'] = dev_inst_match.group(1).strip()
    else:
        inst_text_match = re.search(r'\[instructions\]\s*text\s*=\s*"""(.*?)"""', content, re.DOTALL)
        if inst_text_match:
            data['developer_instructions'] = inst_text_match.group(1).strip()
            
    return data

def generate_readme_table(categories_data):
    lines = []
    for cat_name in sorted(categories_data.keys()):
        if cat_name == 'categories':
            continue
            
        formatted_cat = CATEGORY_TITLES.get(cat_name)
        if not formatted_cat:
            if '-' in cat_name:
                parts = cat_name.split('-', 1)
                formatted_cat = f"{parts[0]}. {parts[1].replace('-', ' ').title()}"
            else:
                formatted_cat = cat_name.title()

        lines.append(f"### {formatted_cat}")
        lines.append("")
        lines.append("| Skill | Description |")
        lines.append("|-------|-------------|")
        
        skills = sorted(categories_data[cat_name], key=lambda x: x['name'])
        for skill in skills:
            name = skill['name']
            desc = skill['description'].replace('\\n', ' ').strip()
            lines.append(f"| [**{name}**](skills/{name}/SKILL.md) | {desc} |")
        lines.append("")
        
    return "\n".join(lines)

def update_readme(table_content, skill_count, category_count):
    if not README_PATH.exists():
        return

    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<!-- START_SKILLS_TABLE -->).*?(<!-- END_SKILLS_TABLE -->)'
    content = re.sub(pattern, rf'\1\n{table_content}\n\2', content, flags=re.DOTALL)

    count_replacements = [
        (r'subagents-\d+-blue', f'subagents-{skill_count}-blue'),
        (r'The awesome collection of \d+\+ Codex subagents across \d+ categories\.',
         f'The awesome collection of {skill_count}+ Codex subagents across {category_count} categories.'),
        (r'takes the \d+\+ highly specialized Codex',
         f'takes the {skill_count}+ highly specialized Codex'),
        (r'adapts the \d+\+ subagents',
         f'adapts the {skill_count}+ subagents'),
        (r'install all \d+\+ skills via a single command',
         f'install all {skill_count}+ skills via a single command'),
    ]
    for pat, repl in count_replacements:
        content = re.sub(pat, repl, content)

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

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
    
    categories_data = {}
    count = 0
    
    for root, dirs, files in os.walk(categories_dir):
        category = os.path.basename(root)
        if category == 'categories':
            continue
            
        if category not in categories_data:
            categories_data[category] = []
            
        for file in files:
            if file.endswith('.toml'):
                toml_path = Path(root) / file
                
                with open(toml_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                skill_data = {}
                if tomllib:
                    try:
                        data = tomllib.loads(content)
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
                    
                categories_data[category].append({
                    'name': skill_data['name'],
                    'description': skill_data['description']
                })
                    
                skill_dir = SKILLS_DIR / skill_data['name']
                os.makedirs(skill_dir, exist_ok=True)
                
                skill_md_path = skill_dir / "SKILL.md"
                with open(skill_md_path, 'w', encoding='utf-8') as f:
                    f.write("---\n")
                    f.write(f"name: {skill_data['name']}\n")
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
                    f.write("## Instructions\n\n")
                    f.write(skill_data['instructions'])
                    f.write("\n")
                
                count += 1
                
    table_content = generate_readme_table(categories_data)
    update_readme(table_content, count, len(categories_data))
                
    shutil.rmtree(TEMP_DIR, ignore_errors=True)
    print(f"Successfully synchronized {count} skills and updated README.md.")

if __name__ == "__main__":
    sync_skills()
