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
		
		describle = "\n- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier\n{\n"
		describle +="	if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier]) {\n"
		describle +="	"+JHViewObject.addViewAttribute(self,"self",attribView)
		describle +="	[self loadAllSubView];\n"
		describle +="	}\n"
		describle +="	return self;\n"
		describle +="}\n"

		return describle
