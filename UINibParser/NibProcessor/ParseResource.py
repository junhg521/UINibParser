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

from Processor import JHObjcProcessor

class JHBaseParser(object):
	"define the attributes and interfaces required to parse a commom resource file"

	__slots__ = ('resourceFileName', 'className')
	
	def __init__(self, resource_file_name):
		""" use the constructor to initialize the parser properties
		args:
			resource_file_name:parse name of resource file（such as *.xib or *.storyboard）
		properties:
			resourceFileName:recevied file name
			className:the class name of xib file name,you can get the value from 
				customClass node of xib file, the initial vaule is empty
		"""
		self.resourceFileName = resource_file_name
		self.className = ""
		pass

	def parse(self):
		""" define a common parse nib method, subClass can rewrite this method to parse
		a specific file.
		"""
		pass

class JHXibParser(JHBaseParser):
	"extract the nodes in the parsed file into attributes of JHXibParser class"
	
	def __init__(self, resource_file_name, needloadConfiguration):
		""" use the constructor to initialize the xib parser properties
		args:
			resource_file_name:parse name of resource file（such as *.xib）
		properties:
			outletViews:gets all node vaules of `outlet` node in xib file.
				(such as [{'destination':'','property':'','id':''},{...},...])
			attribViews:gets all node values of all `view` node in xib file.
				(such as [{'subviews':[{...}...]},{...},...])
			resources:gets all node values of `resource` node in xib file.(such as {{...},...})
			needloadConfiguration:indicates whether an alternate function for awakeFromNib neends to be loaded
			parseType:xib file type, default value is controller
			viewId: it's controller main view identify
			resources: related information of image
		"""
		JHBaseParser.__init__(self, resource_file_name)
		self.outletViews = []
		self.attribViews = []
		self.resources = []
		self.needloadConfiguration = needloadConfiguration
		self.parseType = "controller"
		self.viewId = ""
		self.resources = []
		pass

	def parse(self):
		""" resolve the node named `objects` and `resources` under file named (*.xib) and
		bind data to the corresponding properties of JHXibParser class
		"""
		try:
			tree = ElementTree.parse(self.resourceFileName)
		except Exception as e:
			print "can\'t parse resource file name:"+self.resourceFileName+",please make user load right resource file name"
			sys.exit(1)
			raise
		else:
			root = tree.getroot()
			objects = root.findall('objects')
			self.parseObjectsNode(list(objects))

			resourceObject = root.findall('resources')
			self.parseResourcesNode(list(resourceObject))
		finally:
			pass
		pass

	def parseResourcesNode(self, resourecObjects):
		"""
		args:
			resourecObjects:
		"""
		for element in resourecObjects:
			pass
		pass

	def parseObjectsNode(self, resourecObjects):
		"""
		args:parse `object` node
			resourecObjects:lists all nodes under the objects node and resolves them, you can
		get the class name of current xib file from the `customClass` node under the `objects` node
		"""
		for element in resourecObjects:
			for subElememt in element:
				# print 'list=', list(subElememt)
				if subElememt.tag == 'placeholder':
					self.parsePlaceholderObjectNode(list(subElememt))
					if subElememt.attrib.get('placeholderIdentifier','') == 'IBFilesOwner':
						if len(self.viewId):
							self.getParseClassName('controller', subElememt.attrib)
							pass
						else:
							self.getParseClassName('view', subElememt.attrib)
							pass
						pass
					pass
				else:
					self.getParseClassName(subElememt.tag, subElememt.attrib)
					otherAttrib = self.parseViewNode(list(subElememt))
					attribView = self.loadParseAttribute(subElememt.tag, subElememt.attrib, otherAttrib)
					self.attribViews.append(attribView)
					pass
			pass
		# print 'className=', self.className
		# print "attribView=", self.attribViews
		pass

	def loadParseAttribute(self, elementTag, elementAttrib, elementOtherAttrib):
		attribView = {}
		attrib = elementAttrib
		attrib.update(elementOtherAttrib)
		attribView[elementTag] = attrib
		return attribView

	def getParseClassName(self, attribTag, attribView):
		""" set parse type and class name
		arg:
			attribTag:resolve the type of node, there are controller、view、collectionReusableView、tableViewCell、collectionViewCell five types
			attribView:attibute of node
		"""
		if len(attribView.get('customClass', '')):
			customClass = attribView.get('customClass', '')
			if len(self.className) == 0:
				self.parseType = attribTag
				self.className = attribView.get('customClass', '')
				pass
			elif self.className == customClass:
				self.parseType = attribTag
			else:
				pass
			pass
		pass

	def parsePlaceholderObjectNode(self, resourecObjects):
		""" parses data of `placeholder` node under `objects` node and assigned to `outletViews` 
		property of `JHXibParser` class
		"""
		for element in resourecObjects:
			for subElement in list(element):
				if subElement.tag == 'outlet':
					self.rootViewID(subElement.attrib)
					self.outletViews.append(subElement.attrib)
				pass
			pass
		# print 'outletViews=', self.outletViews
		pass

	def rootViewID(self, attribView):
		if attribView.get('property', '') == 'view':
			self.viewId = attribView.get('destination', '')
		pass

	def parseViewNode(self, resourecViewObject):
		""" parses data of `tableViewCell` node under `objects` node and assigned to `attribViews` 
		property of `JHXibParser` class
		args:
			resourecObjects: all nodes of `tableViewCell` node
		"""
		attribView = {}
		for element in resourecViewObject:
			if element.tag == 'tableViewCellContentView' or (element.tag == "view" and element.attrib.get('key', '') == "contentView"):
				contentViewSubAttribute = self.parseViewNode(list(element))
				contentViewAttribute = self.loadParseAttribute(element.tag, element.attrib, contentViewSubAttribute)
				subAttribViews = []
				subAttribViews.append(contentViewAttribute)
				attribView['subviews'] = subAttribViews
				pass
			elif element.tag == 'subviews':
				attribView[element.tag] = self.parseSubViewsNode(list(element))
				# print 'subviews =', attribView[element.tag]
				pass
			elif element.tag == 'constraints':
				attribView[element.tag] = self.parseViewListPropertyNode(list(element))
				# print 'attributedString =', attribView[element.tag]
				pass
			elif element.tag == 'attributedString':
				attribView[element.tag] = self.parseAttributeStringNode(list(element))
				# print 'attributedString =', attribView[element.tag]
				pass
			elif element.tag == 'connections':
				attribView[element.tag] = self.parseViewListPropertyNode(list(element))
				# print 'attributedString =', attribView[element.tag]
				pass
			elif element.tag == 'collectionViewFlowLayout':
				attribView[element.tag] = self.parsecollectionViewFlowLayoutNode(list(element),element.tag, element.attrib)
				# print 'attributedString =', attribView[element.tag]
				pass
			elif element.tag == 'state':
				states = {}
				states[element.tag] = element.attrib
				states.update(self.parseViewNode(list(element)))
				self.parseViewPropetyNode(attribView, 'states', states)
				pass
			elif element.tag == 'userDefinedRuntimeAttributes':
				attribView[element.tag] = self.parseViewListContainObjectPropertyNode(list(element))
				pass
			else:
				self.parseViewPropetyNode(attribView, element.tag, element.attrib)
			pass

		return attribView

	def parseSubViewsNode(self, resourceObjects):
		""" parse `subviews` node 
		"""
		allAttribViews = []
		for element in resourceObjects:
			otherAttrib = self.parseViewNode(list(element))
			attribView = self.loadParseAttribute(element.tag, element.attrib, otherAttrib)
			allAttribViews.append(attribView)
			pass
		return allAttribViews

	def parseViewPropetyNode(self, attribView, viewTag, viewValue):

		if attribView.has_key(viewTag):
			# print 'viewTag=',viewTag,'attribView=',attribView
			sameElement = attribView.get(viewTag)
			if type(sameElement) == list:
				sameElement.append(viewValue)
				pass
			elif type(sameElement) == dict:
				theSameElement = []
				theSameElement.append(sameElement)
				theSameElement.append(viewValue)
				attribView[viewTag] = theSameElement
				pass
			else:
				pass
			pass
		else:
			attribView[viewTag] = viewValue
			pass
		pass

	def parseViewListPropertyNode(self, resourceObjects):
		# 解析Ojbect的约束
		properties = []
		for element in resourceObjects:
			viewProperty = {}
			viewProperty[element.tag] = element.attrib
			if element.tag == 'outlet':
				self.outletViews.append(element.attrib)
				pass
			properties.append(viewProperty)
			pass
		return properties

	def parseAttributeStringNode(self, resourceObjects):
		# 解析UILable的AttributeString属性
		attributeStrings = []
		for element in resourceObjects:
			attributedContent = {}
			attributedContent[element.tag] = element.attrib
			attributedString = self.parseAttributeStringNode(list(element))
			for attribute in attributedString:
				attributedContent.update(attribute)
				pass
				
			attributeStrings.append(attributedContent)
			pass
		
		return attributeStrings

	def parsecollectionViewFlowLayoutNode(self, resourceObjects, tag, attrib):
		""" 
		"""
		element = {}
		element[tag] = attrib
		propertyElement = {}
		propertyElement['property'] = self.parseViewNode(resourceObjects)
		element.update(propertyElement)
		return element

	def parseViewListContainObjectPropertyNode(self, resourceObjects):
		properties = []
		for element in resourceObjects:
			viewProperty = {}
			viewProperty[element.tag] = element.attrib
			viewProperty.update(self.parseViewNode(list(element)))
			properties.append(viewProperty)
			pass
		return properties
# exec

if __name__ == '__main__':
	parser = JHXibParser(sys.argv[1], sys.argv[2])
	parser.parse()

	processor = JHObjcProcessor(parser)
	sys.exit(processor.processing())
	
