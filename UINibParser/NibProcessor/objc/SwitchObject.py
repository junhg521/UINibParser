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

	def addViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=',instanceProperty
		describle = JHControlObject.addViewAttribute(self, instanceTag, instanceProperty)
		describle += self.addSwitchAttribute(instanceTag, instanceProperty)
		return describle

	def addSwitchAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=',instanceProperty
		describle = ""

		if instanceProperty.get('onImage','') != "":
			describle += self.setViewProperty(instanceTag, "onImage", "[UIImage imageNamed:@"+"\""+instanceProperty.get('onImage','')+"\""+"]", "")
			pass

		if instanceProperty.get('offImage','') != "":
			describle += self.setViewProperty(instanceTag, "offImage", "[UIImage imageNamed:@"+"\""+instanceProperty.get('offImage','')+"\""+"]", "")
			pass

		describle += self.setViewProperty(instanceTag, "on", instanceProperty.get('on','YES'), "YES")
		return describle
