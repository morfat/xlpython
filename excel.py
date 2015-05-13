
"""
Author: Morfat Mosoti Ogega
Email: morfatmosoti@gmail.com
Phone: 0700872844
"""
import xlrd
   
class Excel:
    """For processing the excel sheet itself """
    
    def __init__(self,excel_file,sheet_number):
        self.book,self.sheet=self.open(excel_file, sheet_number)
        self.date_time=None
        
    def open(self,excel_file,sheet_number):
        book=xlrd.open_workbook(filename=excel_file)
        sheet=book.sheet_by_index(int(sheet_number)-1) #since first sheet is 0
        return [book,sheet]
    
    def get_book(self):
        return self.book
    
    
    def get_sheet(self):
        return self.sheet
    
    def get_total_rows(self):
        return int(self.get_sheet().nrows)
    
    def get_row(self,row_num):
        """return the row in the excel"""
        return self.get_sheet().row_values(row_num)
    
    def sanitize(self,string):
        """ improve the excel input into proper values """
        string=string.encode('utf8') if isinstance(string,basestring) else unicode(string).encode('utf8')
        return string[:-2] if (string.find('.0'))!=-1 else string
        
    def create_phone_number(self,area_code,phone):
        """form a phone number per area code . """
        return area_code+self.sanitize(phone)
    
    def set_date_time(self,val):
        #year, month, day, hour, minute, second 
        self.date_time=xlrd.xldate.xldate_as_datetime(val, self.get_book().datemode)
    
    def get_date_time(self):
        return self.date_time
    
    def get_date(self,date_val):
        """returns date from tuple """
        self.set_date_time(date_val)    
        return self.get_date_time().date()
    
    def get_time(self,time_val):
        """returns time from tuple """
        self.set_date_time(time_val)
        return self.get_date_time().time()
    
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
        """
        pass
    
            
             
                    
"""use it like this
 
excel=Excel("/home/mosoti/dok.xlsx",sheet_number)
excel.process(2)
"""


