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
		describle += self.setViewProperty(classViewName, 'contentHorizontalAlignment', self.getControlContentHorizontalAlignment(attribViewId.get('contentHorizontalAlignment', {})),'UIControlContentVerticalAlignmentCenter')
		
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

		if attribView.has_key('state'):
			if type(attribView.get('state')) == list:
				for controlState in attribView.get('state', []):
					describle += self.setControlSateInfos(classViewName, controlState)
				pass

			elif type(attribView.get('state')) == dict:
				describle += self.setControlSateInfos(classViewName, attribView.get('state', {}))
				pass
			else:
				pass
			pass

		return describle

	def setControlSateInfos(self, classViewName, controlState):
		# print 'controlState=',controlState
		# print 'title=',controlState.get('title', '').encode('utf-8')
		
		describle = ''
		if controlState.get('title', '') != '':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("["+classViewName+" setTitle:@"+"\""+controlState.get('title', '').encode('utf-8') +"\""+" forState:"+self.getControlState(controlState.get('key','normal'))+"];")
			pass
		if controlState.get('backgroundImage','') != '':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("["+classViewName+" setBackgroundImage:[UIImage imageNamed:@"+"\""+controlState.get('backgroundImage', '').encode('utf-8')+"\""+"] forState:"+self.getControlState(controlState.get('key','normal'))+"];")
			pass
		if controlState.get('image', '') != '':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("["+classViewName+" setImage:[UIImage imageNamed:@"+"\""+controlState.get('image', '').encode('utf-8')+"\""+"] forState:"+self.getControlState(controlState.get('key','normal'))+"];")
			pass

		# describle += JHViewObject.getViewColor(self, classViewName, attribView)
		return describle

	def setControlConnectionInfos(self, classViewName, connection):
		describle = ""
		if connection.has_key('action'):
			action = connection.get('action', {})
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("["+classViewName+" addTarget:self action:@selector("+action.get('selector','')+") forControlEvents:"+self.getControlEvent(action.get('eventType', 'touchUpInside'))+"];")
			pass
		# if connection.has_key('outlet'):
		# 	describle += self.addBlackCharacter()
		# 	describle += self.writeDescribleSyntax(classViewName+"."+connection.get('outlet',{}).get('property') +" = self;")
		# 	pass

		return describle

