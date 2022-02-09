from __future__ import unicode_literals

import argparse
import os
import sys
import glob

from markdown2 import markdown_path
from weasyprint import HTML, CSS


def get_files(pattern="**"):
    files = []
    for file in glob.glob(pattern, recursive=True):
        files.append(file)
    return files


DEFAULT_MD2_EXTRAS = ['cuddled-lists', 'tables', 'header-ids', 'fenced-code-blocks', 'toc']

parser = argparse.ArgumentParser(description="Convert markdown files to PDFs")
parser.add_argument("md", help="The path/pattern of the mardown file(s) to convert", type=str, default="**.md")
parser.add_argument("--base-dir", help="The directory in the repository to be used as a base for local links", type=str, required=False, default=".")
parser.add_argument("--css-pattern", help="The path to a CSS file to use in the conversion", type=str, required=False, default="**.css")
parser.add_argument("--markdown2-extras", help="A comma-separated list of markdown2 extras", type=str, required=False, default=",".join(DEFAULT_MD2_EXTRAS))
parser.add_argument('--gh-actions', action='store_true')
args = parser.parse_args()

if args.markdown2_extras == "":
    args.markdown2_extras = ",".join(DEFAULT_MD2_EXTRAS)

css_files = get_files(pattern=args.css_pattern)
print("📄 Found {} css file(s)".format(len(css_files)))
styles = []
for css_file in css_files:
    try:
        styles.append(CSS(filename=css_file))
    except:
        print("🚨 Failed to get style from CSS file: {}".format(css_file))

base_dir = os.path.join(os.getcwd(), args.base_dir)
print("📁 PWD: {}".format(base_dir))
md2_extras = args.markdown2_extras.split(",")

md_files = get_files(pattern=args.md)
print("📄 Found {} markdown file(s)".format(len(md_files)))
if len(md_files) == 0:
    print("🆘 Need at least 1 markdown file to continue")
    sys.exit(1)
files_completed = []
for md_file in md_files:
    try:
        html_raw = markdown_path(md_file, extras=md2_extras)
        html = HTML(string=html_raw, base_url=base_dir)
        file_name, extension = os.path.splitext(md_file)
        html.write_pdf(file_name + ".pdf", stylesheets=styles)
        files_completed.append(file_name)
    except:
        print("🚨 Failed to convert MD file to PDF: {}".format(md_file))

if args.gh_actions:
    print("::set-output name=convertedFiles::{}".format(",".join(files_completed)))
