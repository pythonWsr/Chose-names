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

def modify_target_file(target_file_path):
    with open(target_file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

    # 初始化行号，包括空行
    line_number = 1
    non_empty_lines = []

    for line in lines:
        # 保留所有行，包括空行
        non_empty_lines.append(line)
        if line_number == 240:
            # 修改第240行：将debug设置为False
            non_empty_lines[-1] = "debug = False\n"
        line_number += 1

    # 删除第248行及之后的所有内容
    if line_number >= 248:
        non_empty_lines = non_empty_lines[:247]

    # 重新写入修改后的行
    try:
        with open(target_file_path, 'w', encoding='utf-8') as file:
            file.writelines(non_empty_lines)
    except PermissionError as e:
        print(f"没有权限写入文件：{target_file_path}")

    print('Set debug to False successfully!')

if __name__ == '__main__':
    modify_target_file('guide.py')
    main()
