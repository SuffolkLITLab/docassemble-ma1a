import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ma1a',
      version='0.72.1',
      description=('Massachusetts 1A Divorce Forms'),
      long_description='# docassemble.ma1a\r\n\r\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\r\n\r\nComplete package for Massachusetts 1A no-fault divorce. Generates all required forms for uncontested divorce filing.\r\n\r\n## What is this?\r\n\r\nThis Docassemble interview helps couples prepare all required forms for an **uncontested divorce** under Massachusetts General Laws Chapter 208, Section 1A (also called a "1A divorce").\r\n\r\nA 1A divorce is available when both spouses agree the marriage has broken down irretrievably and have reached agreement on all issues including custody, support, and property division.\r\n\r\n## Forms Generated\r\n\r\nThis interview creates up to 11 different forms based on your situation:\r\n\r\n### Always Required\r\n- **Joint Petition for Divorce (CJ-D 101A)** - Auto-filled with your information\r\n- **Affidavit of Irretrievable Breakdown** - Auto-filled\r\n- **Report of Absolute Divorce (R-408)** - Auto-filled\r\n- **Financial Statements (Short or Long Form)** - Blank forms with guidance\r\n\r\n### If You Have Children\r\n- **Custody Disclosure Affidavit** - Provided with instructions\r\n- **Child Support Guidelines Worksheet** - Link to official form with guidance\r\n\r\n### If Needed\r\n- **Separation Agreement** - Upload existing or guided drafting assistance\r\n- **Findings & Determinations (CJD-305)** - If deviating from child support guidelines\r\n- **Affidavit of Indigency** - If requesting fee waiver\r\n- **Motion (CJD-400)** - If filing a specific motion\r\n\r\n## Who is this for?\r\n\r\n- **Pro se litigants** filing their own 1A divorce\r\n- **Legal aid organizations** helping clients with divorce forms\r\n- **Family law attorneys** streamlining routine 1A divorces\r\n- **Court self-help centers** assisting the public\r\n\r\n## Installation\r\n\r\n### For Docassemble Administrators\r\n\r\n1. Download the latest release: `docassemble_ma1a_v0.72.zip`\r\n2. In your Docassemble server, go to **Package Management**\r\n3. Click **Add Package** and upload the .zip file\r\n4. Click **Install** to make it available to users\r\n\r\n### Dependencies\r\n\r\nThis package requires:\r\n- `docassemble.AssemblyLine` (core framework)\r\n- `docassemble.ALToolbox` (enhanced functionality)\r\n- `docassemble.ALMassachusetts` (Massachusetts-specific features)\r\n- `docassemble.MassAccess` (court integration)\r\n\r\nThese will be installed automatically if not already present.\r\n\r\n## Usage\r\n\r\n### Starting the Interview\r\n\r\n1. Create a new interview session\r\n2. Select **"MA 1A Divorce Package"** from available interviews\r\n3. Follow the guided questions (typically 30-45 minutes)\r\n4. Review your answers\r\n5. Download completed forms ready for court filing\r\n\r\n### What to Expect\r\n\r\n**Time Required**: 30-45 minutes depending on complexity\r\n- Simple divorce (no children): ~25 minutes\r\n- With children: ~35 minutes  \r\n- Complex situations (all forms): ~45 minutes\r\n\r\n**Information Needed**:\r\n- Full names, addresses, and contact details for both spouses\r\n- Marriage details (date, place, separation information)\r\n- Children information (if applicable)\r\n- Income information for financial statements\r\n- Court selection (county where you or your spouse live)\r\n\r\n## Features\r\n\r\n- **Smart form selection** - Only generates forms you actually need\r\n- **Auto-filled PDFs** - Core forms completed with your information\r\n- **Guided assistance** - Clear instructions for complex forms\r\n- **Mobile-friendly** - Works on phones, tablets, and computers\r\n- **Court-ready output** - PDFs formatted for Massachusetts courts\r\n- **Built-in help** - Tooltips and guidance throughout\r\n\r\n## Technical Details\r\n\r\n- **Built with**: Docassemble + AssemblyLine framework\r\n- **Version**: 0.72.0\r\n- **License**: MIT\r\n- **Jurisdiction**: Massachusetts\r\n- **Court System**: Probate and Family Court\r\n\r\n## Support and Resources\r\n\r\n- **Official Guide**: [MA 1A Divorce Process](https://www.mass.gov/guides/get-a-no-fault-1a-divorce)\r\n- **Court Assistance**: [Find Your Probate & Family Court](https://www.mass.gov/orgs/probate-and-family-court)\r\n- **Legal Help**: [Massachusetts Legal Services](https://www.masslegalservices.org)\r\n- **Technical Issues**: [GitHub Issues](https://github.com/SuffolkLITLab/docassemble-ma1a/issues)\r\n\r\n## Contributing\r\n\r\nThis project is part of the Suffolk LIT Lab\'s Document Assembly Line ecosystem. Contributions welcome!\r\n\r\n## Changelog\r\n\r\n### v0.72.0 (Current)\r\n- Improved navigation with 8 detailed sections\r\n- Updated resource links to official government sources\r\n- Enhanced user experience with better help text\r\n- Removed development artifacts from user interface\r\n\r\n### Previous Versions\r\nSee [release history](https://github.com/SuffolkLITLab/docassemble-ma1a/releases) for complete changelog.\r\n\r\n---\r\n\r\n**Developed by**: Samuel Darkwa Jr\r\n**Organization**: Suffolk Legal Innovation and Technology Lab  \r\n**Framework**: [AssemblyLine Document Assembly](https://github.com/SuffolkLITLab/docassemble-AssemblyLine)',
      long_description_content_type='text/markdown',
      author='Samuel Darkwa Jr',
      author_email='sam.darkwa@su.suffolk.edu',
      license='',
      url='https://github.com/SuffolkLITLab/docassemble-ma1a',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ma1a/', package='docassemble.ma1a'),
     )
