import os

def fix_dependency_of_template(filename):
    with open(filename) as file:
        file_content = file.read()
        file_content = file_content.replace("{../preamble/}", "{preamble/}")
        return file_content

if __name__ == "__main__":
    templates = [
        "template_blank.tex",
        # "template_dissertation.tex",
        "template_report.tex",
        # "template_beamer.tex"
    ]

    for template in templates:
        template_content = fix_dependency_of_template("documents/" + template)
        with open(template, 'w') as out_file:
            out_file.write(template_content)


