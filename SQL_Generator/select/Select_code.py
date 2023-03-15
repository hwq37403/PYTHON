from dataclasses import replace
import os
from re import A, template
import pandas as pd
from sqlalchemy import func

class Node():
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree():
    def __init__(self):
        self.root = None

    #层遍历
    def level_travel(self):
        res=''
        if self.root == None:
            return 
    
        queue = [self.root]
        while queue:
            cur = node = queue.pop(0)
            print(cur.elem, end=" ")
            res=res+cur.elem+" "
            if cur.lchild != None:
                queue.append(cur.lchild)
            if cur.rchild != None:
                queue.append(cur.rchild)
        return res
    
    #添加结点
    def add(self, item):
        node = Node(item)

        # 如果节点为空
        if self.root == None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.lchild == None:
                cur.lchild = node
                return 
            else:
                queue.append(cur.lchild)
            if cur.rchild == None:
                cur.rchild = node
                return 
            else:
                queue.append(cur.rchild)
    def preorder_travel(self, node):
        # 如果节点为空
        if node == None:
            return

        print(node.elem, end=" ")
        self.preorder_travel(node.lchild)
        self.preorder_travel(node.rchild)

    #中序遍历
    def inorder_travel(self, node):
        # 如果节点为空
        if node == None:
            return
        self.inorder_travel(node.lchild)
        print(node.elem, end=" ")
        self.inorder_travel(node.rchild)

"""
@description  : 条件字典，生成
---------
@param  :
-------
@Returns  :
-------
"""

def condInit():
    cond_conn_list=["","and","or"]
    id1=[0,1,2]
    d1=['','与','或']

    agg_list=["","AVG","MAX","MIN","COUNT","SUM","NO_OP"]
    id2=[0,1,2,3,4,5,6]
    d2=['','平均值','最大值','最小值','计数','求和','无运算']

    cond_list=[">","<","=","<>","NO_OP"]
    id3=[0,1,2,3,4]
    d3=['大于','小于','等于','不等','无运算']

    cond_conn_op=pd.DataFrame({'cond_conn_op':cond_conn_list,'id':id1,'description':d1})
    agg=pd.DataFrame({'agg':agg_list,'id':id2,'description':d2})
    cond_op=pd.DataFrame({'cond_op':cond_list,'id':id3,'description':d3})
    return cond_conn_op,agg,cond_op
    
def search(tableName_df,ts,i,j):
    tmp=tableName_df[tableName_df.iloc[:,i].str.contains(ts,case=False)].iloc[:,j]
    print('tmp:-------------------------------------------')

    print(tmp)
    if len(tmp)==0:
        return ts
    else:
        res=str(tmp.values)
        res=res.replace('[','').replace(']','').replace('\'','')
        # res=tmp
        return res

def keyTravel(key_dict):
    res=''
    for value in key_dict.values():
       res=res+value+','
    
    res=res[0:-1]
    print(res)
    return res

def sqlPrint(select_t):
    sql_res=''
    for v in select_t:
        sql_res=sql_res+str(v)
        sql_res=sql_res+' '
    print(sql_res)
    return sql_res



def select_sql():
    agg_tree = Tree()
    agg_input="等于"
    cond_conn_op,agg,cond_op=condInit()
    # print(cond_op)
    # con_key=
    


    op=search(cond_op,agg_input,2,0)

    print('agg:'+op)



    #default
    key_dict={'服务中心ID':'x_area_id','服务中心':'x_area'}
    table_dict={'表名':'yb_tmp_hwq_test'}

    directory_path=os.path.dirname(os.path.realpath(__file__))
    print(directory_path)
    tableName_df=pd.read_excel(directory_path+"/tableName.xlsx")

    #根据输入检索表名
    #比如mou
    ts="mou"


    tableName=search(tableName_df,ts,0,1)
    print(tableName)
    keywords=keyTravel(key_dict)


    # #二叉树存储条件，因为条件是运算表达式
    cond_tree=Tree()


    # #条件初始化
    # print(cond_conn_op.preorder_travel(cond_conn_op.root))
    # print(cond_conn_op.inorder_travel(cond_conn_op.root))

    cond_tree.add('x_area')
    cond_tree.add('is not null')

    cond_res=cond_tree.level_travel()

    select_t=['select',keywords,'from',tableName,'where',cond_res]

    sql_res=sqlPrint(select_t)


"""
@description  :输出sql查询语句
---------
@param  :keywords 字段,con 条件,group_key 分组字段,tableName 查询表名,#TODO agg1 运算操作
-------
@Returns  :
-------
"""
def initSqlTemplate(keywords,con,group_key,tableName):
    tableCount=len(tableName)


    if tableCount==2:
        table1=tableName[0]
        table2=tableName[1]
    else:
        table1=tableName[0]
        table2=''
    templateSql=['select key from table1 a',
   'select key from table1 a where con',
   'select a.* from table1 a,table2 b where con',
   'select a.*,b.key from table1 a left join table2 b on a.d1=b.d2 where con',
   'Select group_k,agg1 as name1 from table1 where con group by group_k'
   ]


    for sql in templateSql:
        print(sql.replace('key',keywords)
        .replace('con',con)
        .replace('group_k',group_key)
        .replace('table1',table1)
        .replace('table2',table2)
        )
        print(' ')


def table(words):
    directory_path=os.path.dirname(os.path.realpath(__file__))
    print(directory_path)
    tableName_df=pd.read_excel(directory_path+"/tableName.xlsx")

    #根据输入检索表名
    #比如mou

    tableName=search(tableName_df,words,0,1)
    return tableName


def append(list):
    list_res=[]
    for k in list:
        list_res.append(table(k))
    return list_res



def getCondition(op_input,conn_input,agg_input):
    cond_tree = Tree()

    cond_conn_op,agg,cond_op=condInit()

    print('test______________')
    print(cond_conn_op)
    print(agg)
    print(cond_op)

    # print('agg():'+agg)
    



    cond_conn=search(cond_conn_op,conn_input,2,0)
    cond=search(cond_op,op_input,2,0)
    op=search(agg,agg_input,2,0)


    print('conn:'+cond_conn)
    # print('cond:'+op)
    print('agg:'+cond)

    print('op:'+op)

    return cond_conn,cond,op
if __name__ == "__main__":
    
    # select_sql()
    keywords='x_area_id,x_area_name'

    con='x_area_id is not null'

    group_key='x_area_id,x_area_name'

    searchWords=['用户','全量']

    

    op_input="等于"    
    conn_input='与'
    agg_input="求和"
 

    tableName=append(searchWords)

    #获取条件及OP字段
    conn,agg,op=getCondition(op_input,conn_input,agg_input)

    #根据条件

    initSqlTemplate(keywords,con,group_key,tableName)




