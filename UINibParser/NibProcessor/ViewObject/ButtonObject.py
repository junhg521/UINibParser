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
		describle += self.addViewAttribute(classViewName, attribView)
		return describle

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		describle = JHControlObject.addViewAttribute(self, classViewName, attribView)
		describle += self.addButtonViewAttribute(classViewName, attribView)
		return describle

	def addButtonViewAttribute(self, classViewName, attribView):
		describle = ""
		describle += self.setViewProperty(classViewName+".titleLabel", 'font', self.getTextFont(attribView.get('fontDescription', {})), '')
		if attribView.has_key('states'):
			if type(attribView.get('states')) == list:
				for controlState in attribView.get('states', []):
					describle += self.setControlSateInfos(classViewName, controlState)
				pass
			elif type(attribView.get('states')) == dict:
				describle += self.setControlSateInfos(classViewName, attribView.get('states', {}))
				pass
			else:
				pass
			pass
		return describle

	def setControlSateInfos(self, classViewName, controlStates):
		# print 'controlState=',controlState
		
		describle = ""
		controlState = controlStates.get('state', {})
		buttonState = self.getControlState(controlState.get('key','normal'))
		if controlState.get('title', '') != '':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("["+classViewName+" setTitle:@"+"\""+controlState.get('title', '').encode('utf-8') +"\""+" forState:"+buttonState+"];")
			pass

		if controlState.get('backgroundImage','') != '':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("["+classViewName+" setBackgroundImage:[UIImage imageNamed:@"+"\""+controlState.get('backgroundImage', '').encode('utf-8')+"\""+"] forState:"+buttonState+"];")
			pass

		if controlState.get('image', '') != '':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("["+classViewName+" setImage:[UIImage imageNamed:@"+"\""+controlState.get('image', '').encode('utf-8')+"\""+"] forState:"+buttonState+"];")
			pass

		if controlStates.has_key('color'):
			if type(controlStates.get('color')) == list:
				for color in controlStates.get('color', []):
					describle += self.getControlColorProperty(classViewName, color, buttonState)
					pass
				pass
			elif type(controlStates.get('color')) == dict:
				describle = self.getControlColorProperty(classViewName, controlStates.get('color', {}), buttonState)
				pass
			else:
				pass
		else:
			# print 'controlState=', controlState
			pass
		return describle

	def getControlColorProperty(self, classViewName, color, controlState):
		colorTag = color.get('key', '')
		describle = self.addBlackCharacter()
		describle += self.writeDescribleSyntax("["+classViewName +" set"+colorTag[0].upper()+colorTag[1:]+":"+self.getClassColor(color)+" forState:"+controlState+"];")
		return describle
