class DataTypeChecker:
     @staticmethod
     def strIsFloat(string:str)->bool:
          try:
               float(string)
               return True
          except:
               return False