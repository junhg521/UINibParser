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

	def loadRootViewInit(self, needloadConfiguration, instanceProperty):
		"""
		It's mainly initialization used for single Xib File which types as (View、UItableViewCell、UICollectionViewCell)
		"""
		# print 'instanceProperty=', instanceProperty
		describle = self.loadSyntaxWithDoubleLineFeed("- (instancetype)initWithFrame:(CGRect)frame")
		describle += self.leftBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("if (self = [super initWithFrame:frame])")
		describle += self.addBlackCharacter()
		describle += self.leftBrackets()
		describle += self.addBasicViewAttribute("self", instanceProperty)
		describle += self.loadAllContentSubView()
		describle += self.loadViewConfigInfos(needloadConfiguration)
		describle += self.addBlackCharacter()
		describle += self.rightBrackets()
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("return self;")
		describle += self.rightBrackets()
		return describle

	def loadView(self, instanceProperty):
		# print 'instanceProperty=', instanceProperty
		describle = self.addClassMethodName("void", "loadView")
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("self.view = [[UIView alloc] initWithFrame:"+self.getClassFrame(instanceProperty.get('rect', {}))+"];")
		describle += self.addViewAttribute("self.view", instanceProperty)
		describle += self.rightBrackets()
		return describle

	def addSubViewOfContentView(self):
		return self.addClassMethodName("void", "loadAllContentSubView")

	def addSubview(self, instanceTag, instanceProperty, classMethodName):
		
		instanceName = self.attribViewInstanceName(instanceTag, instanceProperty)
		classType = self.instanceClassNameType(instanceTag, instanceProperty)
		describle = self.addClassMethodName(classType, classMethodName)

		frame = self.getClassFrame(instanceProperty.get('rect', {}))
		if len(frame) > 0:
			describle += self.loadSyntaxWithLineFeedAndSingleSpace(classType+"* "+instanceName+" = [["+classType+" alloc] initWithFrame:"+frame+"];")
			pass
		else:
			describle += self.loadSyntaxWithLineFeedAndSingleSpace(classType+"* "+instanceName+" = [["+classType+" alloc] init];")
			pass
		pass

		describle += self.addViewAttribute(instanceName, instanceProperty)
		return describle

	def addClassMethodName(self, classType, classMethodName):
		# print 'classType=',classType, ' classMethodName=',classMethodName
		describle = ""

		if classType == 'void':
			describle += self.loadSyntaxWithDoubleLineFeed("- ("+classType+")"+classMethodName)
			pass
		else:
			describle += self.loadSyntaxWithDoubleLineFeed("- ("+classType+" *"+")"+classMethodName)
			pass

		describle += self.leftBrackets()
		return describle

	def addViewAttribute(self, instanceTag, instanceProperty):
		describle = self.addBasicViewAttribute(instanceTag, instanceProperty)
		describle += self.getViewConnection(instanceTag, instanceProperty)
		return describle

	def addBasicViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=', instanceProperty
		describle = self.getViewColor(instanceTag, instanceProperty)
		describle += self.setViewProperty(instanceTag, 'canBecomeFocused', instanceProperty.get('canBecomeFocused', 'NO'), 'NO')
		describle += self.setViewProperty(instanceTag, 'multipleTouchEnabled', instanceProperty.get('multipleTouchEnabled', 'NO'), 'NO')
		describle += self.setViewProperty(instanceTag, 'exclusiveTouch', instanceProperty.get('exclusiveTouch', 'NO'), 'NO')
		describle += self.setViewProperty(instanceTag, 'autoresizesSubviews', instanceProperty.get('autoresizesSubviews', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'autoresizingMask', self.getAutoresizingMask(instanceProperty.get('autoresizingMask', {})), 'UIViewAutoresizingNone')
		describle += self.setViewProperty(instanceTag, 'clipsToBounds', instanceProperty.get('clipsToBounds', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'alpha', instanceProperty.get('alpha', '1.0'), '1.0')
		describle += self.setViewProperty(instanceTag, 'opaque', instanceProperty.get('opaque', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'clearsContextBeforeDrawing', instanceProperty.get('clearsContextBeforeDrawing', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'hidden', instanceProperty.get('hidden', 'NO'), 'NO')
		describle += self.setViewProperty(instanceTag, 'contentMode', self.getContentModel(instanceProperty.get('contentMode', {})), 'UIViewContentModeScaleToFill')
		describle += self.setViewProperty(instanceTag, 'translatesAutoresizingMaskIntoConstraints', instanceProperty.get('translatesAutoresizingMaskIntoConstraints', 'YES'), 'YES')
		describle += self.setViewProperty(instanceTag, 'userInteractionEnabled', instanceProperty.get('userInteractionEnabled', 'YES'), 'YES')
		describle += self.setViewRuntimeProperty(instanceTag, instanceProperty)
		return describle

	def setViewRuntimeProperty(self, instanceTag, instanceProperty):
		describle = ""
		
		for runtimeProperty in instanceProperty.get('userDefinedRuntimeAttributes',[]):
			userDefine = runtimeProperty.get('userDefinedRuntimeAttribute', {})
			# print 'keypath=',userDefine.get('keyPath', ''), 'instanceTag=',instanceTag
			if userDefine.get('keyPath', '').find('layer') == -1:
				classLayName = instanceTag+".layer"
				pass
			else:
				classLayName = instanceTag
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

	def getViewColor(self, instanceTag, instanceProperty):
		describle = ""

		if instanceProperty.has_key('color'):
			if type(instanceProperty.get('color')) == list:
				for color in instanceProperty.get('color', []):
					describle += self.getViewColorProperty(instanceTag, color)
					pass
				pass
			elif type(instanceProperty.get('color')) == dict:
				describle = self.getViewColorProperty(instanceTag, instanceProperty.get('color', {}))
				pass
			else:
				pass
		else:
			# print 'instanceProperty=', instanceProperty
			pass

		return describle

	def getViewColorProperty(self, instanceTag, color):
		# print 'color=', color
		viewColor = ""

		if color.get('key', '') == 'highlightedColor':
			viewColor = self.setViewProperty(instanceTag, 'highlightedTextColor', self.getClassColor(color), '')
			pass
		else:
			viewColor = self.setViewProperty(instanceTag, color.get('key', ''), self.getClassColor(color), '')
			pass

		return viewColor

	def getViewConnection(self, instanceTag, instanceProperty):
		describle = ""

		if instanceProperty.has_key('connections'):
			if type(instanceProperty.get('connections')) == list:
				for connection in instanceProperty.get('connections', []):
					outlet = connection.get('outlet',{})
					describle += self.setViewProperty(instanceTag, outlet.get('property', ''), 'self', '')
					pass
				pass
			elif type(instanceProperty.get('connections')) == dict:
				outlet = connection.get('outlet',{})
				describle = self.setViewProperty(instanceTag, outlet.get('property', ''), 'self', '')
				pass
			else:
				pass
		else:
			# print 'instanceProperty=', instanceProperty
			pass
			
		return describle

	def loadTextAttributeString(self, instanceTag, instanceProperty):
		describle = self.setViewProperty(instanceTag, 'numberOfLines', '0', '')
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("NSMutableAttributedString *attributeContent = [[NSMutableAttributedString alloc] init];")
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("[attributeContent beginEditing];")
		i = 0
		for attributedString in instanceProperty.get('attributedString',{}):
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
		describle += self.setViewProperty(instanceTag, 'attributedText', 'attributeContent', '')
		return describle

	