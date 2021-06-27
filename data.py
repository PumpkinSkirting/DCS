class Data:
    global_value = 'Start'
    def RWN_Data(self, RWN, input_data=None):
        if RWN == 'r1':
            #Чтение последней строки
            with open('Data.txt', 'r') as Data_text:
                lines = Data_text.readlines()
            return lines[len(lines)-1]
        if RWN == 'w1':
            #Запись input_data а базу данных
            with open('Data.txt', 'a') as Data_text:
                Data_text.write(input_data + '\n')

        if RWN == 'n1':
            #Счетчик строк в базе данных
            with open('Data.txt', 'r') as Data_text:
                i=0
                for i in Data_text:
                    i+=1
            return i
        if RWN == 'r2':
            #Чтение последней строки
            with open('Data_f_d.txt', 'r') as Data_text:
                lines = Data_text.readlines()
            return lines[len(lines)-1]
        if RWN == 'w2':
            #Запись input_data а базу данных
            with open('Data_f_d.txt', 'a') as Data_text:
                Data_text.write(input_data + '\n')

        if RWN == 'n2':
            #Счетчик строк в базе данных
            with open('Data_f_d.txt', 'r') as Data_text:
                i=0
                for i in Data_text:
                    i+=1
            return i

Dron_data = Data()
Dron_data.RWN_Data('w1', '0')
Dron_data.RWN_Data('w1', '0')
Dron_data.RWN_Data('w2', '0')
Dron_data.RWN_Data('w2', '0')






