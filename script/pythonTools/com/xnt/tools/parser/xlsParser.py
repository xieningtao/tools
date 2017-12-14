#!/usr/bin/env python
# -*- coding: utf-8 -*-



import xlrd
import json

def save(htmlContent,json_output):
        '''Coverts a dictionary into a json file.'''
        f = open(json_output, 'w')
        # content = json.dumps(''.join(self.allContent), ensure_ascii=False);
        content=''.join(htmlContent)
        print ("dictionary: " + content)
        f.write(content.encode("utf-8"))
        f.close()

if (__name__ == "__main__"):
    sourceMockPath = 'C:\\Users\\g8876\\Desktop\\month\\171214_issues_export_program.xls';
    destMockPath = "C:\\Users\\g8876\\Desktop\\program.html";
    data = xlrd.open_workbook(sourceMockPath)
    table = data.sheet_by_index(0)  # 通过索引顺序获取
    print"sheetName: " + json.dumps(table.name)
    allContent = [];
    nrows = table.nrows

    print "row: "+ str(nrows)

    for i in range(1, nrows):
        bugId = "#" + str(int(table.cell(i,0).value))
        bugHttp = "http://cc.pm.netease.com:8082/issues/" + str(int(table.cell(i,0).value))
        bugTitle = table.cell(i,6).value
        print "bugId: " + bugId + " title: " + bugTitle + " bugHttp: " + bugHttp
        allContent.append('<p>')
        allContent.append(bugTitle.strip())
        for i in range(1, 6):
            allContent.append("&nbsp;")
        allContent.append('<a')
        allContent.append(' href="')
        allContent.append(bugHttp)
        allContent.append('"')
        allContent.append(">")
        allContent.append(bugId.strip())
        allContent.append('</a>')
        allContent.append('</p>')
    save(allContent, destMockPath)
