#定义一个接口
class choose(object):
    #不实现
    def choose_consumer(self):
        pass


#定义对象,并且实现接口,原生类，继承接口，同时定义装饰器继承接口，保证原生类不用代码重构


#TODO 假设要增强该类的我号异宽方法，就该用装饰器模式

class wkkh_term(choose):

    def __init__(self,res):

        self.res= res
    def choose_consumer(self):
        print('该对象基本功能')
        
    #我号异宽
    def df_whyk(self,df_tmp):
        df_tmp_res=df_tmp[(df_tmp['高价值80元以上客户']==self.res[0])&(df_tmp['办理7折提值大于0客户']==self.res[1])&(df_tmp['办理7折提值30-70客户']==self.res[2])&
        (df_tmp['终端换机']==self.res[3])&(df_tmp['4G资费']==self.res[4])&(df_tmp['预警']==self.res[5])&(df_tmp['不限量']==self.res[6])]
        return df_tmp_res
    
    #我宽异号
    def df_wkyh(self,df_tmp):
        df_tmp_res=df_tmp[(df_tmp['我宽异号']==self.res[0])&(df_tmp['是否裸奔高价值']==self.res[1])&(df_tmp['是否老旧设备']==self.res[2])&(df_tmp['免费成员空间']==self.res[3])&(df_tmp['全家享2.0']==self.res[4])]
        return df_tmp_res

    #全家享
    def df_qjx(self,df_tmp):
        df_tmp_res=df_tmp[(df_tmp['我宽异号']==self.res[0])&(df_tmp['是否裸奔高价值']==self.res[1])&(df_tmp['是否老旧设备']==self.res[2])&(df_tmp['免费成员空间']==self.res[3])&(df_tmp['全家享2.0']==self.res[4])]
        return df_tmp_res
    
    #终端购机
    def df_zdgj(self,df_tmp):
        df_tmp_res=df_tmp[(df_tmp['是否为宽带客户']==self.res[0])]
        return df_tmp_res

#定义装饰器，并且实现接口
class Decorator(choose):
    def __init__(self,choose):
        self.choose=choose
    def choose_consumer(self):
        pass


#实现装饰器，继承装饰类父类，并将choose接口对象注入该类
class extendChoose(Decorator):
    def __init__(self,choose):
        self.choose=choose
    


    def choose_consumer(self):
        print('增强前')
        self.choose.choose_consumer()
        print('增强后')


#eg
res=[1,1,1,1,1,1,1]
ob=wkkh_term(res)

extendChoose(ob).choose_consumer()