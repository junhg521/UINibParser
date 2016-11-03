#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/27
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHControlObject(JHViewObject):
	def __init__(self):
			pass

	def __del__(self):
			pass

	def addSubview(self, attribView):
		# print 'attribView=', attribView
		return ""

	def addControlAttribute(self, attribView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		
		describle = JHViewObject.addViewAttribute(attribView)
		if attribView.get('contentVerticalAlignment', 'center') != 'center':
			describle +="	self.view.contentVerticalAlignment = "+self.getControlContentVerticalAlignment(attribView.get('contentVerticalAlignment', 'center'))+";\n"
			pass
		
		if attribView.get('contentHorizontalAlignment', 'center') != 'center':
			describle +="	self.view.contentHorizontalAlignment = "+self.getControlContentHorizontalAlignment(attribView.get('contentHorizontalAlignment', 'center'))+";\n"
			pass

		for connection in attribView.get('connections', {}):
			action = connection.get('action', {})
			if action.has_key('selector') and action.has_key('eventType'):
				describle +="	["+classViewName+" addTarget:self action:@selector("+action.get('selector','')+") forControlEvents:+"+self.getControlEvent(action.get('eventType', 'touchUpInside'))+"];\n"
				pass
			pass

		return describle
