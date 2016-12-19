#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/27
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHLabelObject(JHViewObject):

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView
		
		describle = JHViewObject.addViewAttribute(self, classViewName, attribView)
		describle += self.setViewProperty(classViewName, 'adjustsFontSizeToFit', attribView.get('adjustsFontSizeToFit', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'baselineAdjustment', self.getBaselineAdjustment(attribView.get('baselineAdjustment', {})), 'UIBaselineAdjustmentAlignBaselines')

		if len(attribView.get('attributedString',{})) > 0:
			describle += self.loadTextAttributeString(classViewName, attribView)
			pass
		else:
			describle += self.setViewProperty(classViewName, 'text', "@\""+attribView.get('text', '').encode('utf-8')+"\"", '')
			describle += self.setViewProperty(classViewName, 'font', self.getTextFont(attribView.get('fontDescription', {})), '')
			pass
		
		describle += self.setViewProperty(classViewName, 'textAlignment', self.getTextAlignment(attribView.get('textAlignment', 'left')), 'NSTextAlignmentLeft')
		return describle
