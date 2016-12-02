#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/18
# version: 0.0.1
# author: Junhg
# contribute:
# 

try:
	import xml.etree.cElementTree as ElementTree
except ImportError:
	import xml.etree.ElementTree as ElementTree
finally:
	pass

import sys
import os
import commands
from ViewObject.CommonObject import JHCommomObject
from Processor import JHObjcProcessor

class JHBaseParser():
	'定义通用的接口'
	# 描述: 采用构造函数初始化解析器属性
	# propety:
	#	__resourceFileName: 私有变量，解析的文件名
	#	className: 实现类名,字符换类型（如"TestViewController"
	def __init__(self,resource_file_name):
		self.resourceFileName = resource_file_name
		self.className = ""
	
	def __del__(self):
		pass

	def parse(self):
		pass

	def resourceFileDir(self):
		index = self.resourceFileName.find(self.className)
		
		if index > 1:
			file_dir = self.resourceFileName[0:index]
			return file_dir
			pass
		return ""
		pass
	

class JHNibParser(JHBaseParser, JHCommomObject):
	'解析xib文件，将xib中的资源抽离到实现文件中'
	
	# 描述：	采用构造函数初始化该解析器
	# 		将__resourceFileName文件的资源文件中的试图解析到属性变量中
	# propety:
	#	outletViews:xib所持有的outlet变量，数组类型
	#   如下列的所示：[{'destination': 'Jfs-zd-G9X', 'property': 'bottomView', 'id': 'Net-4U-kRv'},
	#    {'destination': 'i5M-Pr-FkT', 'property': 'view', 'id': 'VQG-gN-rva'}]
	#   attribViews:xib所持有的控件属性，数组类型
	#	如下列的所示：[{'subviews':[{'autoresizingMask':{'flexibleMaxY':'YES','key':'autoresizingMask','flexibleMaxX':'YES'},'color':{'blue':'0.27450980390000002','colorSpace':'calibratedRGB','green':'0.75294117650000003','key':'backgroundColor','alpha':'1','red':'1'},'frame':{'minY':'79','height':'128','key':'frameInset','width':'375'},'view':{'fixedFrame':'YES','translatesAutoresizingMaskIntoConstraints':'NO','contentMode':'scaleToFill','id':'Jfs-zd-G9X'}},],
	#				'point':{'y':'51.5','x':'25.5','key':'canvasLocation'},'color':{'blue':'1','colorSpace':'custom','green':'1','key':'backgroundColor','alpha':'1','customColorSpace':'sRGB','red':'1'},'autoresizingMask':{'heightSizable':'YES','widthSizable':'YES','key':'autoresizingMask'},'rect':{'y':'0.0','x':'0.0','height':'667','key':'frame','width':'375'},'view':{'clearsContextBeforeDrawing':'NO','contentMode':'scaleToFill','id':'i5M-Pr-FkT'}}]
	def __init__(self, resource_file_name):
		JHBaseParser.__init__(self,resource_file_name)
		self.outletViews = []
		self.attribViews = []
		pass
	
	def __del__(self):
		pass

	# 描述：解析资源文件，将相关的属性字段通过fileHandleManager写到文件中
	def parse(self):
		try:
			tree = ElementTree.parse(self.resourceFileName)
			root = tree.getroot()
		except Exception as e:
			print 'can not parse resource file name:', self.resourceFileName, 'please make user load right resource file name' 
			sys.exit(1)
			raise
		else:
			pass
		finally:
			pass

		resourecObject = root.findall('objects')
		self.parseResourceObjectNode(resourecObject)

	def parseResourceObjectNode(self,resourecObject):
		# 罗列出resourecObject中的objects
		for element in list(resourecObject):
			for subElememt in element:
				# print 'list=', list(subElememt)
				if subElememt.tag == 'view':
					attribView = {}
					attribView[subElememt.tag] = subElememt.attrib
					self.attribViews.append(self.parseResourceViewObjectNode(list(subElememt), attribView))
					# print 'attribView=', self.attribViews
					pass
				elif subElememt.tag == 'placeholder':
					if subElememt.attrib.get('placeholderIdentifier','') == 'IBFilesOwner':
						self.className = subElememt.attrib.get('customClass', '')
						pass
					self.parseResourcePlaceholderObjectNode(list(subElememt))
					pass
				else:
					# 暂时在xib中未发现存在的类型，直接过滤掉
					pass
			pass
		# print 'className=', self.className
		pass

	def parseResourcePlaceholderObjectNode(self, resourecObject):
		for element in resourecObject:
			for subElement in list(element):
				if subElement.tag == 'outlet':
					self.outletViews.append(subElement.attrib)
				pass
			
			pass
		# print 'outletViews=', self.outletViews
		pass

	def parseResourceViewObjectNode(self, resourecViewObject, objectViewAttrib):
		# 解析xib上的view及subViews
		attribView = objectViewAttrib
		for element in resourecViewObject:
			if element.tag == 'subviews':
				# print 'tag=',element.tag, 'resourecObject=',list(element), 'element=',element
				attribView[element.tag] = self.parseResourceSubViewObjectNode(list(element))
				pass
			elif element.tag == 'constraints':
				attribView[element.tag] = self.parseResourceConstraintObjectNode(list(element))
				pass
			elif element.tag == 'attributedString':
				attribView[element.tag] = self.parseResourceAttributeStringObjectNode(list(element))
				# print 'attributedString =', attribView[element.tag]
			else :
				# 对属性做特殊处理，UILabel的Color
				if element.tag == 'color':
					attribView[element.attrib['key']] = element.attrib
				else :
					attribView[element.tag] = element.attrib
				pass
			pass

		return attribView

	def parseResourceSubViewObjectNode(self, resourecObject):
		# 解析view上的subView
		allAttribViews = []
		for element in resourecObject:
			# print 'tag=',element.tag, 'attrib=', list(element)
			if self.judgementViewTag(element.tag):
				attribView = {}
				attribView[element.tag] = element.attrib
				# 添加element.tag下的其他属性
				allAttribViews.append(self.parseResourceViewObjectNode(list(element), attribView))
				pass
			pass
		return allAttribViews

	def parseResourceConstraintObjectNode(self, resourecObject):
		# 解析Ojbect的约束
		allConstraints = []
		for element in resourecObject:
			constraint = {}
			constraint[element.tag] = element.attrib
			allConstraints.append(constraint)
			pass
		return allConstraints

	def parseResourceAttributeStringObjectNode(self, resourecObject):
		# 解析UILable的AttributeString属性
		allAttributeString = []
		for element in resourecObject:
			attributedContent = {}
			attributedContent[element.tag] = element.attrib
			attributedString = self.parseResourceAttributeStringObjectNode(list(element))
			for attribute in attributedString:
				attributedContent.update(attribute)
				pass
				
			allAttributeString.append(attributedContent)
			pass
			
		# print 'allAttributeString=',allAttributeString
		return allAttributeString

# exec

if __name__ == '__main__':
	# 解析nib文件
	nibParser = JHNibParser(*sys.argv[1:])
	nibParser.parse()

	# processor解析后的属性
	processor = JHObjcProcessor(nibParser)
	processor.processing()
