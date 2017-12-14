#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''A module for converting xml into json.'''

import json

from lxml import etree
from lxml.etree import fromstring
from xmljson import badgerfish as bf

def xml_to_json(xml_input, json_output):
    '''Converts an xml file to json.'''
    dict_to_json(xml_to_json_help(xml_to_etree(xml_input)), json_output)

def xml_to_etree(xml_input):
    '''Converts xml to a lxml etree.'''
    f = open(xml_input, 'r')
    xml = f.read()
    # print("xml: "+xml)
    f.close()
    return fromstring(xml)

def xml_to_json_help(content):
   return bf.data(content);

def dict_to_json(dictionary, json_output):
    '''Coverts a dictionary into a json file.'''
    f = open(json_output, 'w')
    content=json.dumps(dictionary, ensure_ascii = False);
    print ("dictionary: "+content)
    f.write(content.encode("utf-8"))
    f.close()

if __name__ == '__main__':
    sourceMockPath = "C:\\Users\\g8876\\Desktop\\email_example.txt";
    destMockPath = "C:\\Users\\g8876\\Desktop\\result.txt";
    xml_to_json(sourceMockPath,destMockPath)
