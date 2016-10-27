#!/usr/bin/python
# _*_ coding: UTF-8 _*_

# create: 2016/10/21
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

	def addSubview(self, attribView, isLoadView):
		classViewName = self.attribViewTag(attribView)
		classType = self.objcClassNameType(classViewName)
		classMethodName = self.attribViewViewMethod(attribView)
		backgroundColor = self.objcClassColor(attribView.get('backgroundColor', {}))
		frame = self.objcClassFrame(attribView.get('frame', {}))
		autoresizingMask = self.loadAutoresizingMask(attribView.get('autoresizingMask', {}))
		contentModel = self.loadViewContentModel(attribView.get('contentMode', 'scaleToFill'))
		
		describle = "\n"

		# 变更成classViewName所对应的类型
		if isLoadView:
			classViewName = "self.view"
			describle += "- (void)loadView\n{\n"
			if len(frame) > 0:
				describle +="	self.view = [["+classType+" alloc] initWithFrame:"+frame+"];\n"
				pass
			else :
				describle +="	self.view = [["+classType+" alloc] init];\n"
				pass
			pass
		else:
			describle += "- ("+classType+" *"+")"+classMethodName+"\n{\n"
			if len(frame) > 0:
				describle +="	"+classType+"* "+classViewName+" = [["+classType+" alloc] initWithFrame:"+frame+"];\n"
				pass
			else :
				describle +="	"+classType+"* "+classViewName+" = [["+classType+" alloc] init];\n"
				pass
			pass

		describle +="	"+classViewName+".tag = [@"+"\""+self.attribViewMethodNameId(classMethodName)+"\""+" hash];\n"
		
		if len(backgroundColor) > 0:
			describle +="	"+classViewName+".backgroundColor = "+backgroundColor+";\n"
			pass
		
		if autoresizingMask != 'UIViewAutoresizingNone':
			describle +="	"+classViewName+".autoresizingMask = "+autoresizingMask+";\n"
			pass
		
		if contentModel != 'UIViewContentModeScaleToFill':
			describle +="	"+classViewName+".contentMode = "+contentModel+";\n"
			pass

		return describle
		
	def objcClassFrame(self, frame):
		classFrame = ""
		if len(frame) == 0:
			pass
		else :
			if frame.get('key','frameInset') == 'frameInset':
				classFrame = "CGRectMake("+str(frame.get('minX', 0))+","+str(frame.get('minY', 0))+","+str(frame.get('width', 320))+","+str(frame.get('height', 480))+")"
				pass
			else :
				classFrame = "CGRectMake("+str(frame.get('x', 0))+","+str(frame.get('y', 0))+","+str(frame.get('width', 320))+","+str(frame.get('height', 480))+")"
				pass
		return classFrame

	def objcClassColor(self, color):
		if len(color) > 0:
			red = str(color.get('red', 0))
			green = str(color.get('green', 0))
			blue = str(color.get('blue',0))
			alpha = str(color.get('alpha', 1))
			return "[UIColor colorWithRed:"+red+" green:"+green+" blue:"+blue+" alpha:"+alpha+"]"
			pass
		else :
			return ""

	def loadViewContentModel(self, model):
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

	def loadAutoresizingMask(self, autoresizingMask):
		autoresizing = 'UIViewAutoresizingNone'

		if autoresizingMask.get('flexibleMaxX', 'NO') == 'YES':
			autoresizing = self.mergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleLeftMargin')
			pass
		if autoresizingMask.get('widthSizable', 'NO') == 'YES':
			autoresizing = self.mergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleWidth')
			pass
		if autoresizingMask.get('flexibleMinX', 'NO') == 'YES':
			autoresizing = self.mergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleRightMargin')
			pass
		if autoresizingMask.get('flexibleMaxY', 'NO') == 'YES':
			autoresizing = self.mergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleTopMargin')
			pass
		if autoresizingMask.get('heightSizable', 'NO') == 'YES':
			autoresizing = self.mergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleHeight')
			pass
		if autoresizingMask.get('flexibleMinY', 'NO') == 'YES':
			autoresizing = self.mergeAutoresizingMask(autoresizing, 'UIViewAutoresizingFlexibleBottomMargin')
			pass

		return autoresizing
	
	def mergeAutoresizingMask(self, oldAutoresizing, newAutoresizing):
		if oldAutoresizing == 'UIViewAutoresizingNone':
			oldAutoresizing = newAutoresizing 
			pass
		else :
			oldAutoresizing = oldAutoresizing +' | '+ newAutoresizing
		return oldAutoresizing
