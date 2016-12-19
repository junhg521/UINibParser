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

	def addViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=', instanceProperty
		describle = JHViewObject.addViewAttribute(self, instanceTag, instanceProperty)
		describle += self.addControlViewAttribute(instanceTag, instanceProperty)
		return describle

	def addControlViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=', instanceProperty

		describle = self.setViewProperty(instanceTag, 'contentVerticalAlignment', self.getControlContentVerticalAlignment(instanceProperty.get('contentVerticalAlignment', {})), 'UIControlContentVerticalAlignmentCenter')
		describle += self.setViewProperty(instanceTag, 'contentHorizontalAlignment', self.getControlContentHorizontalAlignment(instanceProperty.get('contentHorizontalAlignment', {})),'UIControlContentHorizontalAlignmentCenter')
		
		if instanceProperty.has_key('connections'):
			if type(instanceProperty.get('connections')) == list:
				for connection in instanceProperty.get('connections', []):
					describle += self.setControlConnectionInfos(instanceTag, connection)
					pass
				pass
			elif type(instanceProperty.get('connections')) == dict:
				describle += self.setControlConnectionInfos(instanceTag, instanceProperty.get('connections', {}))
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

