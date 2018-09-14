#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
from urllib import parse
import json

if __name__ == '__main__':
	request_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	
	Form_Data = {}
	Form_Data['type'] = 'AUTO'
	Form_Data['i'] = 'Jack'
	Form_Data['doctype'] = 'json'
	Form_Data['xmlVersion'] = '1.8'
	Form_Data['keyfrom'] = 'fanyi.web'
	Form_Data['ue'] = 'ue:UTF-8'
	Form_Data['action'] = 'FY_BY_CLICKBUTTON'
	#使用urlencode方法转换标准格式
	data = parse.urlencode(Form_Data).encode('utf-8')
	#传递Request对象和转换完格式的数据
	response = request.urlopen(request_url,data)
	#读取信息并解码
	html = response.read().decode('utf-8')
	#使用JSON
	translate_results = json.loads(html)
	#找到翻译结果
	translate_results = translate_results['translateResult'][0][0]['tgt']
	#打印翻译信息
	print("翻译的结果是：%s" % translate_results)