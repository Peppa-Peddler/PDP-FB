import files
import properties

names_path = "../fichas/ls-dxf.txt"

for tag in files.get_dfxs(names_path):
	properties.process(tag)
