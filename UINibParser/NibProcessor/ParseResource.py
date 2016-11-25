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
	'定义解析通用资源文件所需要的属性及接口'
	# 描述: 采用构造函数初始化解析器属性
	# propety:
	#	__resourceFileName: 私有变量，解析的文件名
	#	className: 实现类名,字符换类型（如"TestUIViewViewController"
	def __init__(self, resource_file_name):
		self.resourceFileName = resource_file_name
		self.className = ""

	def parse(self):
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
	def __init__(self, resource_file_name, needloadConfiguration):
		JHBaseParser.__init__(self, resource_file_name)
		self.outletViews = []
		self.attribViews = []
		self.resources = []
		self.needloadConfiguration = needloadConfiguration
		self.parseType = "controller"
		pass

	# 描述：解析资源文件，将相关的属性字段通过fileHandleManager写到文件中
	def parse(self):
		try:
			tree = ElementTree.parse(self.resourceFileName)
		except Exception as e:
			print 'can not parse resource file name:', self.resourceFileName, 'please make user load right resource file name' 
			sys.exit(1)
			raise
		else:
			root = tree.getroot()
			nibObject = root.findall('objects')
			self.parseNibObjectNode(nibObject)

			resourceObject = root.findall('resources')
			self.parseResourceObjectNode(resourceObject)
			pass
		finally:
			pass

	def parseResourceObjectNode(self, resourecObject):
		for element in list(resourecObject):
			pass
		pass

	def parseNibObjectNode(self, resourecObject):
		# 罗列出resourecObject中的objects
		for element in list(resourecObject):
			for subElememt in element:
				# print 'list=', list(subElememt)
				if subElememt.tag == 'view':
					# 处理普通的controller的xib类型
					customClass = subElememt.attrib.get('customClass', '')
					if len(customClass) > 0:
						self.parseType = 'parseOther'
						self.className = customClass
						pass
					else:
						self.parseType = 'controller'
						pass
					
					attribView = self.parseResourceViewObjectNode(list(subElememt))
					attribView[subElememt.tag] = subElememt.attrib
					self.attribViews.append(attribView)
					# print 'attribView=', self.attribViews
					pass
				elif subElememt.tag == 'placeholder':
					# 处理获取controller的类名
					if subElememt.attrib.get('placeholderIdentifier','') == 'IBFilesOwner':
						self.className = subElememt.attrib.get('customClass', '')
						pass
					self.parseResourcePlaceholderObjectNode(list(subElememt))
					pass
				elif subElememt.tag == 'tableViewCell':
					self.parseType = "tableViewCell"
					self.className = subElememt.attrib.get('customClass', '')
					# 处理UITableViewCell的xib类型
					attribView = self.parseResourceTableContentViewWithViewTag(list(subElememt),'tableViewCellContentView')
					attribView[subElememt.tag] = subElememt.attrib
					self.attribViews.append(attribView)
					# print 'attribView=', self.attribViews
					pass
				elif subElememt.tag == 'collectionReusableView':
					self.parseType = 'collectionReusableView'
					self.className = subElememt.attrib.get('customClass', '')
					# 处理UICollectionReusableView的xib类型
					attribView = self.parseResourceViewObjectNode(list(subElememt))
					attribView[subElememt.tag] = subElememt.attrib
					self.attribViews.append(attribView)
					# print 'attribView=', self.attribViews
					pass
				elif subElememt.tag == 'collectionViewCell':
					self.parseType = 'collectionViewCell'
					self.className = subElememt.attrib.get('customClass', '')
					# 处理UICollectionViewCell的xib类型
					attribView = self.parseResourceCollectionContentView(list(subElememt),'view', subElememt.attrib.get('id',''))
					attribView[subElememt.tag] = subElememt.attrib
					self.attribViews.append(attribView)
					# print 'attribView=', self.attribViews
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

	def parseResourceTableContentViewWithViewTag(self, resourecViewObject, viewTag):
		attribView = {}
		for element in resourecViewObject:
			if element.tag == viewTag:
				subAttribViews = []
				contentViewAttribute = {}
				contentViewAttribute[element.tag] = element.attrib
				contentViewAttribute.update(self.parseResourceViewObjectNode(list(element)))
				subAttribViews.append(contentViewAttribute)
				attribView['subviews'] = subAttribViews
				pass
			elif element.tag == 'connections':
				attribView[element.tag] = self.parseResoureConnectionsObjectNode(list(element))
				pass
			elif element.tag == 'constraints':
				attribView[element.tag] = self.parseResourceConstraintObjectNode(list(element))
				# print 'attributedString =', attribView[element.tag]
				pass
			else:
				attribView[element.tag] = element.attrib
				pass
			pass

		return attribView

	def parseResourceCollectionContentView(self, resourecViewObject, viewTag, parentId):
		attribView = {}
		constraints = []
		contentView = {}
		for element in resourecViewObject:
			if element.tag == viewTag:
				element.attrib['id'] = parentId
				contentView[element.tag] = element.attrib
				contentView.update(self.parseResourceViewObjectNode(list(element)))
				
				subAttribViews = []
				subAttribViews.append(contentView)
				attribView['subviews'] = subAttribViews
				pass
			elif element.tag == 'connections':
				attribView[element.tag] = self.parseResoureConnectionsObjectNode(list(element))
				pass
			elif element.tag == 'constraints':
				constraints = self.parseResourceConstraintObjectNode(list(element))
				# print 'attributedString =', attribView[element.tag]
				pass
			else:
				attribView[element.tag] = element.attrib
				pass
			pass

		contentView['constraints'] = constraints

		return attribView

	def parseResourceViewObjectNode(self, resourecViewObject):
		# 解析xib上的view及subViews
		attribView = {}
		for element in resourecViewObject:
			if element.tag == 'subviews':
				attribView[element.tag] = self.parseResourceSubViewObjectNode(list(element))
				# print 'tag=',element.tag, 'resourecObject=',list(element), 'element=',element
				# print 'subviews =', attribView[element.tag]
				pass
			elif element.tag == 'constraints':
				attribView[element.tag] = self.parseResourceConstraintObjectNode(list(element))
				# print 'attributedString =', attribView[element.tag]
				pass
			elif element.tag == 'attributedString':
				attribView[element.tag] = self.parseResourceAttributeStringObjectNode(list(element))
				# print 'attributedString =', attribView[element.tag]
				pass
			elif element.tag == 'connections':
				attribView[element.tag] = self.parseResoureConnectionsObjectNode(list(element))
				# print 'attributedString =', attribView[element.tag]
				pass
			elif element.tag == 'collectionViewFlowLayout':
				attribView[element.tag] = self.parsecollectionViewFlowLayoutObjectNode(list(element),element.tag, element.attrib)
				# print 'attributedString =', attribView[element.tag]
				pass
			else:
				# 处理含有相同的tag字段
				if attribView.has_key(element.tag):
					# print 'element.tag=',element.tag,'attribView=',attribView
					sameElement = attribView.get(element.tag)
					if type(sameElement) == list:
						sameElement.append(element.attrib)
						pass
					elif type(sameElement) == dict:
						theSameElement = []
						theSameElement.append(sameElement)
						theSameElement.append(element.attrib)
						attribView[element.tag] = theSameElement
						pass
					else:
						pass
					pass
				else:
					attribView[element.tag] = element.attrib
					pass
				pass
			pass

		return attribView

	def parseResourceSubViewObjectNode(self, resourecObject):
		# 解析view上的subView
		allAttribViews = []
		for element in resourecObject:
			# print 'tag=',element.tag, 'attrib=', list(element)
			if self.judgementViewTag(element.tag):
				attribView = self.parseResourceViewObjectNode(list(element))
				attribView[element.tag] = element.attrib
				# 添加element.tag下的其他属性
				allAttribViews.append(attribView)
				pass
			pass
		return allAttribViews

	def parseResourceConstraintObjectNode(self, resourecObject):
		# 解析Ojbect的约束
		constraints = []
		for element in resourecObject:
			constraint = {}
			constraint[element.tag] = element.attrib
			constraints.append(constraint)
			pass
		return constraints

	def parseResourceAttributeStringObjectNode(self, resourecObject):
		# 解析UILable的AttributeString属性
		attributeStrings = []
		for element in resourecObject:
			attributedContent = {}
			attributedContent[element.tag] = element.attrib
			attributedString = self.parseResourceAttributeStringObjectNode(list(element))
			for attribute in attributedString:
				attributedContent.update(attribute)
				pass
				
			attributeStrings.append(attributedContent)
			pass
		
		return attributeStrings

	def parseResoureConnectionsObjectNode(self, resourecObject):
		connections = []
		for element in resourecObject:
			connect = {}
			connect[element.tag] = element.attrib

			# 特殊处理情况
			# 对tableViewCell这类型的IBoutlet放置位置坐处理
			if element.tag == 'outlet':
				self.outletViews.append(element.attrib)
				pass

			connections.append(connect)
			pass
		return connections

	def parsecollectionViewFlowLayoutObjectNode(self, resourecObject, tag, attrib):
		element = {}
		element[tag] = attrib
		propertyElement = {}
		propertyElement['property'] = self.parseResourceViewObjectNode(resourecObject)
		element.update(propertyElement)
		return element
# exec

if __name__ == '__main__':
	# 解析nib文件
	nibParser = JHNibParser(sys.argv[1], sys.argv[2])
	nibParser.parse()

	# processor解析后的属性
	processor = JHObjcProcessor(nibParser)
	processor.processing()
