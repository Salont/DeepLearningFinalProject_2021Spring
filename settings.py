
DataPath = "../Data/ctr_data.csv"
stdoutPath = "../Res/stdout.log"
LGBM_modelPath = "../Model/LightGBM/model.txt"

all_columns = [
    'server_ip',            # 服务器ip
    'log_time',             # 日志时间
    'guid',                 # 用户id
    'qua',                  # qua
    'doc_id',               # 文章id
    'action',               # 0：曝光 1：点击
    'action_time',          # 事件发生时的时间戳（精确到秒）
    'net_type',             # 网络类型
    'ui_type',              # ui类型
    'send_sequence',        # 第几刷
    'show_position',        # 第几位
    'hour',                 # 事件发生时是几点
    'isweekend',            # 是否周末
    'platform',             # 平台
    'version',              # 版本
    'new_doc_id',           # 已废弃，doc_id
    'query_id',             # 请求的标识id
    'sex_age_exposure',     # 性别_年龄_曝光数
    'sex_age_click',        # 性别_年龄_点击数
    'recall_exposure_click',  # 曝光数_点击数_召回策略
    'hobbyhitsubject_exposure',  # 兴趣命中主题_曝光数
    'hobbyhitsubject_click',    # 兴趣命中主题_点击数
    'hobbyclass_exposure',  # 兴趣分档_曝光数
    'hobbyclass_click',     # 兴趣分档_点击数
    'subject_sim',          # 主题相似度
    'hobbyclass',           # 兴趣分档(从0档开始)
    'is_operation',         # 是否运营数据(0:不是; 1:是)
    'taglevel_exposure',    # tag相似度分档_曝光数
    'taglevel_click',       # tag相似度分档_点击数
    'comlevel_exposure',    # 组合相似度分档_曝光数
    'comlevel_click',       # 组合相似度分档_点击数
    'usertagwgtlevel_exposure',  # 匹配用户tag权重分档_曝光数
    'usertagwgtlevel_click',    # 匹配用户tag权重分档_点击数
    'iuflevel_exposure',    # 用户文章iuf相似度分档_曝光数
    'iuflevel_click',       # 用户文章iuf相似度分档_点击数
    'tag_sim',              # tag相似度
    'tag_sim_level',        # tag相似度分档(从1档开始)
    'com_sim',              # 组合相似度
    'com_sim_level',        # 组合相似度分档
    'usertagwgt',           # 匹配用户tag权重
    'usertagwgt_level',     # 匹配用户tag权重分档(从1档开始)
    'iuf_sim',              # iuf相似度
    'iuf_sim_level',        # iuf相似度分档
    'doctagwgtlevel_exposure',  # 文章tag权重分档_曝光数
    'doctagwgtlevel_click',    # 文章tag权重分档_点击数
    'usermodelwgtlevel_exposure',  # 用户兴趣点权重分档_曝光数
    'usermodelwgtlevel_click',    # 用户兴趣点权重分档_点击数
    'doc_tag_wgt',          # 文章tag权重
    'doc_tag_wgt_level',    # 文章tag权重分档(从0档开始)
    'user_model_wgt',       # 用户兴趣点权重
    'user_model_wgt_level',  # 用户兴趣点权重分档(从0档开始)
    'grayfeature1_info',    # 灰度特征1信息（格式：曝光数_点击数_分档）(从1档开始)
    'grayfeature2_info',    # 灰度特征2信息（格式：曝光数_点击数_分档）(从1档开始)
    'grayfeature3_info',    # 灰度特征3信息（格式：曝光数_点击数_分档）(从1档开始)
    'grayfeature4_info',    # 灰度特征4信息（格式：曝光数_点击数_分档）(从1档开始)
    'gray_id',              # 灰度id
    'strategy',             # 策略（多个策略用;分隔）
    'data_src',             # 数据源
    'new_subject',          # 新主题
    'user_profile',         # 用户Profile
    'area',                 # 地域
    'is_mini_program']      # 小程序标记

useless_columns = [
    'server_ip',            # 服务器ip
    'log_time',             # 日志时间
    'qua',                  # qua
    'new_doc_id',           # 已废弃，doc_id
    'hobbyhitsubject_exposure',  # 兴趣命中主题_曝光数
    'hobbyhitsubject_click',     # 兴趣命中主题_点击数
    'hobbyclass_exposure',  # 兴趣分档_曝光数
    'hobbyclass_click',     # 兴趣分档_点击数
    'subject_sim',          # 主题相似度
    'hobbyclass',           # 兴趣分档(从0档开始)
    'is_operation',         # 是否运营数据(0:不是; 1:是)
    'taglevel_exposure',    # tag相似度分档_曝光数
    'taglevel_click',       # tag相似度分档_点击数
    'comlevel_exposure',    # 组合相似度分档_曝光数
    'comlevel_click',       # 组合相似度分档_点击数
    'usertagwgtlevel_exposure',  # 匹配用户tag权重分档_曝光数
    'usertagwgtlevel_click',    # 匹配用户tag权重分档_点击数
    'iuflevel_exposure',    # 用户文章iuf相似度分档_曝光数
    'iuflevel_click',       # 用户文章iuf相似度分档_点击数
    'tag_sim',              # tag相似度
    'tag_sim_level',        # tag相似度分档(从1档开始)
    'com_sim',              # 组合相似度
    'com_sim_level',        # 组合相似度分档
    'usertagwgt',           # 匹配用户tag权重
    'usertagwgt_level',     # 匹配用户tag权重分档(从1档开始)
    'iuf_sim',              # iuf相似度
    'iuf_sim_level',        # iuf相似度分档
    'doctagwgtlevel_exposure',  # 文章tag权重分档_曝光数
    'doctagwgtlevel_click',    # 文章tag权重分档_点击数
    'usermodelwgtlevel_exposure',  # 用户兴趣点权重分档_曝光数
    'usermodelwgtlevel_click',    # 用户兴趣点权重分档_点击数
    'doc_tag_wgt',          # 文章tag权重
    'doc_tag_wgt_level',    # 文章tag权重分档(从0档开始)
    'user_model_wgt',       # 用户兴趣点权重
    'user_model_wgt_level',  # 用户兴趣点权重分档(从0档开始)
    'grayfeature1_info',    # 灰度特征1信息（格式：曝光数_点击数_分档）(从1档开始)
    'grayfeature2_info',    # 灰度特征2信息（格式：曝光数_点击数_分档）(从1档开始)
    'grayfeature3_info',    # 灰度特征3信息（格式：曝光数_点击数_分档）(从1档开始)
    'grayfeature4_info',    # 灰度特征4信息（格式：曝光数_点击数_分档）(从1档开始)
    'gray_id',              # 灰度id
    'strategy',             # 策略（多个策略用;分隔）
    'data_src',             # 数据源
    'new_subject',          # 新主题
    'user_profile',         # 用户Profile
    'area',                 # 地域
    'is_mini_program']      # 小程序标记


lgb_params = {
	'task': 'train',
	'boosting_type': 'gbdt',
	'objective': 'binary',
	'metric': {'binary_logloss'},
	'num_leaves': 64,
	# 'num_trees': 100,
	'learning_rate': 0.01,
	'feature_fraction': 0.9,
	'bagging_fraction': 0.8,
	'bagging_freq': 5,
	'verbose': 0
}
