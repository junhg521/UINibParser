#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/28
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHButtonObject(JHViewObject):
	def __init__(self):
			pass

	def __del__(self):
			pass

	def addSubview(self, attribView, isLoadView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		classViewAttrib = self.attribViewTagProperty(attribView)
		textAligment = self.getTextAlignment(classViewAttrib.get('textAlignment', 'NSTextAlignmentLeft'))
		lineAdjustment = self.getBaselineAdjustment(classViewAttrib.get('baselineAdjustment', 'UIBaselineAdjustmentAlignBaselines'))
		font = self.getTextFont(attribView.get('fontDescription', {}))
		textColor = self.getClassColor(attribView.get('textColor', {}))
		controlStates = attribView.get('state', {})
		connections = attribView.get('connections', {})
		frame =  self.getClassFrame(attribView.get('frame', {}))

		describle = JHViewObject.addSubview(self,attribView,False)

		if len(frame) > 0:
			describle +="	"+classViewName+".frame = "+frame+";\n"
			pass

		for controlState in controlStates:
			if controlState.has_key('title'):
				describle +="	["+classViewName+" setTitle:@"+"\""+controlState.get('title', '')+"\""+" forState:"+self.getControlState(controlState.get('key','normal'))+"];\n"
				pass
			if controlState.has_key('backgroundImage'):
				describle +="	["+classViewName+" setBackgroundImage:[UIImage imageNamed:@"+"\""+controlState.get('backgroundImage', '')+"\""+"] forState:"+self.getControlState(controlState.get('key','normal'))+"];\n"
				pass
			if controlState.has_key('image'):
				describle +="	["+classViewName+" setImage:[UIImage imageNamed:@"+"\""+controlState.get('image', '')+"\""+"] forState:"+self.getControlState(controlState.get('key','normal'))+"];\n"
				pass
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

