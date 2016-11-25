#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/21
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHScrollViewObject(JHViewObject):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		describle = JHViewObject.addViewAttribute(self, classViewName, attribView)
		describle += self.addScrollViewAttribute(classViewName, attribView)
		
		return describle

	def addScrollViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView

		describle = self.setViewProperty(classViewName, 'directionalLockEnabled', attribView.get('directionalLockEnabled', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'bounces', attribView.get('bounces', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'alwaysBounceVertical', attribView.get('alwaysBounceVertical', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'alwaysBounceHorizontal', attribView.get('alwaysBounceHorizontal', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'pagingEnabled', attribView.get('pagingEnabled', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'scrollEnabled', attribView.get('scrollEnabled', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'showsHorizontalScrollIndicator', attribView.get('showsHorizontalScrollIndicator', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'showsVerticalScrollIndicator', attribView.get('showsVerticalScrollIndicator', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'tracking', attribView.get('tracking', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'dragging', attribView.get('dragging', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'decelerating', attribView.get('decelerating', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'delaysContentTouches', attribView.get('delaysContentTouches', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'canCancelContentTouches', attribView.get('canCancelContentTouches', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'bouncesZoom', attribView.get('bouncesZoom', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'zooming', attribView.get('zooming', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'zoomBouncing', attribView.get('zoomBouncing', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'scrollsToTop', attribView.get('scrollsToTop', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'keyboardDismissMode', attribView.get('keyboardDismissMode', 'none'), 'none')

		return describle
