import os.path
import markdown


def openfile(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as opened_file:
        md_content = opened_file.read()

    md_html = markdown.markdown(md_content)
    data = {"text": md_html}

    return data
