
import os
class BookspiderPipeline(object):

    def process_item(self, item, spider):

        curPath = 'E:/小说/'
        tempPath = str(item['book_name'])

        targetPath = curPath + tempPath
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        book_list_name = str(str(item['i'])+item['book_list_name'])
        filename_path = targetPath+'/'+book_list_name+'.txt'
        print('------------')
        print(filename_path)

        with open(filename_path,'a',encoding='utf-8') as f:
            f.write(item['book_content'])
        return item

