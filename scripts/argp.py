import argparse     # 引入模块
# 建立解析对象
parser = argparse.ArgumentParser()
 
parser.add_argument("echo",help = "echo is here~",type = int)   # a)xx.add_argument("aa") 给xx对象增加一个aa属性;当前情况下为给parser对象增加一个"echo"属性 b)type = int 规定可传入参数的类型
parser.add_argument('--algo', help='algorithm',
                    choices=['DQN', 'Double', 'Dueling','DuelingDouble'],
                    default='DQN')

 
# 把parser中设置的所有"add_argument"给返回到args子类对象当中
# 那么parser中增加的属性内容都会在args对象中，使用即可。·
args = parser.parse_args()

# print(args.echo)     # 打印定位参数echo
print(args.algo+"测试")
