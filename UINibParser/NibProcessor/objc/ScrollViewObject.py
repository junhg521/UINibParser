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

	def addViewAttribute(self, instanceTag, instanceProperty):
		# print 'attribView=', attribView
		describle = JHViewObject.addViewAttribute(self, instanceTag, instanceProperty)
		describle += self.addScrollViewAttribute(instanceTag, instanceProperty)
		return describle

	def addScrollViewAttribute(self, instanceTag, instanceProperty):
		# print 'attribView=', attribView
		describle = self.setViewProperty(instanceTag, 'directionalLockEnabled', instanceProperty.get('directionalLockEnabled', 'NO'), 'NO')
		describle += self.setViewProperty(instanceTag, 'bounces', instanceProperty.get('bounces', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'alwaysBounceVertical', instanceProperty.get('alwaysBounceVertical', 'NO'), 'NO')
		describle += self.setViewProperty(instanceTag, 'alwaysBounceHorizontal', instanceProperty.get('alwaysBounceHorizontal', 'NO'), 'NO')
		describle += self.setViewProperty(instanceTag, 'pagingEnabled', instanceProperty.get('pagingEnabled', 'NO'), 'NO')
		describle += self.setViewProperty(instanceTag, 'scrollEnabled', instanceProperty.get('scrollEnabled', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'showsHorizontalScrollIndicator', instanceProperty.get('showsHorizontalScrollIndicator', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'showsVerticalScrollIndicator', instanceProperty.get('showsVerticalScrollIndicator', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'tracking', instanceProperty.get('tracking', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'dragging', instanceProperty.get('dragging', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'decelerating', instanceProperty.get('decelerating', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'delaysContentTouches', instanceProperty.get('delaysContentTouches', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'canCancelContentTouches', instanceProperty.get('canCancelContentTouches', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'bouncesZoom', instanceProperty.get('bouncesZoom', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'zooming', instanceProperty.get('zooming', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'zoomBouncing', instanceProperty.get('zoomBouncing', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'scrollsToTop', instanceProperty.get('scrollsToTop', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'keyboardDismissMode', self.getScrollViewKeyboardDismissMode(instanceProperty.get('keyboardDismissMode', 'none')), 'UIScrollViewKeyboardDismissModeNone')
		return describle
