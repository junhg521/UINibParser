#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/11/9
# version: 0.0.1
# author: Junhg
# contribute:
# 

from CollectionReusableView import JHCollectionReusableView
from ViewObject import JHViewObject

class JHCollectionViewCell(JHCollectionReusableView):

	def loadRootViewInit(self, needloadConfiguration, attribView):
		# print 'attribView=', attribView
		describle = self.loadSyntaxWithDoubleLineFeed("- (instancetype)initWithFrame:(CGRect)frame")
		describle += self.leftBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("if (self = [super initWithFrame:frame])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
		describle += JHViewObject.addBasicViewAttribute(self, "self", attribView)
		describle += self.loadSyntaxWithLineFeedAndDoubleSpace("[self loadAllContentSubView];")
		describle += self.addContentViewConstraint()
		describle += self.addBlackCharacter()
		describle += self.rightBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("return self;")
		describle += self.rightBrackets()
		return describle

	def loadView(self, attribView):
		# print 'attribView=', attribView
		describle = self.addClassMethodName("UIView", "loadAllContentSubView")
		describle += self.setViewProperty("self.contentView", 'frame', self.getClassFrame(attribView.get('rect', {})), '')
		describle += self.addViewAttribute("self.contentView", attribView)
		describle += self.rightBrackets()
		return describle
