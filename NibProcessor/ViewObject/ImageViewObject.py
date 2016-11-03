#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/26
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHImageViewObject(JHViewObject):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def addSubview(self, attribView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		classViewAttrib = self.attribViewTagProperty(attribView)

		describle = JHViewObject.addSubview(self,attribView)
		
		if classViewAttrib.has_key('image'):
			describle +="	"+classViewName+".image = [UIImage imageNamed:@"+"\""+classViewAttrib.get('image','')+"\""+"];\n"
			pass

		if classViewAttrib.has_key('highlightedImage'):
			describle +="	"+classViewName+".highlightedImage = [UIImage imageNamed:@"+"\""+classViewAttrib.get('image','')+"\""+"];\n"
			pass

		if classViewAttrib.get('highlighted','NO') != 'NO':
			describle +="	"+classViewName+".highlighted = "+classViewAttrib.get('highlighted','NO')+"];\n"
			pass

		return describle
