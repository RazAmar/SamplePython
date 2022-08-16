import xml.etree.ElementTree as ET

def ChangeRecipie(path):
    with open(path, 'r') as f:
        tree = ET.parse(f)
        root = tree.getroot()
    for SelfPorting in root.iter('SelfPorting'):
        SelfPorting.text = 'True'
    tree.write(path)

def getInput(file):
    link=open(file,"r").read()
    paths=open(link,"r").read()
    pathsList=paths.split(',')
    for p in pathsList:
        ChangeRecipie(p)


