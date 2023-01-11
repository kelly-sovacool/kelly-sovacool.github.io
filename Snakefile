import datetime
import pathlib

rule convert_bib_to_yml:
    input:
        bib='cv/pubs.bib',
        py='cv/publications.py'
    output:
        yml='cv/pubs.yml'
    conda: 'environment.yml'
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

rule quarto_render:
    conda: 'environment.yml'
    shell:
        """
        quarto render
        """

rule postrender:
    input:
        rules.copy_keybase.output
