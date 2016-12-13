#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/11/9
# version: 0.0.1
# author: Junhg
# contribute:
# 

from CollectionReusableView import JHCollectionReusableViewObject
from ViewObject import JHViewObject

class JHCollectionViewCellObject(JHCollectionReusableViewObject):

	def loadRootViewInit(self, needloadConfiguration, attribView):
		
		describle = self.loadSyntaxWithDoubleLineFeed("- (instancetype)initWithFrame:(CGRect)frame")
		describle += self.leftBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("if (self = [super initWithFrame:frame])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
		describle += self.addBasicViewAttribute("self", attribView)
		describle += self.loadAllContentSubView()
		describle += self.loadViewConfigInfos(needloadConfiguration)
		describle += self.addBlackCharacter()
		describle += self.rightBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("return self;")
		describle += self.rightBrackets()
		return describle

	def addSubViewOfContentView(self, classMethodName, attribView):
		# print 'attribView=', attribView
		describle = self.addClassMethodName("void", "loadAllContentSubView")
		describle += self.setViewProperty("self.contentView", 'frame', self.getClassFrame(attribView.get('rect', {})), '')
		describle += self.addBasicViewAttribute("self.contentView", attribView)
		return describle
