import os
import base64
import argparse

def filepath(relative):
    return os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir, relative))

with open(filepath("documents/template_blank.tex"), "r") as template_file:
    template_content = template_file.read()

with open(filepath("preamble/preamble_base.tex"), "r") as preamble_base_file:
    preamble_base_content = preamble_base_file.read()

with open(filepath("preamble/preamble_dk.tex"), "r") as preamble_dk_file:
    preamble_dk_content = preamble_dk_file.read()

with open(filepath("preamble/preamble_en.tex"), "r") as preamble_en_file:
    preamble_en_content = preamble_en_file.read()

with open("latexgen.py", "w") as output_script:
    output_script.write("#!/usr/bin/env python\n\n")
    output_script.write("import os\nimport base64\nimport argparse\n")
    output_script.write("template = \"\"\"%s\"\"\"\n" % ( base64.encodestring(template_content) ))
    output_script.write("preamble_base = \"\"\"%s\"\"\"\n" % ( base64.encodestring(preamble_base_content) ))
    output_script.write("preamble_en = \"\"\"%s\"\"\"\n" % ( base64.encodestring(preamble_en_content) ))
    output_script.write("preamble_dk = \"\"\"%s\"\"\"\n" % ( base64.encodestring(preamble_dk_content) ))
    output_script.write("""
    
parser = argparse.ArgumentParser(description='Make a LaTeX project from Steffan\\'s awesome template')
parser.add_argument('path', type=str, nargs='+', help='the path to build the project')
parser.add_argument('-l', type=str, nargs=1, help='the language of the preamble, \"en\" or \"dk\"', default=["en"])
parser.add_argument('--zip', dest='zip', action='store_const', const=True, default=False, help='zip the resulting project')
#TODO: Add -c option to clean folders first / after
args = parser.parse_args()

preamble_locale = 'preamble_dk' if args.l[0] == 'dk' else 'preamble_en'
preamble_l_content = preamble_dk if args.l[0] == 'dk' else preamble_en
preamble_l_content = base64.decodestring( preamble_l_content )
preamble_base_content = base64.decodestring( preamble_base )
template_content = base64.decodestring( template )

#TODO: make this specifiable in the prepare.py
######## MODIFICATIONS ########

template_content = template_content.replace( '\\subimport{../preamble/}{preamble_en.tex}',
'\\subimport{preamble/}{' + preamble_locale + '.tex}')

###############################

PATH = " ".join(args.path)
if not os.path.exists(PATH):
    os.makedirs(PATH)
os.chdir(PATH)
if not os.path.exists('preamble'):
    os.mkdir('preamble')
with open(os.path.join('preamble', preamble_locale + '.tex'), 'w') as preamble_l_file:
    preamble_l_file.write(preamble_l_content)

with open(os.path.join('preamble', 'preamble_base.tex'), 'w') as preamble_base_file:
    preamble_base_file.write(preamble_base_content)

with open('template.tex', 'w') as template_file:
    template_file.write(template_content)

if args.zip:
    fname = os.getcwd() #includes the filepath, sice we cd'ed to it
    import zipfile
    zipf = zipfile.ZipFile(fname + '.zip', 'w', zipfile.ZIP_DEFLATED)
    zipf.write(os.path.join('preamble', preamble_locale + '.tex'))
    zipf.write(os.path.join('preamble', 'preamble_base.tex'))
    zipf.write('template.tex')
    zipf.close()
raw_input('Success, Press enter to exit')
""")
