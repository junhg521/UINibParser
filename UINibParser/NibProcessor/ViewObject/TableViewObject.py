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

	def addSubview(self, classViewName, classMethodName, attribView):
		# print 'attribView=', attribView

		classType = self.objcClassNameType(classViewName)
		attribViewId = self.attribViewTagProperty(attribView)

		describle = self.addClassMethodName(classType, classMethodName)
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax(classType+"* "+classViewName+" = [["+classType+" alloc] initWithFrame:"+self.getClassFrame(attribView.get('rect', {}))+" style:"+self.getTableViewStyle(attribViewId.get('style','UITableViewStylePlain'))+"];")

		return describle

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		describle = JHScrollViewObject.addViewAttribute(self, classViewName, attribView)
		describle += self.addTableViewAttribute(classViewName, attribView)

		return describle

	def addTableViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		attribViewId = self.attribViewTagProperty(attribView)
		describle = self.setViewProperty(classViewName, 'separatorStyle', self.getTableViewCellSeparatorStyle(attribViewId.get('separatorStyle', 'none')), '')
		describle += self.setViewProperty(classViewName, 'sectionHeaderHeight', attribViewId.get('sectionHeaderHeight', '0'), '0')
		describle += self.setViewProperty(classViewName, 'sectionFooterHeight', attribViewId.get('sectionFooterHeight', '0'), '0')
		describle += self.setViewProperty(classViewName, 'rowHeight', attribViewId.get('rowHeight', '0'), '0')
		return describle

			
