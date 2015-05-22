The Excel class requires xlrd package installed.so install xlrd first before using this package
This class is for processing excel files using python. it is simple and straight forward
#use it like this

from xlpython.excel import Excel 

excel=Excel("/path/to/excelfile.xlsx",sheet_number)#sheet number is integer
excel.process(start_row)#call the process method with row to start in the excel
#the process method can be overridden as the example below:

    def process(self,start_row):
        """ to be overriden """
        """ sample processing is a shown
        #to skip heading start from 1 else start from 0
        for row_num in range((int(start_row)-1), self.get_total_rows()):
            row = self.get_row(row_num)
            #to get row's  column values
            column_val=self.sanitize(row[0])# first column is 0
            #if column is date
            date_val=self.get_date(row[0])
            #if column is time
            time_val=self.get_time(row[0])
            #if colum in phone number
            phone=self.create_phone_number('254', row[0])
    
            
            
#for Django users:

from xlpython.excel import Excel
""" get then excel from Django forms """
excel=request.FILES['excel_file'] 
""" we need to pass the sheet number and excel file as below """
excel=Excel(1,file_contents=excel.read()) 
""" then process your excel in a loop or how you want it """

for row_num in range((0, excel.get_total_rows()): """ we start from 0  if no headers in excel else 1"""
            row = excel.get_row(row_num)
            #to get row's  column values
            column_val=excel.sanitize(row[0])# first column is 0
            #if column is date
            date_val=excel.get_date(row[0])
            #if column is time
            time_val=excel.get_time(row[0])
            #if colum in phone number
            phone=excel.create_phone_number('254', row[0])

                    


