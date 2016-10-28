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
		
		if attribView.get('contentVerticalAlignment', 'center') != 'center':
			describle +="	"+classViewName+".contentVerticalAlignment = "+self.getControlContentVerticalAlignment(attribView.get('contentVerticalAlignment', 'center'))+";\n"
			pass

		if attribView.get('contentHorizontalAlignment', 'center') != 'center':
			describle +="	"+classViewName+".contentHorizontalAlignment = "+self.getControlContentHorizontalAlignment(attribView.get('contentHorizontalAlignment', 'center'))+";\n"
			pass

		for controlState in controlStates:
			describle +="	["+classViewName+" setTitle:@"+"\""+controlState.get('title', '')+"\""+" forState:"+self.getControlState(controlState.get('key','normal'))+"];\n"
			if len(controlState.get('backgroundImage','')) > 0:
					describle +="	["+classViewName+" setBackgroundImage:@"+"\""+controlState.get('backgroundImage', '')+"\""+" forState:"+self.getControlState(controlState.get('key','normal'))+"];\n"
					pass
				elif len(controlState.get('image', '')) > 0:
					describle +="	["+classViewName+" setImage:@"+"\""+controlState.get('image', '')+"\""+" forState:"+self.getControlState(controlState.get('key','normal'))+"];\n"
				pass
			pass
			
		for connection in connections:
			action = connection.get('action', {})
			if len(action) > 0:
				describle +="	["+classViewName+" addTarget:self action:@selector("+action.get('selector','')+") forControlEvents:+"+self.getControlEvent(action.get('eventType', 'touchUpInside'))+"];\n"
			pass
		return describle

