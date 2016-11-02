#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/11/1
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHTableViewCellObject(JHViewObject):
	def __init__(self):
		pass

	def __del__(self):
		pass
		
	def addSubview(self, attribView):
		pass

	def loadView(self,attribView):
		print 'attribView=', attribView
		classViewAttrib = self.attribViewTagProperty(attribView)
		
		describle = "\n- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier\n{\n"
		describle +="	if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier]) {\n"
		for color in attribView.get('color', {}):
			if len(color.get('key','')) > 0 and color.get('key','') != 'textColor':
				describle +="		self.view."+color.get('key','')+" = "+self.getClassColor(color)+";\n"
				pass
			pass
		
		if self.getAutoresizingMask(attribView.get('autoresizingMask', {})) != 'UIViewAutoresizingNone':
			describle +="		self.view.autoresizingMask = "+self.getAutoresizingMask(attribView.get('autoresizingMask', {}))+";\n"
			pass
		
		if self.getContentModel(attribView.get('contentMode', 'scaleToFill')) != 'UIViewContentModeScaleToFill':
			describle +="		self.view.contentMode = "+self.getContentModel(attribView.get('contentMode', 'scaleToFill'))+";\n"
			pass

		if attribView.get('opaque', 'YES') != 'YES':
			describle +="		self.view.opaque = "+attribView.get('opaque', 'YES')+";\n"
			pass

		if attribView.get('clearsContextBeforeDrawing', 'YES') != 'YES':
			describle +="		self.view.clearsContextBeforeDrawing = "+attribView.get('clearsContextBeforeDrawing', 'YES')+";\n"
			pass

		if classViewAttrib.get('translatesAutoresizingMaskIntoConstraints', 'YES') != 'YES':
			describle +="		self.view.translatesAutoresizingMaskIntoConstraints = "+classViewAttrib.get('translatesAutoresizingMaskIntoConstraints', 'YES')+';\n'
			pass

		if attribView.get('contentVerticalAlignment', 'center') != 'center':
			describle +="		self.view.contentVerticalAlignment = "+self.getControlContentVerticalAlignment(attribView.get('contentVerticalAlignment', 'center'))+";\n"
			pass
		
		if attribView.get('contentHorizontalAlignment', 'center') != 'center':
			describle +="		self.view.contentHorizontalAlignment = "+self.getControlContentHorizontalAlignment(attribView.get('contentHorizontalAlignment', 'center'))+";\n"
			pass
		describle += "	}\n"
		describle +="	return self;\n"
		describle += "}\n"

		return describle
