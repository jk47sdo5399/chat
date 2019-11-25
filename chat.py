#读取文件
def read_file(file_name):
    lines = []
    with open (file_name,'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#格式转换
def convert(lines):
    new = []
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        new.append(person + ':' + line)
    return new

#主函数
def main():
    lines = read_file('075 input.txt')
    print(lines)
    print (convert(lines))

if __name__ == '__main__':
    main()