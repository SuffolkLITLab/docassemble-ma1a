# docassemble.ma1a

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Complete package for Massachusetts 1A no-fault divorce. Generates all required forms for uncontested divorce filing.

## What is this?

This Docassemble interview helps couples prepare all required forms for an **uncontested divorce** under Massachusetts General Laws Chapter 208, Section 1A (also called a "1A divorce").

A 1A divorce is available when both spouses agree the marriage has broken down irretrievably and have reached agreement on all issues including custody, support, and property division.

## Forms Generated

This interview creates up to 11 different forms based on your situation:

### Always Required
- **Joint Petition for Divorce (CJ-D 101A)** - Auto-filled with your information
- **Affidavit of Irretrievable Breakdown** - Auto-filled
- **Report of Absolute Divorce (R-408)** - Auto-filled
- **Financial Statements (Short or Long Form)** - Blank forms with guidance

### If You Have Children
- **Custody Disclosure Affidavit** - Provided with instructions
- **Child Support Guidelines Worksheet** - Link to official form with guidance

### If Needed
- **Separation Agreement** - Upload existing or guided drafting assistance
- **Findings & Determinations (CJD-305)** - If deviating from child support guidelines
- **Affidavit of Indigency** - If requesting fee waiver
- **Motion (CJD-400)** - If filing a specific motion

## Who is this for?

- **Pro se litigants** filing their own 1A divorce
- **Legal aid organizations** helping clients with divorce forms
- **Family law attorneys** streamlining routine 1A divorces
- **Court self-help centers** assisting the public

## Installation

### For Docassemble Administrators

1. Download the latest release: `docassemble_ma1a_v0.72.zip`
2. In your Docassemble server, go to **Package Management**
3. Click **Add Package** and upload the .zip file
4. Click **Install** to make it available to users

### Dependencies

This package requires:
- `docassemble.AssemblyLine` (core framework)
- `docassemble.ALToolbox` (enhanced functionality)
- `docassemble.ALMassachusetts` (Massachusetts-specific features)
- `docassemble.MassAccess` (court integration)

These will be installed automatically if not already present.

## Usage

### Starting the Interview

1. Create a new interview session
2. Select **"MA 1A Divorce Package"** from available interviews
3. Follow the guided questions (typically 30-45 minutes)
4. Review your answers
5. Download completed forms ready for court filing

### What to Expect

**Time Required**: 30-45 minutes depending on complexity
- Simple divorce (no children): ~25 minutes
- With children: ~35 minutes  
- Complex situations (all forms): ~45 minutes

**Information Needed**:
- Full names, addresses, and contact details for both spouses
- Marriage details (date, place, separation information)
- Children information (if applicable)
- Income information for financial statements
- Court selection (county where you or your spouse live)

## Features

- **Smart form selection** - Only generates forms you actually need
- **Auto-filled PDFs** - Core forms completed with your information
- **Guided assistance** - Clear instructions for complex forms
- **Mobile-friendly** - Works on phones, tablets, and computers
- **Court-ready output** - PDFs formatted for Massachusetts courts
- **Built-in help** - Tooltips and guidance throughout

## Technical Details

- **Built with**: Docassemble + AssemblyLine framework
- **Version**: 0.72.0
- **License**: MIT
- **Jurisdiction**: Massachusetts
- **Court System**: Probate and Family Court

## Support and Resources

- **Official Guide**: [MA 1A Divorce Process](https://www.mass.gov/guides/get-a-no-fault-1a-divorce)
- **Court Assistance**: [Find Your Probate & Family Court](https://www.mass.gov/orgs/probate-and-family-court)
- **Legal Help**: [Massachusetts Legal Services](https://www.masslegalservices.org)
- **Technical Issues**: [GitHub Issues](https://github.com/SuffolkLITLab/docassemble-ma1a/issues)

## Contributing

This project is part of the Suffolk LIT Lab's Document Assembly Line ecosystem. Contributions welcome!

## Changelog

### v0.72.0 (Current)
- Improved navigation with 8 detailed sections
- Updated resource links to official government sources
- Enhanced user experience with better help text
- Removed development artifacts from user interface

### Previous Versions
See [release history](https://github.com/SuffolkLITLab/docassemble-ma1a/releases) for complete changelog.

---

**Developed by**: Samuel Darkwa Jr
**Organization**: Suffolk Legal Innovation and Technology Lab  
**Framework**: [AssemblyLine Document Assembly](https://github.com/SuffolkLITLab/docassemble-AssemblyLine)