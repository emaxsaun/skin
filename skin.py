import base64
import sys
from xml.dom import minidom
import re

basePath = 'skins'
skinName = sys.argv[1]
skinPath = basePath + '/' + skinName + '/src/' + skinName + '.xml'
skinFile = open(skinPath,'r')
skin = minidom.parse(skinFile)
components = skin.getElementsByTagName('component')
for component in components:
	componentName = component.attributes['name']
	elements = component.getElementsByTagName('element')
	for element in elements:
		elementPath = basePath + '/' + skinName + '/src/' + componentName.value + '/' + element.attributes['src'].value
		imageText = base64.b64encode(open(elementPath,'rb').read())
		imageText = imageText.decode('utf8')
		element.attributes['src'].value = 'data:image/png;base64,' + imageText
skinText = '\''+skin.toxml()+'\''

outputPath = skinPath = basePath + '/' + skinName + '/' + skinName + '.xml'
outputFile = open(outputPath,'w')
outputFile.write(skinText)
outputFile.close()