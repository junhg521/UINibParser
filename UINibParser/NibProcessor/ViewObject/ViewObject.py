#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/24
# version: 0.0.1
# author: Junhg
# contribute:
# 

from BasicObject import JHBasicObject

class JHViewObject(JHBasicObject):
	def __init__(self):
			pass

	def __del__(self):
			pass

	def loadInitialization(self, needloadConfiguration, attribView):
		# print 'attribView=', attribView

		describle = self.newlineCharacter()
		describle += self.writeDescribleSyntax("- (instancetype)initWithFrame:(CGRect)frame")
		describle += self.leftBrackets()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("if (self = [super initWithFrame:frame])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
		describle += self.addBlackCharacter()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("[self loadAllContentSubView];")
		if needloadConfiguration > 0:
			describle += self.addBlackCharacter()
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("[self loadConfigCellInfo];")
			pass
			
		describle += self.addBasicViewAttribute("self", attribView)
		describle += self.addBlackCharacter()
		describle += self.rightBrackets()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("return self;")
		describle += self.rightBrackets()

		return describle

	def addSubview(self, classViewName, classMethodName, attribView):
		# print 'attribView=', attribView

		classType = self.objcClassNameType(classViewName)
		describle = self.addClassMethodName(classType, classMethodName)

		if len(self.getClassFrame(attribView.get('rect', {}))) > 0:
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax(classType+"* "+classViewName+" = [["+classType+" alloc] initWithFrame:"+self.getClassFrame(attribView.get('rect', {}))+"];")
			pass
		else:
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax(classType+"* "+classViewName+" = [["+classType+" alloc] init];")
			pass
		pass

		return describle

	def loadView(self, needloadConfiguration, attribView):
		# print 'attribView=', attribView

		describle = self.addClassMethodName("void", "loadView")

		if len(self.getClassFrame(attribView.get('rect', {}))) > 0:
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("self.view = [[UIView alloc] initWithFrame:"+self.getClassFrame(attribView.get('rect', {}))+"];")
			pass
		else:
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("self.view = [[UIView alloc] init];")
			pass

		describle += self.addViewAttribute("self.view", attribView)
		describle += self.rightBrackets()

		return describle

	def addClassMethodName(self, classType, classMethodName):
		# print 'classType=',classType, ' classMethodName=',classMethodName

		describle = self.newlineCharacter()
		if classType == 'void':
			describle = self.writeDescribleSyntax("- ("+classType+")"+classMethodName)
			pass
		else:
			describle = self.writeDescribleSyntax("- ("+classType+" *"+")"+classMethodName)
			pass
		describle += self.leftBrackets()

		return describle

	def addBasicViewAttribute(self, classViewName, attribView):
		# print 'attribView=', attribView
		
		describle = self.getViewColor(classViewName, attribView)
		attribViewId = self.attribViewTagProperty(attribView)
		describle += self.setViewProperty(classViewName, 'canBecomeFocused', attribViewId.get('canBecomeFocused', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'multipleTouchEnabled', attribViewId.get('multipleTouchEnabled', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'exclusiveTouch', attribViewId.get('exclusiveTouch', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'autoresizesSubviews', attribViewId.get('autoresizesSubviews', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'autoresizingMask', self.getAutoresizingMask(attribView.get('autoresizingMask', {})), 'UIViewAutoresizingNone')
		describle += self.setViewProperty(classViewName, 'clipsToBounds', attribViewId.get('clipsToBounds', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'alpha', attribViewId.get('alpha', '1.0'), '1.0')
		describle += self.setViewProperty(classViewName, 'opaque', attribViewId.get('opaque', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'clearsContextBeforeDrawing', attribViewId.get('clearsContextBeforeDrawing', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'hidden', attribViewId.get('hidden', 'NO'), 'NO')
		describle += self.setViewProperty(classViewName, 'contentMode', self.getContentModel(attribViewId.get('contentMode', {})), 'UIViewContentModeScaleToFill')
		describle += self.setViewProperty(classViewName, 'translatesAutoresizingMaskIntoConstraints', attribViewId.get('translatesAutoresizingMaskIntoConstraints', 'YES'), 'YES')
		describle += self.setViewProperty(classViewName, 'userInteractionEnabled', attribViewId.get('userInteractionEnabled', 'YES'), 'YES')
		describle += self.setViewRuntimeProperty(classViewName, attribView)
		return describle

	def addViewAttribute(self, classViewName, attribView):
		describle = self.addBasicViewAttribute(classViewName, attribView)
		describle += self.getViewConnection(classViewName, attribView)
		
		return describle

	def setViewRuntimeProperty(self, classViewName, attribView):
		describle = ""
		classLayName = classViewName+".layer"

		for runtimeProperty in attribView.get('userDefinedRuntimeAttributes',[]):
			userDefine = runtimeProperty.get('userDefinedRuntimeAttribute', {})
			if userDefine.get('type', '') == 'number':
				userDefineValue = ""
				if runtimeProperty.get('integer', '') != '':
					userDefineValue = runtimeProperty.get('integer').get('value', '')
					pass
				elif runtimeProperty.get('real', '') != '':
					userDefineValue = runtimeProperty.get('real').get('value', '')
					pass
				pass
				describle += self.setViewProperty(classLayName, userDefine.get('keyPath', ''), userDefineValue, '')
			elif userDefine.get('type', '') == 'point':
				userDefineValue = runtimeProperty.get('point')
				describle += self.setViewProperty(classLayName, userDefine.get('keyPath', ''), "CGPointMake("+userDefineValue.get('x', '0.0')+", "+userDefineValue.get('y', '0.0')+")", '')
				pass
			elif userDefine.get('type', '') == 'size':
				userDefineValue = runtimeProperty.get('size')
				describle += self.setViewProperty(classLayName, userDefine.get('keyPath', ''), "CGSizeMake("+userDefineValue.get('width', '0.0')+", "+userDefineValue.get('height', '0.0')+")", '')
				pass
			elif userDefine.get('type', '') == 'rect':
				userDefineValue = runtimeProperty.get('rect')
				describle += self.setViewProperty(classLayName, userDefine.get('keyPath', ''), "CGRectMake("+userDefineValue.get('x', '0.0')+", "+userDefineValue.get('y', '0.0')+userDefineValue.get('width', '0.0')+", "+userDefineValue.get('height', '0.0')+")", '')
				pass
			elif userDefine.get('type', '') == 'range':
				userDefineValue = runtimeProperty.get('range')
				describle += self.setViewProperty(classLayName, userDefine.get('keyPath', ''), "NSMakeRange("+userDefineValue.get('location', '0.0')+", "+userDefineValue.get('length', '0.0')+")", '')
				pass
			elif userDefine.get('type', '') == 'color':
				userDefineValue = runtimeProperty.get('color')
				describle += self.setViewProperty(classLayName, userDefine.get('keyPath', ''), self.getClassColor(userDefineValue), '')
				pass
			else:
				describle += self.setViewProperty(classLayName, userDefine.get('keyPath', ''), userDefine.get('value', ''), '')
				pass
			pass
		return describle

	def getViewColor(self, classViewName, attribView):
		describle = ""

		if attribView.has_key('color'):
			if type(attribView.get('color')) == list:
				for color in attribView.get('color', []):
					describle += self.getViewColorProperty(classViewName, color)
					pass
				pass
			elif type(attribView.get('color')) == dict:
				describle = self.getViewColorProperty(classViewName, attribView.get('color', {}))
				pass
			else:
				pass
		else:
			# print 'attribView=', attribView
			pass

		return describle

	def getViewColorProperty(self, classViewName, color):
		# print 'color=', color

		viewColor = ""
		if color.get('key', '') == 'highlightedColor':
			viewColor = self.setViewProperty(classViewName, 'highlightedTextColor', self.getClassColor(color), '')
			pass
		else:
			viewColor = self.setViewProperty(classViewName, color.get('key', ''), self.getClassColor(color), '')
			pass
		return viewColor

	def getViewConnection(self, classViewName, attribView):
		describle = ""

		if attribView.has_key('connections'):
			if type(attribView.get('connections')) == list:
				for connection in attribView.get('connections', []):
					outlet = connection.get('outlet',{})
					describle += self.setViewProperty(classViewName, outlet.get('property', ''), 'self', '')
					pass
				pass
			elif type(attribView.get('connections')) == dict:
				outlet = connection.get('outlet',{})
				describle = self.setViewProperty(classViewName, outlet.get('property', ''), 'self', '')
				pass
			else:
				pass
		else:
			# print 'attribView=', attribView
			pass
			
		return describle

	def addContentViewConstraint(self):

		describle = self.addBlackCharacter()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("self.contentView.translatesAutoresizingMaskIntoConstraints = NO;")
		describle += self.addBlackCharacter()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("[self addConstraint:[NSLayoutConstraint constraintWithItem:self \n\
                                                          attribute:NSLayoutAttributeBottom \n\
                                                          relatedBy:NSLayoutRelationEqual \n\
                                                             toItem:self.contentView \n\
                                                          attribute:NSLayoutAttributeBottom \n\
                                                         multiplier:1.0 \n\
                                                           constant:0]];")
		describle += self.addBlackCharacter()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("[self addConstraint:[NSLayoutConstraint constraintWithItem:self.contentView \n\
                                                          attribute:NSLayoutAttributeTop \n\
                                                          relatedBy:NSLayoutRelationEqual \n\
                                                             toItem:self \n\
                                                          attribute:NSLayoutAttributeTop \n\
                                                         multiplier:1.0 \n\
                                                           constant:0]];")
		describle += self.addBlackCharacter()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("[self addConstraint:[NSLayoutConstraint constraintWithItem:self.contentView \n\
                                                          attribute:NSLayoutAttributeLeading \n\
                                                          relatedBy:NSLayoutRelationEqual \n\
                                                             toItem:self \n\
                                                          attribute:NSLayoutAttributeLeading \n\
                                                         multiplier:1.0 \n\
                                                           constant:0]];")
		describle += self.addBlackCharacter()
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("[self addConstraint:[NSLayoutConstraint constraintWithItem:self \n\
                                                          attribute:NSLayoutAttributeTrailing \n\
                                                          relatedBy:NSLayoutRelationEqual \n\
                                                             toItem:self.contentView \n\
                                                          attribute:NSLayoutAttributeTrailing \n\
                                                         multiplier:1.0 \n\
                                                           constant:0]];")
		return describle

	