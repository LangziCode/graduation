DROP TABLE IF EXISTS `storeup`; CREATE TABLE `storeup` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`refid`  bigint(20) NULL DEFAULT NULL COMMENT '收藏id' ,
`tablename`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '表名' ,
`name`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '收藏名称' ,
`picture`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '收藏图片' ,
`type`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '1' COMMENT '类型(1:收藏,21:赞,22:踩)' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='收藏表'
AUTO_INCREMENT=1637562662544
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `address`; CREATE TABLE `address` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`address`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '地址' ,
`name`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '收货人' ,
`phone`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '电话' ,
`isdefault`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '是否默认地址[是/否]' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='地址'
AUTO_INCREMENT=7
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `orders`; CREATE TABLE `orders` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`orderid`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '订单编号' ,
`tablename`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT 'ziliaoxinxi' COMMENT '商品表名' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`goodid`  bigint(20) NOT NULL COMMENT '商品id' ,
`goodname`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品名称' ,
`picture`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品图片' ,
`buynumber`  int(11) NOT NULL COMMENT '购买数量' ,
`price`  float NOT NULL DEFAULT 0 COMMENT '价格/积分' ,
`discountprice`  float NULL DEFAULT 0 COMMENT '折扣价格' ,
`total`  float NOT NULL DEFAULT 0 COMMENT '总价格/总积分' ,
`discounttotal`  float NULL DEFAULT 0 COMMENT '折扣总价格' ,
`type`  int(11) NULL DEFAULT 1 COMMENT '支付类型' ,
`status`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '状态' ,
`address`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '地址' ,
PRIMARY KEY (`id`),
UNIQUE INDEX `orderid` (`orderid`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='订单'
AUTO_INCREMENT=1635842906062
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `cart`; CREATE TABLE `cart` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`tablename`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT 'ziliaoxinxi' COMMENT '商品表名' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`goodid`  bigint(20) NOT NULL COMMENT '商品id' ,
`goodname`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '商品名称' ,
`picture`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '图片' ,
`buynumber`  int(11) NOT NULL COMMENT '购买数量' ,
`price`  float NULL DEFAULT NULL COMMENT '单价' ,
`discountprice`  float NULL DEFAULT NULL COMMENT '会员价' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='购物车表'
AUTO_INCREMENT=1625197454864
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `news`; CREATE TABLE `news` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`title`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '标题' ,
`introduction`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '简介' ,
`picture`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '图片' ,
`content`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '内容' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='公告信息'
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `forum`; CREATE TABLE `forum` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`title`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '帖子标题' ,
`content`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '帖子内容' ,
`parentid`  bigint(20) NULL DEFAULT '0' COMMENT '父节点id' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`username`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户名' ,
`isdone`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '状态' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='论坛表'
AUTO_INCREMENT=1609987952877
ROW_FORMAT=DYNAMIC
;DROP TABLE IF EXISTS `messagess`; CREATE TABLE `messagess` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`userid`  bigint(20) NOT NULL COMMENT '留言人id' ,
`username`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户名' ,
`content`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '留言内容' ,
`cpicture`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '留言图片' ,
`reply`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '回复内容' ,
`rpicture`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '回复图片' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='在线留言'
AUTO_INCREMENT=1629368316361
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `exampaper`; CREATE TABLE `exampaper` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`name`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试卷名称' ,
`time`  int(11) NOT NULL COMMENT '等级测试时长(分钟)' ,
`status`  int(11) NOT NULL DEFAULT 0 COMMENT '测试卷状态' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='测试卷表'
AUTO_INCREMENT=1637647520800
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `examquestion`; CREATE TABLE `examquestion` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`paperid`  bigint(20) NOT NULL COMMENT '所属测试卷id（外键）' ,
`papername`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试卷名称' ,
`questionname`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试卷试题名称' ,
`options`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '选项，json字符串' ,
`score`  bigint(20) NULL DEFAULT 0 COMMENT '分值' ,
`answer`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '正确答案' ,
`analysis`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '答案解析' ,
`type`  bigint(20) NULL DEFAULT 0 COMMENT '测试卷试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空）' ,
`sequence`  bigint(20) NULL DEFAULT 100 COMMENT '测试卷试题排序，值越大排越前面' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='测试卷试题'
AUTO_INCREMENT=1637570384253
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `examrecord`; CREATE TABLE `examrecord` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`username`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户名' ,
`paperid`  bigint(20) NOT NULL COMMENT '测试卷id（外键）' ,
`papername`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试卷名称' ,
`questionid`  bigint(20) NOT NULL COMMENT '测试卷试题id（外键）' ,
`questionname`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试卷试题名称' ,
`options`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '选项，json字符串' ,
`score`  bigint(20) NULL DEFAULT 0 COMMENT '分值' ,
`answer`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '正确答案' ,
`analysis`  longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '答案解析' ,
`myscore`  bigint(20) NOT NULL DEFAULT 0 COMMENT '测试卷试题得分' ,
`myanswer`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '考生答案' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='等级测试记录表'
AUTO_INCREMENT=1637647395617
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `config`;CREATE TABLE `config` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '配置参数名称',
  `value` varchar(100) DEFAULT NULL COMMENT '配置参数值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='配置文件';INSERT INTO `config` VALUES(null,'genImg/1757490928266.png','http://oss.fuqixuan.top/genImg/1757490928266.png');DROP TABLE IF EXISTS `token`; CREATE TABLE `token` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`username`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户名' ,
`tablename`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '表名' ,
`role`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '角色' ,
`token`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间' ,
`expiratedtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '过期时间' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='token表'
AUTO_INCREMENT=11
ROW_FORMAT=DYNAMIC
;
DROP TABLE IF EXISTS `users`; CREATE TABLE `users` (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`username`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户名' ,
`password`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码' ,
`role`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '管理员' COMMENT '角色' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间' ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='用户表'
AUTO_INCREMENT=2
ROW_FORMAT=DYNAMIC
;
INSERT INTO `users` VALUES ('1', 'admin', 'admin', '管理员', '2025-03-20 10:41:27');DROP TABLE IF EXISTS `jiaoshi`; CREATE TABLE jiaoshi( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,yonghuming  varchar(200) COMMENT '用户名',mima  varchar(200) COMMENT '密码',xingbie  varchar(200) COMMENT '性别',dianhua  varchar(200) COMMENT '电话',nicheng  varchar(200) COMMENT '昵称',money  float NULL DEFAULT 0 COMMENT '余额',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
COMMENT='教师';DROP TABLE IF EXISTS `xuesheng`; CREATE TABLE xuesheng( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,yonghuming  varchar(200) COMMENT '用户名',touxiang  varchar(200) COMMENT '头像',mima  varchar(200) COMMENT '密码',xingbie  varchar(200) COMMENT '性别',dianhua  varchar(200) COMMENT '电话',nicheng  varchar(200) COMMENT '昵称',rlimg  longtext COMMENT '人脸图片',isws int(11)  NULL DEFAULT 0 COMMENT '是否完善',money  float NULL DEFAULT 0 COMMENT '余额',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
COMMENT='学生';DROP TABLE IF EXISTS `Discusskechengxinxi`; CREATE TABLE Discusskechengxinxi (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`refid`  bigint(20) NOT NULL COMMENT '关联表id' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`nickname` varchar(200)   DEFAULT NULL COMMENT '用户名' ,
`content` longtext   COMMENT '评论内容' ,
`reply` longtext  COMMENT '回复内容',
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='课程信息评论表'
;
DROP TABLE IF EXISTS `kechengxinxi`; CREATE TABLE kechengxinxi( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,kechengmingcheng  varchar(200) COMMENT '课程名称',tupian  varchar(200) COMMENT '图片',shipin  varchar(200) COMMENT '视频',shangchuanshijian  date COMMENT '上传时间',beizhu  varchar(200) COMMENT '备注',xiangqing  longtext COMMENT '详情', price float NOT NULL  COMMENT '价格',onelimittimes  int(11)  NULL DEFAULT '-1' COMMENT '单限' ,alllimittimes  int(11) NULL DEFAULT '-1' COMMENT '库存',sfsh  varchar(200)  DEFAULT '否' COMMENT '是否审核',shhf  longtext COMMENT '审核回复',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
COMMENT='课程信息';DROP TABLE IF EXISTS `Discusskechengziyuanxinxi`; CREATE TABLE Discusskechengziyuanxinxi (
`id`  bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`addtime`  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,
`refid`  bigint(20) NOT NULL COMMENT '关联表id' ,
`userid`  bigint(20) NOT NULL COMMENT '用户id' ,
`nickname` varchar(200)   DEFAULT NULL COMMENT '用户名' ,
`content` longtext   COMMENT '评论内容' ,
`reply` longtext  COMMENT '回复内容',
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='课程资源信息评论表'
;
DROP TABLE IF EXISTS `kechengziyuanxinxi`; CREATE TABLE kechengziyuanxinxi( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,kechengmingcheng  varchar(200) COMMENT '课程名称',tupian  varchar(200) COMMENT '图片',kechengleixing  varchar(200) COMMENT '课程类型',kechengshipin  varchar(200) COMMENT '课程视频',fujian  varchar(200) COMMENT '附件',shangchuanshijian  datetime COMMENT '上传时间',beizhu  varchar(200) COMMENT '备注',xiangqing  longtext COMMENT '详情',sfsh  varchar(200)  DEFAULT '否' COMMENT '是否审核',shhf  longtext COMMENT '审核回复',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
COMMENT='课程资源信息';DROP TABLE IF EXISTS `kechengleixing`; CREATE TABLE kechengleixing( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,kechengleixing  varchar(200) COMMENT '课程类型',shangchuanshijian  date COMMENT '上传时间',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
COMMENT='课程类型';DROP TABLE IF EXISTS `xuexijihua`; CREATE TABLE xuexijihua( id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',addtime  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ,jihuamingcheng  varchar(200) COMMENT '计划名称',tupian  varchar(200) COMMENT '图片',shangchuanshijian  date COMMENT '上传时间',jihuaxiangqing  longtext COMMENT '计划详情',wanchengzhuangtai  varchar(200) COMMENT '完成状态', userid  bigint(20) COMMENT '用户id',PRIMARY KEY  (id))ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
COMMENT='学习计划';