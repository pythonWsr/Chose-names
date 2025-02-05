def main(a=None):
    while True:
        if a == None:
            a = str.lower(input('你确定要清除数据吗？清除后将无法恢复,但可重新导入。(Y/n)'))

        if a == 'n' or a == 'no':
            exit()

        if a == 'y' or a == 'yes':
            import os
            input_template_All = []
            input_template_All_Path = []
            for root, dirs, files in os.walk(r'.\data', topdown=False):
                for name in files:
                    if os.path.splitext(name)[1] == '.txt':
                        input_template_All.append(name)
                        input_template_All_Path.append(os.path.join(root, name))

            for i in input_template_All_Path:
                if i in {'.\\data\\file_kind.txt',
                         '.\\data\\name_base.txt',
                         '.\\data\\xlsx_columns.txt',
                         '.\\data\\group_names.txt'}:
                    with open(i, 'w') as f:
                        f.close()
                elif i == '.\\data\\numbers.txt':
                    with open(i, 'w') as f:
                        f.write('0')
                else:
                    os.remove(i)

            print('已清除：' + str(input_template_All_Path))
            input('点击任意键以继续')
            exit()

if __name__ == '__main__':
    main()
