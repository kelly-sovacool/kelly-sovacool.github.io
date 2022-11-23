import datetime
import pathlib

now = datetime.datetime.now()
update_frequency = datetime.timedelta(days = 7)

bib_filename = 'cv/pubs.bib'
bib_path = pathlib.Path(bib_filename)
sh_filename = 'cv/download.sh'
sh_path = pathlib.Path(sh_filename)
# forcerun download rule if the downloaded file was last modified before today
if bib_path.exists():
    timestamp = datetime.datetime.fromtimestamp(bib_path.stat().st_mtime)
    if (now - update_frequency) > timestamp:
        sh_path.touch(exist_ok=True)

rule download_bib:
    input:
        sh=sh_filename
    output:
        bib=bib_filename
    params:
        url='https://raw.githubusercontent.com/kelly-sovacool/latex-cv/main/cv_KLS.bib'
    shell:
        """
        bash {input.sh} {params.url} {output.bib}
        """

rule convert_bib_to_yml:
    input:
        bib=rules.download_bib.output.bib,
        py='cv/publications.py'
    output:
        yml='cv/pubs.yml'
    shell:
        """
        python3 {input.py} {input.bib} {output.yml}
        """

rule copy_keybase:
    input:
        "keybase.txt"
    output:
        'docs/keybase.txt'
    shell:
        """
        cp {input} {output}
        """

rule prerender:
    input:
        rules.convert_bib_to_yml.output

rule postrender:
    input:
        rules.copy_keybase.output
