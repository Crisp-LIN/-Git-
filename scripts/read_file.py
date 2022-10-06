"""
with open('/home/linx/GitPractice/README','r',encoding = 'utf-8') as f:
	print(f.read())


import sys, getopt
opts, args = getopt.getopt(sys.argv[1:], "hi:o:") # a) sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。b) "hi:o:": 当一个选项只是表示开关状态时，即后面不带附加参数时，在分析串中写入选项字符。当选项后面是带一个附加参数时，在分析串中写入选项字符同时后面加一个":"号。所以"hi:o:"就表示"h"是一个开关选项；"i:"和"o:"则表示后面应该带一个参数。c) 调用getopt函数。函数返回两个列表：opts和args。opts为分析出的格式信息。args为不属于格式信息的剩余的命令行参数。opts是一个两元组的列表。每个元素为：(选项串,附加参数)。如果没有附加参数则为空串''。getopt函数的第三个参数[, long_options]为可选的长选项参数，上面例子中的都为短选项(如-i -o)。---长选项格式举例:

input_file=""
output_file=""
for op, value in opts:
	print(op)

    if op == "-i":

        input_file = value

    elif op == "-o":

        output_file = value

    elif op == "-h":

        usage()

        sys.exit()
"""
"""
import argparse

def train_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--normalize", default=True, type=bool, help='maximum depth')
    parser.add_argument("--n_estimators", default=100, type=int, help='number of estimators')
    parser.add_argument("--max_features", default=6, type=int, help='maximum of features',)
    parser.add_argument("--max_depth", default=5, type=int,help='maximum depth')
    opt = parser.parse_args()
    
    return opt
print(type(train_options()))
"""


