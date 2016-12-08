#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/27
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHLabelObject(JHViewObject):

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView
		attribViewId = self.attribViewTagProperty(attribView)
		
		describle = JHViewObject.addViewAttribute(self, classViewName, attribView)
		describle += self.setViewProperty(classViewName, 'adjustsFontSizeToFit', attribViewId.get('adjustsFontSizeToFit', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'baselineAdjustment', self.getBaselineAdjustment(attribViewId.get('baselineAdjustment', {})), 'UIBaselineAdjustmentAlignBaselines')

		if len(attribView.get('attributedString',{})) > 0:
			describle += self.setViewProperty(classViewName, 'numberOfLines', '0', '')
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("NSMutableAttributedString *attributeContent = [[NSMutableAttributedString alloc] init];")
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("[attributeContent beginEditing];")
			i = 0
			for attributedString in attribView.get('attributedString',{}):
				fragment = attributedString.get('fragment', '')
				subContent = fragment.get('content', '').encode('utf-8')
				length = str("[@"+"\""+subContent+"\""+" length]")
				attributeName = "attribute"+str(i)

				describle += self.addBlackCharacter()
				describle += self.writeDescribleSyntax("NSMutableAttributedString *"+attributeName+" = [[NSMutableAttributedString alloc] initWithString:@"+"\""+subContent+"\"];")
				if attributedString.has_key('font'):
					describle += self.addBlackCharacter()
					describle += self.writeDescribleSyntax("["+attributeName+" addAttribute:NSFontAttributeName value:"+self.getTextFont(attributedString.get('font',{}))+" range:NSMakeRange(0, "+length+")];")
					pass
				if attributedString.has_key('color'):
					describle += self.addBlackCharacter()
					describle += self.writeDescribleSyntax("["+attributeName+" addAttribute:NSForegroundColorAttributeName value:"+self.getClassColor(attributedString.get('color',{}))+" range:NSMakeRange(0, "+length+")];")
					pass
				describle += self.addBlackCharacter()
				describle += self.writeDescribleSyntax("[attributeContent appendAttributedString:"+attributeName+"];")
				i = i + 1
				pass
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("[attributeContent endEditing];")
			describle += self.setViewProperty(classViewName, 'attributedText', 'attributeContent', '')
			pass
		else:
			describle += self.setViewProperty(classViewName, 'text', "@\""+attribViewId.get('text', '').encode('utf-8')+"\"", '')
			describle += self.setViewProperty(classViewName, 'font', self.getTextFont(attribView.get('fontDescription', {})), '')
		
		describle += self.setViewProperty(classViewName, 'textAlignment', self.getTextAlignment(attribViewId.get('textAlignment', 'left')), 'NSTextAlignmentLeft')

		return describle
