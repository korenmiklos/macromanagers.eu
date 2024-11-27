import os
import yaml

def has_macromanagers_tag(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # Read until second '---' to get YAML front matter
        content = ''
        yaml_count = 0
        for line in f:
            if line.strip() == '---':
                yaml_count += 1
                if yaml_count == 2:
                    break
            content += line
        
        if yaml_count < 2:
            return False
        
        try:
            front_matter = yaml.safe_load(content)
            tags = front_matter.get('tag', [])
            if not tags:
                tags = front_matter.get('tags', [])
            return 'macromanagers' in (tags if isinstance(tags, list) else [tags])
        except:
            return False

def copy_markdown_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for root, _, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        for file in files:
            if not file.endswith('.md'):
                continue
                
            src_file = os.path.join(root, file)
            if has_macromanagers_tag(src_file):
                dest_subdir = os.path.join(dest_dir, rel_path)
                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)
                dest_file = os.path.join(dest_subdir, file)
                with open(src_file, 'r', encoding='utf-8') as sf, open(dest_file, 'w', encoding='utf-8') as df:
                    df.write(sf.read())
