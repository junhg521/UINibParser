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

	def loadRootViewInit(self, needloadConfiguration, instanceProperty):
		
		describle = self.loadSyntaxWithDoubleLineFeed("- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier")
		describle += self.leftBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
		describle += self.addViewAttribute("self", instanceProperty)
		describle += self.loadAllContentSubView()
		describle += self.loadViewConfigInfos(needloadConfiguration)
		describle += self.addBlackCharacter()
		describle += self.rightBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("return self;")
		describle += self.rightBrackets()
		return describle

	def addSubview(self, instanceTag, instanceProperty, classMethodName):
		instanceName = self.attribViewInstanceName(instanceTag, instanceProperty)
		classType = self.instanceClassNameType(instanceTag, instanceProperty)
		describle = self.addClassMethodName(classType, classMethodName)
		describle += self.setViewProperty(instanceName, 'frame', self.getClassFrame(instanceProperty.get('rect', {})), '')
		describle += self.addBasicViewAttribute(instanceName, instanceProperty)
		return describle

	def addViewAttribute(self, instanceTag, instanceProperty):
		# print "instanceProperty=",instanceProperty
		describle = self.addBasicViewAttribute(instanceTag, instanceProperty)
		describle += self.setViewProperty(instanceTag, 'selectionStyle', self.getTableViewCellSelectionStyle(instanceProperty.get('selectionStyle', {})), 'UITableViewCellSelectionStyleBlue')
		return describle
