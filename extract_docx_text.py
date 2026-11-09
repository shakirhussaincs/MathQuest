import sys, zipfile, re, xml.etree.ElementTree as ET

def extract_text(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        with z.open('word/document.xml') as f:
            xml = f.read().decode('utf-8')
    # remove namespaces
    xml = re.sub(r'xmlns:[^=]*="[^"]*"', '', xml)
    xml = re.sub(r'xmlns="[^"]*"', '', xml)
    root = ET.fromstring(xml)
    texts = []
    for elem in root.iter():
        if elem.tag == 'w:t' or elem.tag.endswith('}t'):
            texts.append(elem.text)
    return '\n'.join(filter(None, texts))

if __name__ == '__main__':
    path = sys.argv[1]
    print(extract_text(path))

