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

		describle = JHBasicObject.addSubview(self, attribView, isLoadView)

		if isLoadView:
			if attribView.get('clearsContextBeforeDrawing', 'YES') != 'YES':
				describle +="	self."+classViewName+".clearsContextBeforeDrawing = "+attribView.get('clearsContextBeforeDrawing', 'YES')+";\n"
				pass
			pass

			describle += "}\n"
		else :
			if attribView.get('clearsContextBeforeDrawing', 'YES') != 'YES':
				describle +="	"+classViewName+".clearsContextBeforeDrawing = "+attribView.get('clearsContextBeforeDrawing', 'YES')+";\n"
				pass
			pass

		if classViewAttrib.get('translatesAutoresizingMaskIntoConstraints', 'YES') != 'YES':
			describle +="	"+classViewName+".translatesAutoresizingMaskIntoConstraints = "+classViewAttrib.get('translatesAutoresizingMaskIntoConstraints', 'YES')+';\n'
			pass
			
		return describle
