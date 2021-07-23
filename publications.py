import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
import datetime

MONTHS = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}


def main():
    for entry in parse_entries():
        print(entry, '\n')

# adapted from https://bibtexparser.readthedocs.io/en/master/tutorial.html#step-4-add-salt-and-pepper
def parse_entries():
    with open('cv_KLS.bib', 'r') as bibtex_file:
        parser = BibTexParser()
        parser.customization = customizations
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    return sorted([BibEntry(record) for record in bib_database.entries], key = lambda x: x.year_mo, reverse = True)

def get_bib_str():
    return '\n'.join(f"{idx+1}. {entry.bib} {entry.altmetric()}" for idx, entry in enumerate(parse_entries()))

def get_markdown():
    table = ['| | | |', '|---|---|---|']
    entries = parse_entries()
    idx = len(entries)
    for entry in entries:
        table.append(f"| {idx}. | {entry.bib} | {entry.altmetric()} |")
        idx -= 1
    return table

# from https://bibtexparser.readthedocs.io/en/master/tutorial.html#step-4-add-salt-and-pepper
# Let's define a function to customize our entries.
# It takes a record and return this record.
def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = convert_to_unicode(record)
    record = type(record)
    record = author(record)
    record = editor(record)
    record = journal(record)
    record = keyword(record)
    record = link(record)
    record = page_double_hyphen(record)
    record = doi(record)
    return record


def format_author(name, bold = 'Sovacool, Kelly'):
    last_firstmi = name.split(',')
    lastname = last_firstmi[0]
    first_mi = last_firstmi[1].split()
    first_inits = first_mi[0][0] + first_mi[1][0] if len(first_mi) == 2 else first_mi[0][0]
    author = f'{lastname} {first_inits}'
    if bold in name:
        author = f'**{author}**'
    return author

class BibEntry:

    def __init__(self, record):
        self.record = record

    def altmetric(self, badge_type = 'donut', data_hide = "false"):
        #badge_type = 'donut'
        return f'<div data-badge-popover="right" data-badge-type="{badge_type}" data-doi="{self.record["doi"]}" data-condensed="true" data-hide-no-mentions="{data_hide}" class="altmetric-embed"></div>'

    def github_badge(self, font_size_px=48):
        return f'<a href="{self.github_link}"> <i class="fab fa-github" style="font-size:{font_size_px}px;"></i> </a>' if self.github_link else ''

    @property
    def github_link(self):
        return self.record['github'] if 'github' in self.record else ''

    @property
    def authors(self):
        return ', '.join([format_author(author) for author in self.record['author']])

    @property
    def month_num(self):
        return MONTHS[self.record['month']]

    @property
    def year_mo(self):
        return datetime.datetime.strptime(f"{self.record['year']}-{self.month_num}", '%Y-%m')

    @property
    def journal(self):
        return f"_{self.record['journal']['name']}_"

    @property
    def link(self):
        return f"[{self.record['doi']}]({self.record['link'][0]['url']})"

    @property
    def bib(self):
        return f"{self.authors}. {self.record['year']}. {self.record['title']}. {self.journal}. {self.link}"

    def __repr__(self):
        return self.bib


if __name__ == "__main__":
    main()
