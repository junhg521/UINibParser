#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/25
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHTextFieldObject(JHViewObject):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def addSubview(self, attribView, isLoadView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		classViewAttrib = self.attribViewTagProperty(attribView)
		describle = JHViewObject.addSubview(self,attribView,False)
		connections = attribView.get('connections', {})

		if classViewAttrib.has_key('background'):
			describle +="	"+classViewName+".background = [UIImage imageNamed:@"+"\""+classViewAttrib.get('image','')+"\""+"];\n"
			pass

		if classViewAttrib.has_key('disabledBackground'):
			describle +="	"+classViewName+".disabledBackground = [UIImage imageNamed:@"+"\""+classViewAttrib.get('image','')+"\""+"];\n"
			pass

		if attribView.has_key('fontDescription'):
			describle +="	"+classViewName+".font = "+self.getTextFont(attribView.get('fontDescription'))+'\n'
			pass
		
		for connection in connections:
			if connection.has_key('action'):
				action = connection.get('action', {})
				if action.has_key('selector') and action.has_key('eventType'):
					describle +="	["+classViewName+" addTarget:self action:@selector("+action.get('selector','')+") forControlEvents:+"+self.getControlEvent(action.get('eventType', 'touchUpInside'))+"];\n"
					pass
				pass
			pass
		return describle
		