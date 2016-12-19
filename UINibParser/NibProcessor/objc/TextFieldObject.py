#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/25
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ControlObject import JHControlObject

class JHTextFieldObject(JHControlObject):

	def addViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=', instanceProperty
		
		describle = JHControlObject.addViewAttribute(self, instanceTag, instanceProperty)
		describle += self.getTextFieldViewAttribute(instanceTag, instanceProperty)

		return describle

	def getTextFieldViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=', instanceProperty
		
		describle = ""
		if instanceProperty.get('background','').encode('utf-8') != '':
			describle += self.setViewProperty(instanceTag, "background", "[UIImage imageNamed:@"+"\""+instanceProperty.get('background','').encode('utf-8')+"\""+"]", "")
			pass
			
		if instanceProperty.get('disabledBackground','').encode('utf-8') != '':
			describle += self.setViewProperty(instanceTag, "disabledBackground", "[UIImage imageNamed:@"+"\""+instanceProperty.get('disabledBackground','').encode('utf-8')+"\""+"]", "")
			pass

		describle += self.setViewProperty(instanceTag, "placeholder", "@"+"\""+instanceProperty.get('placeholder','').encode('utf-8')+"\"", "")
		describle += self.setViewProperty(instanceTag, "text", "@"+"\""+instanceProperty.get('text','').encode('utf-8')+"\"", "")
		describle += self.setViewProperty(instanceTag, "font", self.getTextFont(instanceProperty.get('fontDescription')), "")
		describle += self.setViewProperty(instanceTag, "borderStyle", self.getTextBorderStyle(instanceProperty.get('borderStyle', 'none')), "UITextBorderStyleNone")
		describle += self.setViewProperty(instanceTag, "clearButtonMode", self.getTextFieldViewMode(instanceProperty.get('clearButtonMode', 'never')), "UITextFieldViewModeNever")
		describle += self.setViewProperty(instanceTag, "leftViewMode", self.getTextFieldViewMode(instanceProperty.get('leftViewMode', 'never')), "UITextFieldViewModeNever")
		describle += self.setViewProperty(instanceTag, "rightViewMode", self.getTextFieldViewMode(instanceProperty.get('rightViewMode', 'never')), "UITextFieldViewModeNever")

		return describle
		