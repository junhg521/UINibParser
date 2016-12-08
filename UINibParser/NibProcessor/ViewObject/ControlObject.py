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

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		describle = JHViewObject.addViewAttribute(self, classViewName, attribView)
		describle += self.addControlViewAttribute(classViewName, attribView)

		return describle

	def addControlViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		attribViewId = self.attribViewTagProperty(attribView)
		describle = self.setViewProperty(classViewName, 'contentVerticalAlignment', self.getControlContentVerticalAlignment(attribViewId.get('contentVerticalAlignment', {})), 'UIControlContentVerticalAlignmentCenter')
		describle += self.setViewProperty(classViewName, 'contentHorizontalAlignment', self.getControlContentHorizontalAlignment(attribViewId.get('contentHorizontalAlignment', {})),'UIControlContentHorizontalAlignmentCenter')
		
		if attribView.has_key('connections'):
			if type(attribView.get('connections')) == list:
				for connection in attribView.get('connections', []):
					describle += self.setControlConnectionInfos(classViewName, connection)
					pass
				pass
			elif type(attribView.get('connections')) == dict:
				describle += self.setControlConnectionInfos(classViewName, attribView.get('connections', {}))
				pass
			else:
				pass
			pass

		return describle

	def setControlConnectionInfos(self, classViewName, connection):
		describle = ""
		action = connection.get('action', {})
		if len(action):
			describle += self.loadSyntaxWithLineFeedAndSingleSpace("["+classViewName+" addTarget:self action:@selector("+action.get('selector','')+") forControlEvents:"+self.getControlEvent(action.get('eventType', 'touchUpInside'))+"];")
			pass

		return describle

	def setControlStateProperty(self, classViewName, setControlPropertyName, controlProperty, controlState):
		describle = self.loadSyntaxWithLineFeedAndSingleSpace("["+classViewName+" "+ setControlPropertyName+":"+controlProperty+" forState:"+controlState+"];")
		return describle	

