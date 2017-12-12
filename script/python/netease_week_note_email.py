#!/usr/bin/env python
# -*- coding: utf-8 -*-



import xml.sax
import json

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.title = []
        self.id = []
        self.CurrentData=""
        self.allContent=[];
        self.bugId=""
        self.bugTitle=""

    def dict_to_json(self, json_output):
        '''Coverts a dictionary into a json file.'''
        f = open(json_output, 'w')
        # content = json.dumps(''.join(self.allContent), ensure_ascii=False);
        content=''.join(self.allContent)
        print ("dictionary: " + content)
        f.write(content.encode("utf-8"))
        f.close()

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        # print "currentData: "+self.CurrentData
        if self.CurrentData == "title":
            self.title=[]
        elif self.CurrentData == "id":
            self.id=[]

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "title":
            # print json.dumps(''.join(self.title),ensure_ascii=False)
            splitContent = ''.join(self.title).split(":")
            firstSegment=splitContent[0].split(" ")
            if splitContent.__len__() == 2 and firstSegment.__len__()>1:
                self.bugTitle=splitContent[1]
                self.bugId = firstSegment[1]
                if(self.bugId!="" and self.bugTitle!=""):
                    self.allContent.append('<p>')
                    print "bugTitle: "+self.bugTitle
                    self.allContent.append(self.bugTitle.strip())
                    print "bugId: "+self.bugId
                else:
                    print "bugId or bugTitle is empty"
            else:
                self.bugId = ""

        elif self.CurrentData == "id":
            print "id: "+json.dumps(''.join(self.id),ensure_ascii=False)
            if self.bugId!="":
                for i in range(1,6):
                    self.allContent.append("&nbsp;")
                self.allContent.append('<a')
                self.allContent.append(' href="')
                self.allContent.append(''.join(self.id))
                self.allContent.append('"')
                self.allContent.append(">")
                self.allContent.append(self.bugId.strip())
                self.allContent.append('</a>')
                self.allContent.append('</p>')
            else:
                print "bugId is empty"

        elif tag =="feed":
            self.dict_to_json(destMockPath)

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "title":
            # print "content: "+content
            self.title.append(content)
        elif self.CurrentData == "id":
            self.id.append(content)



    def xml_to_etree(self,xml_input):
        '''Converts xml to a lxml etree.'''
        f = open(xml_input, 'r')
        xml = f.read()
        print("xml:"+xml)
        f.close()
        return xml

if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    # parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    sourceMockPath = "C:\\Users\\g8876\\Desktop\\email_example.txt";
    destMockPath = "C:\\Users\\g8876\\Desktop\\result.html";

    parser.parse(sourceMockPath)