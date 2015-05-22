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
    
            
             
                    


