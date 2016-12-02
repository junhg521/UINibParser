#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/22
# version: 0.0.1
# author: Junhg
# contribute:
# 
__author__ = 'Junhg'

from CommonObject import JHCommomObject

class JHBasicObject(JHCommomObject):
	
	def writeDescribleSyntax(self, syntax):
		return syntax + self.newlineCharacter()

	def getClassFrame(self, frame):
		classFrame = ""

		if frame.get('key','') == 'frameInset':
			classFrame = "CGRectMake("+frame.get('minX', '0')+","+frame.get('minY', "0")+","+frame.get('width', "320")+","+frame.get('height', "480")+")"
			pass
		elif frame.get('key', '') == 'frame':
			classFrame = "CGRectMake("+frame.get('x', '0')+","+frame.get('y', "0")+","+frame.get('width', "320")+","+frame.get('height', "480")+")"
			pass
		else:
			print 'frame=', frame
			pass

		return classFrame

	def getClassSizeAndKey(self, size):
		# print 'size=',size
		return (size.get('key',''), "CGSizeMake("+size.get('width','')+","+size.get('width','')+")")

	def getClassEdgementAndKey(self, edgement):
		# print 'edgement=',edgement
		return (edgement.get('key',''), "UIEdgeInsetsMake("+edgement.get('minX','')+","+edgement.get('minY','')+","+edgement.get('maxX','')+","+edgement.get('maxY','')+")")

	def getClassColor(self, color):
		classColor = ""

		if type(color) == dict:
			classColor = "[UIColor colorWithRed:"+color.get('red', '1')+" green:"+color.get('green', '1')+" blue:"+color.get('blue','1')+" alpha:"+color.get('alpha', '1')+"]"
			pass
		else:
			print 'color=',color
			pass

		return classColor

	def getTableViewCellSelectionStyle(self, selectionStyle):
		cellStyle = 'UITableViewCellSelectionStyleBlue'

		if selectionStyle == 'none':
			cellStyle = 'UITableViewCellSelectionStyleNone'
			pass
		elif selectionStyle == 'gray':
			cellStyle = 'UITableViewCellSelectionStyleGray'
			pass
		elif selectionStyle == 'blue':
			cellStyle = 'UITableViewCellSelectionStyleBlue'
			pass
		elif selectionStyle == 'default':
			cellStyle = 'UITableViewCellSelectionStyleDefault'
			pass
		else:
			print 'selectionStyle=',selectionStyle
			pass

		return cellStyle

	def getButtonType(self, buttonType):
		buttonObjectType = 'UIButtonTypeCustom'

		if buttonType == 'roundedRect':
			buttonObjectType = 'UIButtonTypeSystem'
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
			print 'buttonType = ', buttonType
			pass

		return buttonObjectType

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
			print 'aligment = ', aligment
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
			print 'adjustment = ', adjustment
			pass

		return lineAdjustment

	def getTextFont(self, fontDescription):
		font = ""

		if fontDescription.get('type', '') == 'boldSystem':
			font = "[UIFont boldSystemFontOfSize:"+fontDescription.get('pointSize', '17')+"]"
			pass
		elif fontDescription.get('type', '') == 'italicSystem':
			font = "[UIFont italicSystemFontOfSize:"+fontDescription.get('pointSize', '17')+"]"
			pass
		elif fontDescription.get('type', '') == 'system':
			font = "[UIFont systemFontOfSize:"+fontDescription.get('pointSize', '17')+"]"
			pass
		elif fontDescription.get('metaFont', '') == 'boldSystem':
			font = "[UIFont boldSystemFontOfSize:"+fontDescription.get('size', '17')+"]"
			pass
		elif fontDescription.get('metaFont', '') == 'italicSystem':
			font = "[UIFont italicSystemFontOfSize:"+fontDescription.get('size', '17')+"]"
			pass
		elif fontDescription.get('metaFont', '') == 'system':
			font = "[UIFont systemFontOfSize:"+fontDescription.get('size', '17')+"]"
			pass
		elif fontDescription.get('name', '') != '':
			font = " [UIFont fontWithName:@\""+fontDescription.get('name')+"\" size:"+fontDescription.get('size', '17')+"]"
			pass
		else:
			print 'fontDescription = ', fontDescription
			pass

		return font

	def getControlContentHorizontalAlignment(self, alignment):
		controlAlignment = 'UIControlContentHorizontalAlignmentCenter'

		if alignment == 'center':
			controlAlignment = 'UIControlContentHorizontalAlignmentCenter'
			pass
		elif alignment == 'left':
			controlAlignment = 'UIControlContentHorizontalAlignmentLeft'
			pass
		elif alignment == 'right':
			controlAlignment = 'UIControlContentHorizontalAlignmentRight'
			pass
		elif alignment == 'fill':
			controlAlignment = 'UIControlContentVerticalAlignmentFill'
			pass
		else:
			print 'alignment = ', alignment
			pass

		return controlAlignment

	def getControlContentVerticalAlignment(self, alignment):
		controlAlignment = 'UIControlContentVerticalAlignmentCenter'

		if alignment == 'center':
			controlAlignment = 'UIControlContentVerticalAlignmentCenter'
			pass
		elif alignment == 'top':
			controlAlignment = 'UIControlContentVerticalAlignmentTop'
			pass
		elif alignment == 'bottom':
			controlAlignment = 'UIControlContentVerticalAlignmentBottom'
			pass
		elif alignment == 'fill':
			controlAlignment = 'UIControlContentVerticalAlignmentFill'
			pass
		else:
			print 'alignment=',alignment
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
			print 'state=', state
			pass

		return controlState

	def getControlEvent(self, event):
		controlEvent = ''

		if event == 'touchDown':
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
		else:
			print 'event=', event
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
			print 'borderStyle=', borderStyle
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
			print 'mode=', mode
			pass
			
		return textFieldViewMode

	def getCollectionViewScrollDirection(self, scrollDirection):
		collectionScrollDirection = 'UICollectionViewScrollDirectionVertical'

		if scrollDirection == 'horizontal':
			collectionScrollDirection = 'UICollectionViewScrollDirectionHorizontal'
			pass
		elif scrollDirection == 'vertical':
			collectionScrollDirection = 'UICollectionViewScrollDirectionVertical'
			pass
		else:
			print 'scrollDirection=', scrollDirection
			pass

		return collectionScrollDirection

	def getTableViewStyle(self, tableViewStyle):
		result = 'UITableViewStylePlain'

		if tableViewStyle == 'plain':
			result = 'UITableViewStylePlain'
			pass
		elif tableViewStyle == 'grouped':
			result = 'UITableViewStyleGrouped'
			pass
		else:
			print 'tableViewStyle=',tableViewStyle
			pass

		return result

	def getScrollViewIndicatorStyle(self, scrollViewIndicatorStyle):
		result = 'UIScrollViewIndicatorStyleDefault'

		if scrollViewIndicatorStyle == 'default':
			result = 'UIScrollViewIndicatorStyleDefault'
			pass
		elif scrollViewIndicatorStyle == 'black':
			result = 'UIScrollViewIndicatorStyleBlack'
			pass
		elif scrollViewIndicatorStyle == 'white':
			result = 'UIScrollViewIndicatorStyleWhite'
			pass
		else:
			print 'scrollViewIndicatorStyle=', scrollViewIndicatorStyle
			pass
			
		return result

	def getScrollViewKeyboardDismissMode(self, scrollViewKeyboardDismissMode):
		result = 'UIScrollViewKeyboardDismissModeNone'

		if scrollViewKeyboardDismissMode == 'none':
			result = 'UIScrollViewKeyboardDismissModeNone'
			pass
		elif scrollViewKeyboardDismissMode == 'onDrag':
			result = 'UIScrollViewKeyboardDismissModeOnDrag'
			pass
		elif scrollViewKeyboardDismissMode == 'interactive':
			result = 'UIScrollViewKeyboardDismissModeInteractive'
			pass
		else:
			print 'style=', scrollViewKeyboardDismissMode
			pass
			
		return result

	def getTableViewCellSeparatorStyle(self, tableViewCellSeparatorStyle):
		result = 'UITableViewCellSeparatorStyleSingleLine'

		if tableViewCellSeparatorStyle == 'none':
			result = 'UITableViewCellSeparatorStyleNone'
			pass
		elif tableViewCellSeparatorStyle == 'singleLine':
			result = 'UITableViewCellSeparatorStyleSingleLine'
			pass
		elif tableViewCellSeparatorStyle == 'singleLineEtched':
			result = 'UITableViewCellSeparatorStyleSingleLineEtched'
			pass
		elif tableViewCellSeparatorStyle == 'default':
			result = 'UITableViewCellSeparatorStyleSingleLine'
			pass
		else:
			print 'tableViewCellSeparatorStyle=', tableViewCellSeparatorStyle
			pass
			
		return result

	def getAutoresizingMask(self, autoresizingMask):
		# print 'autoresizingMask=',autoresizingMask

		autoresizing = 'UIViewAutoresizingNone'
		autoresizing = self.appendAutoreleasingMask(autoresizingMask, 'flexibleMaxX', 'NO', autoresizing, 'UIViewAutoresizingFlexibleLeftMargin')
		autoresizing = self.appendAutoreleasingMask(autoresizingMask, 'widthSizable', 'NO', autoresizing, 'UIViewAutoresizingFlexibleWidth')
		autoresizing = self.appendAutoreleasingMask(autoresizingMask, 'flexibleMinX', 'NO', autoresizing, 'UIViewAutoresizingFlexibleRightMargin')
		autoresizing = self.appendAutoreleasingMask(autoresizingMask, 'flexibleMaxY', 'NO', autoresizing, 'UIViewAutoresizingFlexibleTopMargin')
		autoresizing = self.appendAutoreleasingMask(autoresizingMask, 'heightSizable', 'NO', autoresizing, 'UIViewAutoresizingFlexibleHeight')
		autoresizing = self.appendAutoreleasingMask(autoresizingMask, 'flexibleMinY', 'NO', autoresizing, 'UIViewAutoresizingFlexibleBottomMargin')

		return autoresizing

	def appendAutoreleasingMask(self, autoresizingMask, key, defaultKey, oldAutoresizing, newAutoresizing):
		# print 'autoresizingMask=',autoresizingMask
		
		if autoresizingMask.get(key, defaultKey) != defaultKey:
			return self.getMergeAutoresizingMask(oldAutoresizing, newAutoresizing)
		else:
			return oldAutoresizing

	def getMergeAutoresizingMask(self, oldAutoresizing, newAutoresizing):
		# print 'oldAutoresizing=', oldAutoresizing, ' newAutoresizing=',newAutoresizing

		if oldAutoresizing == 'UIViewAutoresizingNone':
			oldAutoresizing = newAutoresizing 
			pass
		else:
			oldAutoresizing = oldAutoresizing +' | '+ newAutoresizing
			pass

		return oldAutoresizing

	def getContentModel(self, viewModel):
		contentMode = 'UIViewContentModeScaleToFill'

		if viewModel == 'scaleToFill':
			contentMode = 'UIViewContentModeScaleToFill'
			pass
		elif viewModel == 'scaleAspectFit':
			contentMode = 'UIViewContentModeScaleAspectFit'
			pass
		elif viewModel == 'scaleAspectFill':
			contentMode = 'UIViewContentModeScaleAspectFill'
			pass
		elif viewModel == 'redraw':
			contentMode = 'UIViewContentModeRedraw'
			pass
		elif viewModel == 'center':
			contentMode = 'UIViewContentModeCenter'
			pass
		elif viewModel == 'Top':
			contentMode = 'UIViewContentModeTop'
			pass
		elif viewModel == 'bottom':
			contentMode = 'UIViewContentModeBottom'
			pass
		elif viewModel == 'left':
			contentMode = 'UIViewContentModeLeft'
			pass
		elif viewModel == 'right':
			contentMode = 'UIViewContentModeRight'
			pass
		elif viewModel == 'TopLeft':
			contentMode = 'UIViewContentModeTopLeft'
			pass
		elif viewModel == 'TopRight':
			contentMode = 'UIViewContentModeTopRight'
			pass
		elif viewModel == 'bottomLeft':
			contentMode = 'UIViewContentModeBottomLeft'
			pass
		elif viewModel == 'bottomRight':
			contentMode = 'UIViewContentModeBottomRight'
			pass
		else:
			print 'viewModel=', viewModel
			pass

		return contentMode

	def setViewProperty(self, classViewName, key, attribValue, defaultValue):
		describle = ""
		if attribValue != defaultValue and len(key):
			describle = self.addBlackCharacter()
			describle += self.writeDescribleSyntax(classViewName+"."+key+" = "+attribValue+";")
			pass
		return describle
		

