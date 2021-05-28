import os
import xml.etree.ElementTree as ET

from tqdm import tqdm


def HRSC2COCO(xml_path, json_path):
    xml_names = os.listdir(xml_path)
    for xml_name in tqdm(xml_names):
        xml_file_path = os.path.join(xml_path, xml_name)

        root = ET.parse(xml_file_path).getroot()
        
