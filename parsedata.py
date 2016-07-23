import xml.etree.ElementTree as ET
import json
import sys
tree = ET.parse(sys.argv[1])
root = tree.getroot()
levels = []
for child in root:
  leveldata = {'Stardust': int(child[0].text), 'level': float(child[1].text), 'mincp': float(child[2].text), 'maxcp': float(child[3].text)}
  levels += [leveldata]
print json.dumps(levels, sort_keys=True, indent=2)
