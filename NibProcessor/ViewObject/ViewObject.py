#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/24
# version: 0.0.1
# author: Junhg
# contribute:
# 

from BasicObject import JHBasicObject

class JHViewObject(JHBasicObject):
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
		if len(self.getClassFrame(attribView.get('frame', {}))) > 0:
			describle +="	"+classType+"* "+classViewName+" = [["+classType+" alloc] initWithFrame:"+self.getClassFrame(attribView.get('frame', {}))+"];\n"
			pass
		else :
			describle +="	"+classType+"* "+classViewName+" = [["+classType+" alloc] init];\n"
			pass
		pass

		describle +=self.addViewAttribute(classViewName,self.attribViewTagProperty(attribView))
		describle +="	"+classViewName+".tag = [@"+"\""+self.attribViewMethodNameId(classMethodName)+"\""+" hash];\n"

		return describle

	def loadView(self, attribView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		classType = self.objcClassNameType(classViewName)
		classMethodName = self.attribViewViewMethod(attribView)
		
		describle = "\n- (void)loadView\n{\n"
		if len(self.getClassFrame(attribView.get('rect', {}))) > 0:
			describle +="	self.view = [[UIView alloc] initWithFrame:"+self.getClassFrame(attribView.get('rect', {}))+"];\n"
			pass
		else:
			describle +="	self.view = [[UIView alloc] init];\n"
			pass
		pass
			
		describle +=self.addViewAttribute("self.view",self.attribViewTagProperty(attribView))
		describle += "}\n"

		return describle

	def addContentSubview(self,attribView):
		# print 'attribView=', attribView
		attribViewId = self.attribViewTagProperty(attribView)
		classViewName = self.attribViewTag(attribView)
		classType = self.objcClassNameType(classViewName)
		classMethodName = self.attribViewViewMethod(attribView)

		describle = "\n- ("+classType+" *"+")"+classMethodName+"\n{\n"
		describle +=self.addViewAttribute("self."+attribViewId.get('key','contentView'),self.attribViewTagProperty(attribView))

		return describle

	def addViewAttribute(self, classViewName, attribView):
		print 'attribView=', attribView

		describle = ""
		if self.getAutoresizingMask(attribView.get('autoresizingMask', {})) != 'UIViewAutoresizingNone':
			describle +="	"+classViewName+".autoresizingMask = "+self.getAutoresizingMask(attribView.get('autoresizingMask', {}))+";\n"
			pass

		if attribView.get('opaque', 'YES') != 'YES':
			describle +="	"+classViewName+".opaque = "+attribView.get('opaque', 'YES')+";\n"
			pass

		if attribView.get('clearsContextBeforeDrawing', 'YES') != 'YES':
			describle +="	"+classViewName+".clearsContextBeforeDrawing = "+attribView.get('clearsContextBeforeDrawing', 'YES')+";\n"
			pass

		if attribView.get('translatesAutoresizingMaskIntoConstraints', 'YES') != 'YES':
			describle +="	"+classViewName+".translatesAutoresizingMaskIntoConstraints = "+attribView.get('translatesAutoresizingMaskIntoConstraints', 'YES')+';\n'
			pass

		for color in attribView.get('color', {}):
			if len(color.get('key','')) > 0 and color.get('key','') != 'backgroundColor':
				describle +="	"+classViewName+"."+color.get('key','')+" = "+self.getClassColor(color)+";\n"
				pass
			pass

		if attribView.get('userInteractionEnabled', 'YES') != 'YES':
			describle +="	"+classViewName+".userInteractionEnabled = "+attribView.get('userInteractionEnabled', 'YES')+';\n'
			pass

		if attribView.get('canBecomeFocused', 'NO') != 'NO':
			describle +="	"+classViewName+".canBecomeFocused = "+attribView.get('canBecomeFocused', 'NO')+';\n'
			pass

		if attribView.get('clipsToBounds', 'YES') != 'YES':
			describle +="	"+classViewName+".clipsToBounds = "+attribView.get('clipsToBounds', 'YES')+';\n'
			pass

		if attribView.get('alpha', '1.0') != '1.0':
			describle +="	"+classViewName+".alpha = "+attribView.get('alpha', '1.0')+';\n'
			pass

		if attribView.get('hidden', 'NO') != 'NO':
			describle +="	"+classViewName+".hidden = "+attribView.get('hidden', 'NO')+';\n'
			pass

		if self.getContentModel(attribView.get('contentMode', 'scaleToFill')) != 'UIViewContentModeScaleToFill':
			describle +="	"+classViewName+".contentMode = "+self.getContentModel(attribView.get('contentMode', 'scaleToFill'))+";\n"
			pass

		return describle
