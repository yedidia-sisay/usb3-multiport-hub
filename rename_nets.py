import re
import glob

replacements = {
    '"HDTX0P"': '"HDTX0+"',
    '"HDTX0P+"': '"HDTX0+"',
    '"HDTX0N"': '"HDTX0-"',
    '"HDTX0N-"': '"HDTX0-"',
    
    '"HDTX1P"': '"HDTX1+"',
    '"HDTX1P+"': '"HDTX1+"',
    '"HDTX1N"': '"HDTX1-"',
    '"HDTX1N-"': '"HDTX1-"',
    
    '"HDTX2P"': '"HDTX2+"',
    '"HDTX2P+"': '"HDTX2+"',
    '"HDTX2N"': '"HDTX2-"',
    '"HDTX2N-"': '"HDTX2-"',
    
    '"HDTXCP"': '"HDTXC+"',
    '"HDTXCP+"': '"HDTXC+"',
    '"HDTXCN"': '"HDTXC-"',
    '"HDTXCN-"': '"HDTXC-"',
}

pattern = re.compile(r'(\(\s*(?:label|global_label|hierarchical_label|property "Value")\s+)("HDTX[A-Z0-9+-]+")')

for file in glob.glob("*.kicad_sch"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_match(m):
        prefix = m.group(1)
        name = m.group(2)
        if name in replacements:
            return prefix + replacements[name]
        return m.group(0)
    
    new_content = pattern.sub(replace_match, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Modified {file}")
