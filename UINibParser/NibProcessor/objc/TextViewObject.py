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

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView
		describle = JHViewObject.addViewAttribute(self, classViewName, attribView)

		if len(attribView.get('attributedString',{})) > 0:
			describle += self.loadTextAttributeString(classViewName, attribView)
			pass
		else:
			attribViewId = self.attribViewTagProperty(attribView)
			describle += self.setViewProperty(classViewName, 'text', "@\""+attribViewId.get('text', '').encode('utf-8')+"\"", '')
			describle += self.setViewProperty(classViewName, 'font', self.getTextFont(attribView.get('fontDescription', {})), '')
			pass
		
		describle += self.setViewProperty(classViewName, 'textAlignment', self.getTextAlignment(attribViewId.get('textAlignment', 'left')), 'NSTextAlignmentLeft')
		return describle
		