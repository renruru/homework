import xlrd
import xlwt

def readExcle(filename):
    workbook = xlrd.open_workbook(filename,'r')
    sheet_names = workbook.sheet_names()
    for sheet_name in sheet_names:
        sheet2 = workbook.sheet_by_name(sheet_name)
        print(sheet_name)
        rows = sheet2.row_values(1) # 获取第1行内容
        print(rows)
        cols = sheet2.col_values(1) # 获取第1列内容
        print(cols)


def writeExcle(sheetname):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheetbook = book.add_sheet(sheetname,cell_overwrite_ok=True)
    # txt1 = "编号"
    # sheetbook.write(0,0,txt1.decode('utf-8'))
    # sheetbook.write(0,1,'执行操作'.decode('utf-8'))
    # sheetbook.write(0,2,'预期结果'.decode('utf-8'))
    # sheetbook.write(0,3,'备注'.decode('utf-8'))
    row = [u'编号',u'执行操作',u'预期结果',u'备注']
    for i in range(len(row)):
        sheetbook.write(0,i,row[i])
    for j in range(1,10):
        sheetbook.write(j,0,j)
        j+=1   
    
    book.save(r'.\demo.xls') 


if __name__ == '__main__':
    filename1 = "./2018年Q1绩效考核表.xlsx"
    readExcle(filename1)
    writeExcle(sheetname='test')