#定义一个接口
from asyncio.windows_events import NULL
from hashlib import new
from msilib.schema import SelfReg
from types import new_class


class choose(object):
    #不实现
    def choose_consumer(self):
        pass


#real_class
class wkkh_term(choose):

    def __init__(self,res):
        self=choose
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


class ProxyClass(choose):
    def __init__(self) -> None:
        super().__init__()
        self.wkkh_term=choose

    def choose_consumer(self):
        if self.wkkh_term is not NULL:
            print('代理成功')
            self.wkkh_term==wkkh_term(choose)
        self,wkkh_term.choose_consumer(self)




ProxyClass().choose_consumer()