import re
import sys


stringtoreplace = "<toc>"

def generateTOC(filename):
   contents = []
   with open(filename, "r") as ins:
      for line in ins:
         searchObj = re.search( r'(#+)\ (.+)', line, re.M|re.I)
         if searchObj:
            temp = {}
            level = len(searchObj.group(1))
            if (level > 1):
                  temp["level"] = level
                  temp["text"] = searchObj.group(2)
                  temp["link"] = "#"+searchObj.group(2).replace(" ","-").lower()
                  contents.append(temp)

   toctext = "# Table of Contents\n"
   for item in contents:
      line = (item['level'] - 2)*'\t' + "1. ["+item['text']+"]("+item['link']+") \n"
      toctext = toctext + line

   filecontents = ""
   with open(filename, 'r') as myfile:
      filecontents = myfile.read()
   filecontents = filecontents.replace(stringtoreplace,toctext)

   file_update = open(filename, "w")
   file_update.write(filecontents)
   file_update.close()



if __name__ == "__main__":
   if len(sys.argv) < 3:
      if(len(sys.argv) == 1):
         filename = "chapter.md"
      else:
         filename = sys.argv[1]
      generateTOC(filename)
   else:
      print("USAGE:", "$ python toc.py filename.md")