file_list = ["http://www.abc.com/home/docs/alla.txt", "http://www.def.com/documents/files/bczw.txt", "http://www.ghi.com/data/documents/xdnq.txt", "http://www.jkl.com/docs/qwep.txt", "http://www.mno.com/files/documents/pozi.txt", "http://www.pqr.com/content/files/nvwt.txt", "http://www.stu.com/documents/ymco.txt", "http://www.vwx.com/files/documents/rkgi.txt", "http://www.yza.com/docs/xpty.txt", "http://www.bcd.com/documents/files/zxkj.txt", "http://www.efg.com/files/jqwx.txt", "http://www.hij.com/docs/files/btco.txt", "http://www.klm.com/files/mlzr.txt", "http://www.nop.com/documents/files/xpqw.txt", "http://www.qrs.com/files/documents/lmyn.txt", "http://www.tuv.com/data/qazx.txt", "http://www.vwx.com/docs/files/wsxq.txt", "http://www.xyz.com/documents/files/cvbn.txt", "http://www.abc.com/home/files/plko.txt", "http://www.def.com/documents/mkij.txt", "http://www.ghi.com/data/files/nhgb.txt", "http://www.jkl.com/files/documents/vcxz.txt", "http://www.mno.com/data/files/kiuj.txt", "http://www.pqr.com/documents/files/oplc.txt", "http://www.stu.com/docs/bqwe.txt"]
#print(len(file_list))= 25
splitted = []
temp = "randomjai"
for i in file_list:
	temp = i.split("/")
	splitted.append(temp)
for j in splitted:
	print(j[-1])
print(len(splitted))
