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
		# print 'attribView=', attribView
		classViewAttrib = self.attribViewTagProperty(attribView)
		
		describle = "\n- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier\n{\n"
		describle +="	if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier]) {\n"
		for color in attribView.get('color', {}):
			if len(color.get('key','')) > 0 and color.get('key','') != 'textColor':
				describle +="		self."+color.get('key','')+" = "+self.getClassColor(color)+";\n"
				pass
			pass
		
		describle += JHViewObject.addViewAttribute("self",self.attribViewTagProperty(attribView))
		describle += JHViewObject.addViewAttribute("self.contentView",self.attribViewTagProperty(attribView))
		describle +="	[self loadAllSubView];"
		describle +="	}\n"
		describle +="	return self;\n"
		describle +="}\n"

		return describle
