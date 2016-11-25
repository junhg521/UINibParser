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
	def __init__(self):
		pass

	def __del__(self):
		pass

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView
		
		describle = JHControlObject.addViewAttribute(self, classViewName, attribView)
		describle += self.getTextFieldViewAttribute(classViewName, attribView)

		return describle

	def getTextFieldViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView
		
		classViewAttrib = self.attribViewTagProperty(attribView)
		describle = ""
		if classViewAttrib.get('background','').encode('utf-8') != '':
			describle += self.setViewProperty(classViewName, "background", "[UIImage imageNamed:@"+"\""+classViewAttrib.get('background','').encode('utf-8')+"\""+"]", "")
			pass
			
		if classViewAttrib.get('disabledBackground','').encode('utf-8') != '':
			describle += self.setViewProperty(classViewName, "disabledBackground", "[UIImage imageNamed:@"+"\""+classViewAttrib.get('disabledBackground','').encode('utf-8')+"\""+"]", "")
			pass

		describle += self.setViewProperty(classViewName, "placeholder", "@"+"\""+classViewAttrib.get('placeholder','').encode('utf-8')+"\"", "")
		describle += self.setViewProperty(classViewName, "text", "@"+"\""+classViewAttrib.get('text','').encode('utf-8')+"\"", "")
		describle += self.setViewProperty(classViewName, "font", self.getTextFont(attribView.get('fontDescription')), "")
		describle += self.setViewProperty(classViewName, "borderStyle", self.getTextBorderStyle(classViewAttrib.get('borderStyle', 'none')), "UITextBorderStyleNone")
		describle += self.setViewProperty(classViewName, "clearButtonMode", self.getTextFieldViewMode(classViewAttrib.get('clearButtonMode', 'never')), "UITextFieldViewModeNever")
		describle += self.setViewProperty(classViewName, "leftViewMode", self.getTextFieldViewMode(classViewAttrib.get('leftViewMode', 'never')), "UITextFieldViewModeNever")
		describle += self.setViewProperty(classViewName, "rightViewMode", self.getTextFieldViewMode(classViewAttrib.get('rightViewMode', 'never')), "UITextFieldViewModeNever")

		return describle
		