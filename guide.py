def writer():
    print('随机点名程序(write by wsr)引导')

def Writer():
    print('随机点名程序(write by wsr)')

def error_log(e):
    import time
    with open(r'.\log\error_' + str(time.time()) + '.txt', 'w', encoding='utf-8') as f:
        f.write(str(e))
        f.close()

def create_log():
    import os

    # 获取当前工作目录
    current_directory = os.getcwd()
    print(f"当前工作目录：{current_directory}")

    # 设置文件夹名称
    folder_name = "log"

    # 尝试创建文件夹
    try:
        os.mkdir(folder_name)
        print(f"文件夹 '{folder_name}' 已创建。")
    except FileExistsError as e:
        error_log(e)
    except PermissionError as e:
        error_log(e)
        print(f"没有权限在当前目录下创建文件夹 '{folder_name}'。")

def name_input():
    global pd

    try:
        import pandas as pd
        import filetype
        import os
    except ImportError as e:
        print('您尚未成功安装第三方库，请根据“操作指引.docx”安装第三方库！')
        error_log(e)
    os_kind = None
    file_kind = None

    with open(r'.\data\name_base.txt','r') as dat1:
        dat0 = dat1.read()
    if dat0 == '':
        print('您还未导入名单！')
        os_kind_list = ['.txt', '.log', '.md']

        while True:
            try:
                file_path = input('请在这里输入文件路径（拖拽文件至此，支持文件格式：*.xlsx, *.txt, *.log, *.md):')
                kind = filetype.guess(file_path)
                if kind is None:
                    file_kind = os.path.splitext(file_path)[1]
                else:
                    file_kind = '.' + kind.extension
                break
            except FileNotFoundError as e:
                error_log(e)
                print('这不是一个正确的文件路径名，请重新输入！')

        while True:
            if file_kind == '.xlsx':
                df = pd.read_excel(file_path) # 默认读取工作簿中第一个工作表，默认第一行为表头

                data = df.values # 获取整个工作表数据
                length = len(data)
                print("读取整个工作表的数据：\n{0}".format(data))
                column_list = df.columns.values
                print('读取列标题：', column_list)
                if len(column_list) > 1:
                    while True:
                        chose = input('请选择名单列（可输入行标题，也可输入行标题索引）')
                        try:
                            chose_num = int(chose)
                        except ValueError as e:
                            error_log(e)
                            try:
                                chose_num = list(column_list).index(chose)
                            except ValueError as e:
                                error_log(e)
                                print('这不是一个正确的索引，请重新输入！')
                                continue

                        try:
                            chose_columns = df.columns.values[chose_num]
                            break
                        except IndexError as e:
                            error_log(e)
                            print('这不是一个正确的索引，请重新输入！')
                else:
                    chose_columns = column_list[0]

                with open(r'.\data\xlsx_columns.txt', 'w', encoding='UTF-8') as dat2:
                    dat0 = dat2.write(str(chose_columns))

                with open(r'.\data\name_base.txt', 'w', encoding='UTF-8') as dat:
                    dat.write(str(list(df[chose_columns].values)))

                break

            elif file_kind in os_kind_list:
                with open(file_path, 'r', encoding='UTF-8') as f_name:
                    name_list = f_name.readlines()
                    names = []
                    for name in name_list:
                        names.append(name.splitlines()[0])
                print("读取整个名表的数据：\n" + str(names))

                with open(r'.\data\name_base.txt', 'w', encoding='UTF-8') as dat:
                    dat.write(str(names))

                break

            else:
                print('暂不支持导入此类型文件，请重试！')

        with open(r'.\data\file_kind.txt', 'w', encoding='UTF-8') as dat:
            dat.write(str(file_kind))

        with open(r'.\data\numbers.txt', 'w', encoding='UTF-8') as dat:
            dat.write('1')

