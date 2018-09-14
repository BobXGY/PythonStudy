#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#jieba库

import jieba


##################################################################
#lcut方法
#	#1精确模式，把文本分开，不产生冗余
print(jieba.lcut("中华人民共和国是一个伟大的国家"))
#	#2全模式，所有可能的词语都扫描出来，可能会有冗余
print(jieba.lcut("中华人民共和国是一个伟大的国家", cut_all=True))

##################################################################
#lcut_for_search方法:搜索引擎模式
print(jieba.lcut_for_search("中华人民共和国是一个伟大的国家"))
