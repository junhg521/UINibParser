#!/usr/bin/python
# _*_ coding: UTF-8 _*_

# create: 2016/10/22
# version: 0.0.1
# author: Junhg
# contribute:
# 
__author__ = 'Junhg'

from CommonObject import JHCommomObject

class JHBasicObject(JHCommomObject):
	def __init__(self):
		pass
			
	def __del__(self):
		pass

	def addSubview(self, attribView):
		return ""
		
	def getClassFrame(self, frame):
		classFrame = ""
		if len(frame) == 0:
			pass
		else:
			if frame.get('key','frameInset') == 'frameInset':
				classFrame = "CGRectMake("+str(frame.get('minX', 0))+","+str(frame.get('minY', 0))+","+str(frame.get('width', 320))+","+str(frame.get('height', 480))+")"
				pass
			else :
				classFrame = "CGRectMake("+str(frame.get('x', 0))+","+str(frame.get('y', 0))+","+str(frame.get('width', 320))+","+str(frame.get('height', 480))+")"
				pass
		return classFrame

	def getClassColor(self, color):
		if len(color) > 0:
			red = str(color.get('red', 0))
			green = str(color.get('green', 0))
			blue = str(color.get('blue',0))
			alpha = str(color.get('alpha', 1))
			return "[UIColor colorWithRed:"+red+" green:"+green+" blue:"+blue+" alpha:"+alpha+"]"
		else:
			return ""

	def getContentModel(self, model):
		contentMode = 'UIViewContentModeScaleToFill'

		if model == 'scaleToFill':
			contentMode = 'UIViewContentModeScaleToFill'
			pass
		elif model == 'scaleAspectFit':
			contentMode = 'UIViewContentModeScaleAspectFit'
			pass
		elif model == 'scaleAspectFill':
			contentMode = 'UIViewContentModeScaleAspectFill'
			pass
		elif model == 'redraw':
			contentMode = 'UIViewContentModeRedraw'
			pass
		elif model == 'center':
			contentMode = 'UIViewContentModeCenter'
			pass
		elif model == 'Top':
			contentMode = 'UIViewContentModeTop'
			pass
		elif model == 'bottom':
			contentMode = 'UIViewContentModeBottom'
			pass
		elif model == 'left':
			contentMode = 'UIViewContentModeLeft'
			pass
		elif model == 'right':
			contentMode = 'UIViewContentModeRight'
			pass
		elif model == 'TopLeft':
			contentMode = 'UIViewContentModeTopLeft'
			pass
		elif model == 'TopRight':
			contentMode = 'UIViewContentModeTopRight'
			pass
		elif model == 'bottomLeft':
			contentMode = 'UIViewContentModeBottomLeft'
			pass
		elif model == 'bottomRight':
			contentMode = 'UIViewContentModeBottomRight'
			pass
		else:
			pass

		return contentMode

	def getAutoresizingMask(self, autoresizingMask):
		autoresizing = 'UIViewAutoresizingNone'

		if autoresizingMask.get('flexibleMaxX', 'NO') == 'YES':
			autoresizing = self.getMergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleLeftMargin')
			pass
		if autoresizingMask.get('widthSizable', 'NO') == 'YES':
			autoresizing = self.getMergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleWidth')
			pass
		if autoresizingMask.get('flexibleMinX', 'NO') == 'YES':
			autoresizing = self.getMergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleRightMargin')
			pass
		if autoresizingMask.get('flexibleMaxY', 'NO') == 'YES':
			autoresizing = self.getMergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleTopMargin')
			pass
		if autoresizingMask.get('heightSizable', 'NO') == 'YES':
			autoresizing = self.getMergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleHeight')
			pass
		if autoresizingMask.get('flexibleMinY', 'NO') == 'YES':
			autoresizing = self.getMergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleBottomMargin')
			pass

		return autoresizing
	
	def getMergeAutoresizingMask(self, oldAutoresizing, newAutoresizing):
		if oldAutoresizing == 'UIViewAutoresizingNone':
			oldAutoresizing = newAutoresizing 
			pass
		else:
			oldAutoresizing = oldAutoresizing +' | '+ newAutoresizing

		return oldAutoresizing

	def getButtonType(self, buttonType):
		buttonObjectType = 'UIButtonTypeSystem'

		if buttonType == 'roundedRect':
			pass
		elif buttonType == 'contactAdd':
			buttonObjectType = 'UIButtonTypeContactAdd'
			pass
		elif buttonType == 'infoDark':
			buttonObjectType = 'UIButtonTypeInfoDark'
			pass
		elif buttonType == 'infoLight':
			buttonObjectType = 'UIButtonTypeInfoLight'
			pass
		elif buttonType == 'detailDisclosure':
			buttonObjectType = 'UIButtonTypeDetailDisclosure'
			pass
		elif buttonType == 'system':
			buttonObjectType = 'UIButtonTypeSystem'
			pass
		elif buttonType == 'custom':
			buttonObjectType = 'UIButtonTypeCustom'
			pass
		else:
			pass

		return bType

	def getTextAlignment(self, aligment):
		textAligment = 'NSTextAlignmentNatural'

		if aligment == 'left':
			textAligment = 'NSTextAlignmentLeft'
			pass
		elif aligment == 'center':
			textAligment = 'NSTextAlignmentCenter'
			pass
		elif aligment == 'right':
			textAligment = 'NSTextAlignmentRight'
			pass
		elif aligment == 'justified':
			textAligment = 'NSTextAlignmentJustified'
			pass
		elif aligment == 'natural':
			textAligment = 'NSTextAlignmentNatural'
			pass
		else:
			pass

		return textAligment

	def getBaselineAdjustment(self, adjustment):
		lineAdjustment = 'UIBaselineAdjustmentAlignBaselines'

		if adjustment == 'alignBaselines':
			lineAdjustment = 'UIBaselineAdjustmentAlignBaselines'
			pass
		elif adjustment == 'alignCenters':
			lineAdjustment = 'UIBaselineAdjustmentAlignCenters'
			pass
		else:
			pass

		return lineAdjustment

	def getTextFont(self, fontDescription):
		# print 'fontDescription = ', fontDescription
		fontSize = fontDescription.get('pointSize', '17')
		fontType = fontDescription.get('type', 'system')

		if fontType == 'boldSystem':
			return "[UIFont boldSystemFontOfSize:"+str(fontSize)+"];"
		elif fontType == 'italicSystem':
			return "[UIFont italicSystemFontOfSize:"+str(fontSize)+"];"
		else :
			return "[UIFont systemFontOfSize:"+str(fontSize)+"];"
		pass

	def getControlContentHorizontalAlignment(self, alignment):
		controlAlignment = 'UIControlContentHorizontalAlignmentCenter'

		if aligment == 'center':
			controlAlignment = 'UIControlContentHorizontalAlignmentCenter'
			pass
		elif aligment == 'left':
			controlAlignment = 'UIControlContentHorizontalAlignmentLeft'
			pass
		elif aligment == 'right':
			controlAlignment = 'UIControlContentHorizontalAlignmentRight'
			pass
		elif aligment == 'fill':
			controlAlignment = 'UIControlContentVerticalAlignmentFill'
			pass
		else:
			pass

		return controlAlignment

	def getControlContentVerticalAlignment(self, alignment):
		controlAlignment = 'UIControlContentVerticalAlignmentCenter'

		if aligment == 'center':
			controlAlignment = 'UIControlContentVerticalAlignmentCenter'
			pass
		elif aligment == 'top':
			controlAlignment = 'UIControlContentVerticalAlignmentTop'
			pass
		elif aligment == 'bottom':
			controlAlignment = 'UIControlContentVerticalAlignmentBottom'
			pass
		elif aligment == 'fill':
			controlAlignment = 'UIControlContentVerticalAlignmentFill'
			pass
		else:
			pass

		return controlAlignment

	def getControlState(self, state):
		controlState = 'UIControlStateNormal'

		if state == 'normal':
			controlState = 'UIControlStateNormal'
			pass
		elif state == 'highlighted':
			controlState = 'UIControlStateHighlighted'
			pass
		elif state == 'disabled':
			controlState = 'UIControlStateDisabled'
			pass
		elif state == 'selected':
			controlState = 'UIControlStateSelected'
			pass
		elif state == 'focused':
			controlState = 'UIControlStateFocused'
			pass
		elif state == 'application':
			controlState = 'UIControlStateApplication'
			pass
		elif state == 'reserved':
			controlState = 'UIControlStateReserved'
			pass
		else:
			pass

		return controlState

	def getControlEvent(self, event):
		controlEvent = ''

		if event == 'down':
			controlEvent = 'UIControlEventTouchDown'
			pass
		elif event == 'downRepeat':
			controlEvent = 'UIControlEventTouchDownRepeat'
			pass
		elif event == 'dragInside':
			controlEvent = 'UIControlEventTouchDragInside'
			pass
		elif event == 'dragOutside':
			controlEvent = 'UIControlEventTouchDragOutside'
			pass
		elif event == 'dragEnter':
			controlEvent = 'UIControlEventTouchDragEnter'
			pass
		elif event == 'dragExit':
			controlEvent = 'UIControlEventTouchDragExit'
			pass
		elif event == 'touchUpInside':
			controlEvent = 'UIControlEventTouchUpInside'
			pass
		elif event == 'touchUpOutside':
			controlEvent = 'UIControlEventTouchUpOutside'
			pass
		elif event == 'cancel':
			controlEvent = 'UIControlEventTouchCancel'
			pass
		elif event == 'valueChanged':
			controlEvent = 'UIControlEventValueChanged'
			pass
		elif event == 'primaryActionTriggered':
			controlEvent = 'UIControlEventPrimaryActionTriggered'
			pass
		elif event == 'editingDidBegin':
			controlEvent = 'UIControlEventEditingDidBegin'
			pass
		elif event == 'editingChanged':
			controlEvent = 'UIControlEventEditingChanged'
			pass
		elif event == 'editingDidEnd':
			controlEvent = 'UIControlEventEditingDidEnd'
			pass
		elif event == 'editingDidEndOnExit':
			controlEvent = 'UIControlEventEditingDidEndOnExit'
			pass
		elif event == 'allTouchEvents':
			controlEvent = 'UIControlEventAllTouchEvents'
			pass
		elif event == 'allEditingEvents':
			controlEvent = 'UIControlEventAllEditingEvents'
			pass
		elif event == 'applicationReserved':
			controlEvent = 'UIControlEventApplicationReserved'
			pass
		elif event == 'systemReserved':
			controlEvent = 'UIControlEventSystemReserved'
			pass
		elif event == 'allEvents':
			controlEvent = 'UIControlEventAllEvents'
			pass
		else :
			pass

		return controlEvent

	def getTextBorderStyle(self, borderStyle):
		textBorderStyle = 'UITextBorderStyleNone'

		if borderStyle == 'none':
			textBorderStyle = 'UITextBorderStyleNone'
			pass
		elif borderStyle == 'line':
			textBorderStyle = 'UITextBorderStyleLine'
			pass
		elif borderStyle == 'bezel':
			textBorderStyle = 'UITextBorderStyleBezel'
			pass
		elif borderStyle == 'roundedRect':
			textBorderStyle = 'UITextBorderStyleRoundedRect'
			pass
		else:
			pass

		return textBorderStyle

	def getTextFieldViewMode(self, mode):
		textFieldViewMode = 'UITextFieldViewModeNever'

		if mode == 'never':
			textFieldViewMode = 'UITextFieldViewModeNever'
			pass
		elif mode == 'whileEditing':
			textFieldViewMode = 'UITextFieldViewModeWhileEditing'
			pass
		elif mode == 'unlessEditing':
			textFieldViewMode = 'UITextFieldViewModeUnlessEditing'
			pass
		elif mode == 'always':
			textFieldViewMode = 'UITextFieldViewModeAlways'
			pass
		else:
			pass
			
		return textFieldViewMode
		