def new_group(group_name):
    import pandas as pd
    import filetype
    import os
    os_kind = None
    file_kind = None


    os_kind_list = ['.txt', '.log', '.md']
    while True:
        try:
            file_path = input('请在这里输入文件路径（拖拽文件至此，支持文件格式：*.xlsx, *.txt, *.log, *.md):')
            kind = filetype.guess(file_path)
            if kind is None:
                file_kind = os.path.splitext(file_path)[1]
            else:
                file_kind = '.' + kind.extension
            break
        except FileNotFoundError as e:
            error_log(e)
            print('这不是一个正确的文件路径名，请重新输入！')

    if file_kind == '.xlsx':
        df = pd.read_excel(file_path) # 默认读取工作簿中第一个工作表，默认第一行为表头

        data = df.values # 获取整个工作表数据
        length = len(data)
        print("读取整个工作表的数据：\n{0}".format(data))
        column_list = df.columns.values
        print('读取列标题：', column_list)
        if len(column_list) > 1:
            while True:
                chose = input('请选择名单列（可输入行标题，也可输入行标题索引）')
                try:
                    chose_num = int(chose)
                except ValueError as e:
                    error_log(e)
                    try:
                        chose_num = list(column_list).index(chose)
                    except ValueError as e:
                        error_log(e)
                        print('这不是一个正确的索引，请重新输入！')
                        continue

                try:
                    chose_columns = df.columns.values[chose_num]
                    break
                except IndexError as e:
                    error_log(e)
                    print('这不是一个正确的索引，请重新输入！')
        else:
            chose_columns = column_list[0]

        with open(r'.\data\xlsx_columns_' + str(group_name) + '.txt', 'w', encoding='UTF-8') as dat2:
            dat0 = dat2.write(str(chose_columns))

        with open(r'.\data\group_' + str(group_name) + '.txt', 'w', encoding='UTF-8') as dat:
            dat.write(str(list(df[chose_columns].values)))


    elif file_kind in os_kind_list:
        with open(file_path, 'r', encoding='UTF-8') as f_name:
            name_list = f_name.readlines()
            names = []
            for name in name_list:
                names.append(name.splitlines()[0])
        print("读取整个名表的数据：\n" + str(names))

        with open(r'.\data\group_' + str(group_name) + '.txt', 'w', encoding='UTF-8') as dat:
            dat.write(str(names))

    with open(r'.\data\file_kind_' + str(group_name) + '.txt', 'w', encoding='UTF-8') as dat:
        dat.write(str(file_kind))

    with open(r'.\data\numbers.txt', 'r+', encoding='UTF-8') as dat:
        n = dat.read()
        n = int(n) + 1
        dat.write(str(n))

    with open('.\\data\\group_names.txt', 'r+', encoding='UTF-8') as dat:
        dat.write(dat.read() + group_name + '\n')

def change_title(old_title,new_title):
    import os
    directory = ".\\data"
    file_name = "title_list.txt"
    file_path = os.path.join(directory, file_name)
    change_title_dict = {old_title:new_title}
    # 检查文件是否存在
    if not os.path.exists(file_path):
        try:
            # 如果文件不存在，创建文件
            with open(file_path, 'w') as file:
                file.write(str(change_title_dict))
            print('Succeed to create changed title.')
            changed_title_dict = {}
        except PermissionError as e:
            error_log(e)
            print(f"没有权限在目录 '{directory}' 中创建文件 '{file_name}'。")
    else:
        with open(file_path, 'r') as file:
            changed_title_dict = eval(file.read())
        changed_title_dict = {**changed_title_dict, **change_title_dict}
        print('Now new titles are: ' + str(changed_title_dict))
        with open(file_path, 'w') as file:
            file.write(str(changed_title_dict))
    old_title_dict = {}
    for old_title, new_title in changed_title_dict.items():
        old_title_dict[new_title] = old_title
    with open('.\\data\\old_title.txt', 'w', encoding='UTF-8') as file:
        file.write(str(old_title_dict))
        file.close()

debug = False
if __name__ == '__main__' and debug is False:
    writer()
    create_log()
    name_input()

if __name__ == '__main__' and debug is True:
    print('There is nothing.')
