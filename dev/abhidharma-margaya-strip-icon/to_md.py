import os
import glob
from natsort import natsorted
from markdownify import markdownify as md

# 1. Find all html files
files = glob.glob("*.html")

# 2. Sort them naturally (handles 1.html, 1-2.html, 1-10.html correctly)
files = natsorted(files)
li = " ".join(files)

with open("list.txt", "w") as f:
    f.write(li)
    print(f"Found {len(files)} files. Starting conversion...")

final_markdown = ""

for file_name in files:
    print(f"Processing {file_name}...")
    
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
            # Convert HTML to Markdown
            # heading_style="ATX" ensures # Headers instead of underlined headers
            markdown_content = md(html_content, heading_style="ATX")
            
            # Add a separator between chapters (optional)
            final_markdown += f"\n\n<!-- Source: {file_name} -->\n\n"
            final_markdown += markdown_content
            final_markdown += "\n\n---\n\n" 
    except Exception as e:
        print(f"Error reading {file_name}: {e}")

# 3. Save to one file
output_file = "complete_sinhala_combined_book.md"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_markdown)

print(f"Done! Saved to {output_file}")