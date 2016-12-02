#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/21
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

	def addSubview(self, attribView, isLoadView):
		frame = self.objcClassFrame(attribView.get('rect', {}))
		classViewName = self.attribViewTag(attribView)
		clearsContextBeforeDrawing = attribView.get('clearsContextBeforeDrawing', 'NO')

		describle = "\n#pragma mark - lifeCycle\n"
		describle += JHBasicObject.addSubview(self, attribView, isLoadView)
		describle +="	self."+classViewName+".clearsContextBeforeDrawing = "+clearsContextBeforeDrawing+";\n"
		describle += "}\n"
		return describle
