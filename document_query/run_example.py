# 导库
import document_query

# 如果不用度盘查询可以忽略段代码--------------------
# 这俩玩意是用于获取access_token，在代码中用不到
document_query.AppKey = ""
document_query.url_get_access_token = ""
# 必要的token
document_query.access_token = ""
# ____________________________________________

# 查询的基本信息保存对象，如果有多个查询需求就可直接再创建一个
datas_1 = document_query.init_datas(
    # 其中只有rc_path是必填项，其他都是可选项
    # 被查询的文件夹路径
    files_path=None,
    # 被查询的文件的路径
    s_path=None,
    # 被查询的度盘文件夹路径
    panbaidu_path=None,
    # 输出查询结果的文件路径
    existlist_path=None,
    # 查询名单路径
    rc_path=None
)

# 创建顶层对象
top = document_query.datass()
# 把创建的基本信息保存对象全部添加导顶层模块中
top.data_append(datas_1)
# 开始
top.progress_all()
