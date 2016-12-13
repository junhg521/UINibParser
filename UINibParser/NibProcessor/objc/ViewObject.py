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

	def loadRootViewInit(self, needloadConfiguration, attribView):
		"""
		It's mainly initialization used for single Xib File which types as (View、UItableViewCell、UICollectionViewCell)
		"""
		# print 'attribView=', attribView
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

	def loadView(self, attribView):
		# print 'attribView=', attribView
		describle = self.addClassMethodName("void", "loadView")
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("self.view = [[UIView alloc] initWithFrame:"+self.getClassFrame(attribView.get('rect', {}))+"];")
		describle += self.addViewAttribute("self.view", attribView)
		describle += self.rightBrackets()
		return describle

	def addSubViewOfContentView(self, classViewName, attribView):

		describle = self.addClassMethodName("void", "loadAllContentSubView")

		if classViewName != "self.view":
			describle += self.addBasicViewAttribute(classViewName, attribView)
			pass
		
		return describle

	def addSubview(self, classViewName, classMethodName, attribView):
		attribViewId = self.attribViewTagProperty(attribView)
		classType = self.objcClassNameType(self.attribViewTag(attribView))
		
		if attribViewId.get('customClass', '') != '':
			classType = attribViewId.get('customClass')
			pass

		describle = self.addClassMethodName(classType, classMethodName)

		if classViewName != "self.contentView":
			frame = self.getClassFrame(attribView.get('rect', {}))
			instancetViewName = self.attribViewTag(attribView)

			if len(frame) > 0:
				describle += self.loadSyntaxWithLineFeedAndSingleSpace(classType+"* "+instancetViewName+" = [["+classType+" alloc] initWithFrame:"+frame+"];")
				pass
			else:
				describle += self.loadSyntaxWithLineFeedAndSingleSpace(classType+"* "+instancetViewName+" = [["+classType+" alloc] init];")
				pass
			pass
		pass

		describle += self.addViewAttribute(classViewName, attribView)
		return describle

	def addClassMethodName(self, classType, classMethodName):
		# print 'classType=',classType, ' classMethodName=',classMethodName
		describle = ""

		if classType == 'void':
			describle = self.loadSyntaxWithDoubleLineFeed("- ("+classType+")"+classMethodName)
			pass
		else:
			describle = self.loadSyntaxWithDoubleLineFeed("- ("+classType+" *"+")"+classMethodName)
			pass

		describle += self.leftBrackets()
		return describle

	def addViewAttribute(self, classViewName, attribView):
		describle = self.addBasicViewAttribute(classViewName, attribView)
		describle += self.getViewConnection(classViewName, attribView)
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

	def setViewRuntimeProperty(self, classViewName, attribView):
		describle = ""
		
		for runtimeProperty in attribView.get('userDefinedRuntimeAttributes',[]):
			userDefine = runtimeProperty.get('userDefinedRuntimeAttribute', {})
			# print 'keypath=',userDefine.get('keyPath', ''), 'classViewName=',classViewName
			if userDefine.get('keyPath', '').find('layer') == -1:
				classLayName = classViewName+".layer"
				pass
			else:
				classLayName = classViewName
				pass

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
				describle += self.setViewProperty(classLayName, userDefine.get('keyPath', ''), self.getClassColor(userDefineValue)+".CGColor;", '')
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
		describle = self.loadSyntaxWithLineFeedAndDoubleSpace("self.contentView.translatesAutoresizingMaskIntoConstraints = NO;")
		describle += self.loadSyntaxWithLineFeedAndDoubleSpace("[self addConstraint:[NSLayoutConstraint constraintWithItem:self \n\
                                                          attribute:NSLayoutAttributeBottom \n\
                                                          relatedBy:NSLayoutRelationEqual \n\
                                                             toItem:self.contentView \n\
                                                          attribute:NSLayoutAttributeBottom \n\
                                                         multiplier:1.0 \n\
                                                           constant:0]];")
		describle += self.loadSyntaxWithLineFeedAndDoubleSpace("[self addConstraint:[NSLayoutConstraint constraintWithItem:self.contentView \n\
                                                          attribute:NSLayoutAttributeTop \n\
                                                          relatedBy:NSLayoutRelationEqual \n\
                                                             toItem:self \n\
                                                          attribute:NSLayoutAttributeTop \n\
                                                         multiplier:1.0 \n\
                                                           constant:0]];")
		describle += self.loadSyntaxWithLineFeedAndDoubleSpace("[self addConstraint:[NSLayoutConstraint constraintWithItem:self.contentView \n\
                                                          attribute:NSLayoutAttributeLeading \n\
                                                          relatedBy:NSLayoutRelationEqual \n\
                                                             toItem:self \n\
                                                          attribute:NSLayoutAttributeLeading \n\
                                                         multiplier:1.0 \n\
                                                           constant:0]];")
		describle += self.loadSyntaxWithLineFeedAndDoubleSpace("[self addConstraint:[NSLayoutConstraint constraintWithItem:self \n\
                                                          attribute:NSLayoutAttributeTrailing \n\
                                                          relatedBy:NSLayoutRelationEqual \n\
                                                             toItem:self.contentView \n\
                                                          attribute:NSLayoutAttributeTrailing \n\
                                                         multiplier:1.0 \n\
                                                           constant:0]];")
		return describle

	def loadTextAttributeString(self, classViewName, attribView):
		describle = self.setViewProperty(classViewName, 'numberOfLines', '0', '')
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("NSMutableAttributedString *attributeContent = [[NSMutableAttributedString alloc] init];")
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("[attributeContent beginEditing];")
		i = 0
		for attributedString in attribView.get('attributedString',{}):
			fragment = attributedString.get('fragment', '')
			subContent = fragment.get('content', '').encode('utf-8')
			length = str("[@"+"\""+subContent+"\""+" length]")
			attributeName = "attribute"+str(i)

			describle += self.loadSyntaxWithLineFeedAndSingleSpace("NSMutableAttributedString *"+attributeName+" = [[NSMutableAttributedString alloc] initWithString:@"+"\""+subContent+"\"];")
			
			if attributedString.has_key('font'):
				describle += self.loadSyntaxWithLineFeedAndSingleSpace("["+attributeName+" addAttribute:NSFontAttributeName value:"+self.getTextFont(attributedString.get('font',{}))+" range:NSMakeRange(0, "+length+")];")
				pass

			if attributedString.has_key('color'):
				describle += self.loadSyntaxWithLineFeedAndSingleSpace("["+attributeName+" addAttribute:NSForegroundColorAttributeName value:"+self.getClassColor(attributedString.get('color',{}))+" range:NSMakeRange(0, "+length+")];")
				pass

			describle += self.loadSyntaxWithLineFeedAndSingleSpace("[attributeContent appendAttributedString:"+attributeName+"];")
			i = i + 1
			pass
			
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("[attributeContent endEditing];")
		describle += self.setViewProperty(classViewName, 'attributedText', 'attributeContent', '')
		return describle

	