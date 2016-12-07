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

		attribViewId = self.attribViewTagProperty(attribView)
		describle = self.setViewProperty(classViewName, 'directionalLockEnabled', attribViewId.get('directionalLockEnabled', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'bounces', attribViewId.get('bounces', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'alwaysBounceVertical', attribViewId.get('alwaysBounceVertical', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'alwaysBounceHorizontal', attribViewId.get('alwaysBounceHorizontal', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'pagingEnabled', attribViewId.get('pagingEnabled', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'scrollEnabled', attribViewId.get('scrollEnabled', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'showsHorizontalScrollIndicator', attribViewId.get('showsHorizontalScrollIndicator', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'showsVerticalScrollIndicator', attribViewId.get('showsVerticalScrollIndicator', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'tracking', attribViewId.get('tracking', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'dragging', attribViewId.get('dragging', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'decelerating', attribViewId.get('decelerating', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'delaysContentTouches', attribViewId.get('delaysContentTouches', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'canCancelContentTouches', attribViewId.get('canCancelContentTouches', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'bouncesZoom', attribViewId.get('bouncesZoom', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'zooming', attribViewId.get('zooming', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'zoomBouncing', attribViewId.get('zoomBouncing', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'scrollsToTop', attribViewId.get('scrollsToTop', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'keyboardDismissMode', attribViewId.get('keyboardDismissMode', 'none'), 'none')

		return describle
