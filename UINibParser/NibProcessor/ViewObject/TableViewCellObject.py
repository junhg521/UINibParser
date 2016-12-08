#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/11/1
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHTableViewCellObject(JHViewObject):

	def loadRootViewInit(self, needloadConfiguration, attribView):
		# print 'attribView=', attribView
		describle = self.loadSyntaxWithDoubleLineFeed("- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier")
		describle += self.leftBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
	
		attribViewId = self.attribViewTagProperty(attribView)

		if attribViewId.get('selectionStyle', {}) != 'blue':
			describle += self.loadSyntaxWithLineFeedAndDoubleSpace("self.selectionStyle = "+self.getTableViewCellSelectionStyle(attribViewId.get('selectionStyle', {}))+";")
			pass

		if needloadConfiguration:
			describle += self.loadSyntaxWithLineFeedAndDoubleSpace("[self loadConfigCellInfo];")
			pass

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
		return describle
