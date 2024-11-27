import os
import csv
import yaml

def copy_csv_file(src_file, dest_file):
    filtered_rows = []
    with open(src_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        filtered_rows = [item for item in reader if ('tag' in item and 'macromanagers' in item['tag']) or ('tags' in item and 'macromanagers' in item['tags'])]
        
    if filtered_rows:
        with open(dest_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(filtered_rows)
        return True
    return False

def copy_yaml_file(src_file, dest_file):
    with open(src_file, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
            if not isinstance(data, list):
                return False
            
            filtered_data = [item for item in data if ('tag' in item and 'macromanagers' in item['tag']) or ('tags' in item and 'macromanagers' in item['tags'])]
            
            if filtered_data:
                with open(dest_file, 'w', encoding='utf-8') as f:
                    yaml.dump(filtered_data, f, allow_unicode=True)
                return True
        except:
            return False
    return False

def copy_data_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for root, _, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        for file in files:
            src_file = os.path.join(root, file)
            dest_subdir = os.path.join(dest_dir, rel_path)
            
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            dest_file = os.path.join(dest_subdir, file)
            
            if file.endswith('.csv'):
                copy_csv_file(src_file, dest_file)
            elif file.endswith(('.yaml', '.yml')):
                copy_yaml_file(src_file, dest_file)
