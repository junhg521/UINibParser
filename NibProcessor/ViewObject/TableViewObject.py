#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/11/1
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHTableViewObject(JHViewObject):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def addSubview(self, attribView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		classViewAttrib = self.attribViewTagProperty(attribView)
		describle = JHViewObject.addSubview(self,attribView)
		connections = attribView.get('connections', {})
		
		for connection in connections:
			outlets = connection.get('outlet', {})
			describle +="	"+classViewName+"."+action.get('property','')+" = self;\n"
			pass
		return describle
		