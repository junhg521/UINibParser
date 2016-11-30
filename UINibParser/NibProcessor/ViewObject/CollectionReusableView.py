#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/11/9
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHCollectionReusableView(JHViewObject):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def loadView(self, needloadConfiguration, attribView):
		# print 'attribView=', attribView

		describle = self.newlineCharacter()
		describle = self.writeDescribleSyntax("- (instancetype)initWithFrame:(CGRect)frame")
		describle += self.leftBrackets()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("if (self = [super initWithFrame:frame])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
		describle += self.addBlackCharacter()
		describle += JHViewObject.addBasicViewAttribute(self, "self", attribView)
		describle += self.addBlackCharacter()
		describle += self.addBlackCharacter()
		describle +=self.writeDescribleSyntax("[self loadConfigCellInfo];")

		return describle
