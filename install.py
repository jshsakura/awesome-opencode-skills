import os
import sys
import shutil
from pathlib import Path

def main():
    print("🤖 Welcome to Awesome OpenCode Skills Installer!")
    
    # Opencode expects global skills in ~/.config/opencode/skills/
    target_dir = Path.home() / ".config" / "opencode" / "skills"
    source_dir = Path(__file__).parent / "skills"
    
    if not source_dir.exists():
        print("❌ Error: 'skills' directory not found. Please ensure the repository is fully cloned.")
        sys.exit(1)
        
    skills = [d.name for d in source_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]
    
    print(f"📦 Found {len(skills)} skills available for installation.")
    print(f"📂 Target installation path: {target_dir}")
    
    choice = input("\nDo you want to install ALL skills to your global OpenCode config? [Y/n]: ").strip().lower()
    if choice in ['n', 'no']:
        print("Installation cancelled.")
        sys.exit(0)
        
    print("\nCopying files...")
    os.makedirs(target_dir, exist_ok=True)
    
    installed_count = 0
    for skill in skills:
        skill_src = source_dir / skill
        skill_dest = target_dir / skill
        
        if skill_dest.exists():
            shutil.rmtree(skill_dest)
            
        shutil.copytree(skill_src, skill_dest)
        installed_count += 1
        
    print(f"\n✅ Successfully installed {installed_count} skills to {target_dir}")
    print("🚀 You can now use these skills in OpenCode!")
    print("Example usage in OpenCode: skill({ name: '" + (skills[0] if skills else "backend-developer") + "' })")

if __name__ == "__main__":
    main()
