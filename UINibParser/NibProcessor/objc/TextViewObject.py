#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/21
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHTextViewObject(JHViewObject):

	def addViewAttribute(self, instanceTag, instanceProperty):
		# print 'attribView=', attribView
		describle = JHViewObject.addViewAttribute(self, instanceTag, instanceProperty)

		if len(instanceProperty.get('attributedString',{})) > 0:
			describle += self.loadTextAttributeString(instanceTag, instanceProperty)
			pass
		else:
			describle += self.setViewProperty(instanceTag, 'text', "@\""+instanceProperty.get('text', '').encode('utf-8')+"\"", '')
			describle += self.setViewProperty(instanceTag, 'font', self.getTextFont(instanceProperty.get('fontDescription', {})), '')
			pass
		
		describle += self.setViewProperty(instanceTag, 'textAlignment', self.getTextAlignment(instanceProperty.get('textAlignment', 'left')), 'NSTextAlignmentLeft')
		return describle
		