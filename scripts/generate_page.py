import codecs
import sys

CONTENT = u"CONTENT"

# probably a better way to do this
content = u""
with codecs.open(sys.argv[1], 'rb', encoding='utf-8') as f:
    for line in f:
        content += line
        
with codecs.open(sys.argv[2], 'rb', encoding='utf-8') as f:
    with codecs.open(sys.argv[3], 'wb', encoding='utf-8') as g:
        for line in f:
            line = line.strip()
            if line == CONTENT:
                g.write(content+"\n")
            else:
                g.write(line+"\n")
                
            
