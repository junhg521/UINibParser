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
	def __init__(self):
		pass

	def __del__(self):
		pass

	def loadView(self, needloadConfiguration, attribView):
		# print 'attribView=', attribView
		
		describle = self.newlineCharacter()
		describle += self.writeDescribleSyntax("- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier")
		describle += self.leftBrackets()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("if (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
		# describle += self.addBlackCharacter()
		# describle += JHViewObject.addViewAttribute(self, "self", attribView)
		
		attribViewId = self.attribViewTagProperty(attribView)
		if attribViewId.get('selectionStyle', {}) != 'blue':
			describle += self.addBlackCharacter()
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("self.selectionStyle = "+self.getTableViewCellSelectionStyle(attribViewId.get('selectionStyle', {}))+";")
			pass

		describle += self.addBlackCharacter()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("[self loadAllContentSubView];")
		
		if needloadConfiguration:
			describle += self.addBlackCharacter()
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("[self loadConfigCellInfo];")
			pass
		
		describle += self.addContentViewConstraint()
		describle += self.addBlackCharacter()
		describle += self.rightBrackets()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("return self;")
		describle += self.rightBrackets()

		return describle

	def addSubview(self, classViewName, classMethodName, attribView):
		pass
