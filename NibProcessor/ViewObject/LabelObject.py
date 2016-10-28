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
	def __init__(self):
		pass

	def __del__(self):
		pass

	def addSubview(self, attribView, isLoadView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		classViewAttrib = self.attribViewTagProperty(attribView)
		textAligment = self.getTextAlignment(classViewAttrib.get('textAlignment', 'NSTextAlignmentLeft'))
		lineAdjustment = self.getBaselineAdjustment(classViewAttrib.get('baselineAdjustment', 'UIBaselineAdjustmentAlignBaselines'))
		font = self.getTextFont(attribView.get('fontDescription', {}))
		attributedStrings = attribView.get('attributedString',{})
		classColors = attribView.get('color', {})

		describle = JHViewObject.addSubview(self,attribView,False)

		if classViewAttrib.get('adjustsFontSizeToFit', 'NO') != 'NO':
			describle +="	"+classViewName+".adjustsFontSizeToFitWidth = "+classViewAttrib.get('adjustsFontSizeToFit', 'NO')+';\n'
			pass

		if lineAdjustment != 'UIBaselineAdjustmentAlignBaselines':
			describle +="	"+classViewName+".baselineAdjustment = "+lineAdjustment+';\n'
			pass

		if len(attributedStrings) > 0:
			describle +="	"+classViewName+".numberOfLines = 0;\n"
			describle += "	NSMutableAttributedString *attributeContent = [[NSMutableAttributedString alloc] init];\n"
			describle +="	[attributeContent beginEditing];\n"
			i = 0
			for attributedString in attributedStrings:
				fragment = attributedString.get('fragment', '')
				subContent = fragment.get('content', '')
				length = str("[@"+"\""+subContent+"\""+" length]")
				attributeName = "attribute"+str(i)

				describle += "\n"
				describle += "	NSMutableAttributedString *"+attributeName+" = [[NSMutableAttributedString alloc] initWithString:@"+"\""+subContent+"\"];\n"
				if attributedString.has_key('font'):
					describle += "	["+attributeName+" addAttribute:NSFontAttributeName value:"+self.getAttributeTextFont(attributedString.get('font',{}))+" range:NSMakeRange(0, "+length+")];\n"
					pass
				if attributedString.has_key('color'):
					describle += "	["+attributeName+" addAttribute:NSForegroundColorAttributeName value:"+self.getClassColor(attributedString.get('color',{}))+" range:NSMakeRange(0, "+length+")];\n"
					pass
				describle +="	[attributeContent appendAttributedString:"+attributeName+"];\n"
				i = i + 1
				pass
			describle += "\n"
			describle +="	[attributeContent endEditing];\n"
			describle +="	"+classViewName+".attributedText = attributeContent;\n"
			pass
		else :
			describle +="	"+classViewName+".text = "+"@\""+classViewAttrib.get('text', '')+"\""+';\n'
			describle +="	"+classViewName+".font = "+font+'\n'
			for color in classColors:
				if len(color.get('key','')) > 0 and color.get('key','') == 'textColor':
					describle +="	"+classViewName+"."+color.get('key','')+" = "+self.getClassColor(color)+";\n"
					pass
				pass
			pass

		if textAligment != 'NSTextAlignmentNatural':
			describle +="	"+classViewName+".textAlignment = "+textAligment+';\n'
			pass

		if classViewAttrib.get('userInteractionEnabled', 'NO') != 'NO':
			describle +="	"+classViewName+".userInteractionEnabled = "+classViewAttrib.get('userInteractionEnabled', 'NO')+';\n'
			pass
		
		return describle

	def getAttributeTextFont(self, fontDescription):
		# print 'fontDescription = ', fontDescription
		fontSize = fontDescription.get('size', '17')
		fontType = fontDescription.get('metaFont', 'system')

		if fontType == 'boldSystem':
			return "[UIFont boldSystemFontOfSize:"+str(fontSize)+"]"
		elif fontType == 'italicSystem':
			return "[UIFont italicSystemFontOfSize:"+str(fontSize)+"]"
		else :
			return "[UIFont systemFontOfSize:"+str(fontSize)+"]"
		pass
