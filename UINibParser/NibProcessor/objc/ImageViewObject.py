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

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		describle = JHViewObject.addViewAttribute(self, classViewName, attribView)
		describle += self.addImageViewAttribute(classViewName, attribView)

		return describle

	def addImageViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		classViewAttrib = self.attribViewTagProperty(attribView)
		describle = ""

		if classViewAttrib.get('image', 'NO') != 'NO':
			describle = self.setViewProperty(classViewName, "image", "[UIImage imageNamed:@"+"\""+classViewAttrib.get('image','').encode('utf-8')+"\""+"]", "")
			pass

		if classViewAttrib.get('highlightedImage', 'NO') != 'NO':
			describle += self.setViewProperty(classViewName, "highlightedImage", "[UIImage imageNamed:@"+"\""+classViewAttrib.get('highlightedImage','').encode('utf-8')+"\""+"]", "")
			pass

		if classViewAttrib.get('highlighted', 'NO') != 'NO':
			describle += self.setViewProperty(classViewName, "highlighted", "[UIImage imageNamed:@"+"\""+classViewAttrib.get('highlighted','').encode('utf-8')+"\""+"]", "")
			pass
			
		return describle