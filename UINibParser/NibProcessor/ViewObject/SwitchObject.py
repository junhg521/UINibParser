#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/21
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ControlObject import JHControlObject

class JHSwitchObject(JHControlObject):

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=',attribView

		describle = JHControlObject.addViewAttribute(self, classViewName, attribView)
		describle += self.addSwitchAttribute(classViewName, attribView)
		
		return describle

	def addSwitchAttribute(self, classViewName, attribView):
		# print 'attribView=',attribView

		classViewAttrib = self.attribViewTagProperty(attribView)
		describle = ""

		if classViewAttrib.get('onImage','') != "":
			describle += self.setViewProperty(classViewName, "onImage", "[UIImage imageNamed:@"+"\""+classViewAttrib.get('onImage','')+"\""+"]", "")
			pass

		if classViewAttrib.get('offImage','') != "":
			describle += self.setViewProperty(classViewName, "offImage", "[UIImage imageNamed:@"+"\""+classViewAttrib.get('offImage','')+"\""+"]", "")
			pass

		describle += self.setViewProperty(classViewName, "on", classViewAttrib.get('on','YES'), "YES")

		return describle
