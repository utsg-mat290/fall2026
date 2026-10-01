#!/usr/bin/env python3
"""Render the R Markdown sources without R (requires Pandoc and PyYAML)."""
from html import escape
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def main():
    try:
        import yaml
    except ImportError:
        sys.exit('Install PyYAML, or use rmarkdown::render_site() in RStudio.')
    pandoc = shutil.which('pandoc')
    if not pandoc:
        sys.exit('Pandoc was not found. Install Pandoc, or render in RStudio.')
    config = yaml.safe_load((ROOT / '_site.yml').read_text(encoding='utf-8'))
    out = ROOT / config['output_dir']
    out.mkdir(exist_ok=True)
    for directory in ('css', 'images', 'files', 'worksheet', 'js', 'site_libs'):
        shutil.copytree(ROOT / directory, out / directory, dirs_exist_ok=True)
    (out / '.nojekyll').touch()
    nav = config['navbar']
    for page in ('index', 'syllabus'):
        items = []
        for item in nav['left']:
            active = item['href'] == page + '.html'
            li_class = ' class="active"' if active else ''
            current = ' aria-current="page"' if active else ''
            items.append(f'<li{li_class}><a href="{escape(item["href"], quote=True)}"{current}>{escape(item["text"])}</a></li>')
        navbar = '\n'.join([
            '<nav class="navbar navbar-default navbar-fixed-top" aria-label="Course navigation">',
            '<div class="container"><div class="navbar-header">',
            '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#course-nav" aria-expanded="false" aria-controls="course-nav">',
            '<span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button>',
            f'<a class="navbar-brand" href="index.html">{escape(nav["title"])}</a></div>',
            '<div class="collapse navbar-collapse" id="course-nav"><ul class="nav navbar-nav">',
            *items,
            '</ul></div></div></nav>'
        ])
        args = [pandoc, str(ROOT / (page + '.rmd')), '--from=markdown', '--to=html5',
                '--standalone', '--template=' + str(ROOT / 'tools/template.html'),
                '--variable=navbar:' + navbar,
                '--output=' + str(out / (page + '.html'))]
        for key, filename in [('head', 'head.html'), ('skiplink', 'skip-link.html'), ('footer', 'footer.html')]:
            args.append('--variable=' + key + ':' + (ROOT / 'includes' / filename).read_text(encoding='utf-8'))
        subprocess.run(args, cwd=ROOT, check=True)
        print('Built', out / (page + '.html'))


if __name__ == '__main__':
    main()
