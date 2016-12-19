#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/11/1
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ScrollViewObject import JHScrollViewObject

class JHTableViewObject(JHScrollViewObject):

	def addSubview(self, instanceTag, instanceProperty, classMethodName):
		# print 'attribView=', attribView
		classViewName = self.attribViewInstanceName(instanceTag, instanceProperty)
		classType = self.instanceClassNameType(instanceTag, instanceProperty)
		describle = self.addClassMethodName(classType, classMethodName)
		frame = self.getClassFrame(instanceProperty.get('rect', {}))
		style = self.getTableViewStyle(instanceProperty.get('style','UITableViewStylePlain'))
		describle += self.loadSyntaxWithLineFeedAndSingleSpace(classType+"* "+classViewName+" = [["+classType+" alloc] initWithFrame:"+frame+" style:"+style+"];")
		describle += self.addViewAttribute(classViewName, instanceProperty)
		return describle

	def addViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=', instanceProperty
		describle = JHScrollViewObject.addViewAttribute(self, instanceTag, instanceProperty)
		describle += self.addTableViewAttribute(instanceTag, instanceProperty)
		return describle

	def addTableViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=', instanceProperty
		describle = self.setViewProperty(instanceTag, 'separatorStyle', self.getTableViewCellSeparatorStyle(instanceProperty.get('separatorStyle', 'styleSingleLine')), 'UITableViewCellSeparatorStyleSingleLine')
		describle += self.setViewProperty(instanceTag, 'sectionHeaderHeight', instanceProperty.get('sectionHeaderHeight', '0'), '0')
		describle += self.setViewProperty(instanceTag, 'sectionFooterHeight', instanceProperty.get('sectionFooterHeight', '0'), '0')
		describle += self.setViewProperty(instanceTag, 'rowHeight', instanceProperty.get('rowHeight', '0'), '0')
		return describle

			
