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

	def addSubview(self, classViewName, classMethodName, attribView):
		# print 'attribView=', attribView

		attribViewId = self.attribViewTagProperty(attribView)

		classType = self.objcClassNameType(classViewName)
		describle = self.newlineCharacter()
		describle += self.writeDescribleSyntax("- ("+classType+" *"+")"+classMethodName)
		describle += self.leftBrackets()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax(classType+"* "+classViewName+" = [UIButton buttonWithType:"+self.getButtonType(attribViewId.get('buttonType', 'system'))+"];")
		describle += self.setViewProperty(classViewName, 'frame', self.getClassFrame(attribView.get('rect',{})), '')
		
		return describle

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		describle = JHControlObject.addViewAttribute(self, classViewName, attribView)

		return describle
