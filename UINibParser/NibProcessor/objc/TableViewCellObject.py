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
		
		describle = self.loadSyntaxWithDoubleLineFeed("- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier")
		describle += self.leftBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
		describle += self.addViewAttribute("self", attribView)
		describle += self.loadAllContentSubView()
		describle += self.loadViewConfigInfos(needloadConfiguration)
		describle += self.addBlackCharacter()
		describle += self.rightBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("return self;")
		describle += self.rightBrackets()
		return describle

	def addViewAttribute(self, classViewName, attribView):
		# print "attribView=",attribView
		attribViewId = self.attribViewTagProperty(attribView)
		describle = self.addBasicViewAttribute(classViewName, attribView)
		describle += self.setViewProperty(classViewName, 'selectionStyle', self.getTableViewCellSelectionStyle(attribViewId.get('selectionStyle', {})), 'UITableViewCellSelectionStyleBlue')
		return describle

	def addSubViewOfContentView(self, classMethodName, attribView):
		# print 'attribView=', attribView
		describle = self.addClassMethodName("void", "loadAllContentSubView")
		describle += self.setViewProperty("self.contentView", 'frame', self.getClassFrame(attribView.get('rect', {})), '')
		describle += self.addBasicViewAttribute("self.contentView", attribView)
		return describle