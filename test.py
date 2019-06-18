import thulac

thu1 = thulac.thulac(seg_only=True)  #只进行分词，不进行词性标注
text = thu1.cut("她杀约翰", text=True)  #进行一句话分词

print(text.split())