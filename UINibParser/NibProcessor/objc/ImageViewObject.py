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

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		describle = JHViewObject.addViewAttribute(self, classViewName, attribView)
		describle += self.addImageViewAttribute(classViewName, attribView)

		return describle

	def addImageViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView
		describle = ""

		if attribView.get('image', 'NO') != 'NO':
			describle = self.setViewProperty(classViewName, "image", "[UIImage imageNamed:@"+"\""+attribView.get('image','').encode('utf-8')+"\""+"]", "")
			pass

		if attribView.get('highlightedImage', 'NO') != 'NO':
			describle += self.setViewProperty(classViewName, "highlightedImage", "[UIImage imageNamed:@"+"\""+attribView.get('highlightedImage','').encode('utf-8')+"\""+"]", "")
			pass

		if attribView.get('highlighted', 'NO') != 'NO':
			describle += self.setViewProperty(classViewName, "highlighted", "[UIImage imageNamed:@"+"\""+attribView.get('highlighted','').encode('utf-8')+"\""+"]", "")
			pass
			
		return describle