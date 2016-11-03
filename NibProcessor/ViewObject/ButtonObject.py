#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/28
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ControlObject import JHControlObject

class JHButtonObject(JHControlObject):
	def __init__(self):
			pass

	def __del__(self):
			pass

	def addSubview(self, attribView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		classType = self.objcClassNameType(classViewName)
		classMethodName = self.attribViewViewMethod(attribView)

		describle = "\n- ("+classType+" *"+")"+classMethodName+"\n{\n"
		describle +="	"+classType+"* "+classViewName+" = [UIButton buttonWithType:"+self.getButtonType(attribView.get('buttonType', 'roundedRect'))+"];\n"
		describle += JHControlObject.addControlAttribute(self,attribView)

		if len(self.getClassFrame(attribView.get('frame', {}))) > 0:
			describle +="	"+classViewName+".frame = "+self.getClassFrame(attribView.get('frame', {}))+";\n"
			pass

		for controlState in attribView.get('state', {}):
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
			
		return describle

