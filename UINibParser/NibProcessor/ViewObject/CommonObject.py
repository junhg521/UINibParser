#!/usr/bin/python
# _*_ coding: UTF-8 _*_

# create: 2016/10/18
# modify: 2016/10/18
# version: 0.0.1
# author: Junhg
# contribute:
# 
__author__ = 'Junhg'

class JHCommomObject():
	def __init__(self):
		pass

	def __del__(self):
		pass

	def judgementViewTag(self, tag):
		isValidate = False
		className = self.objcClassNameType(tag)
		if len(className) > 0:
			isValidate = True
			pass
		return isValidate

	def containObj(self, originObj, destionationObj):
		if type(originObj) == str:
			split = originObj.split(' ')
			return split.count(destionationObj) > 0
		elif type(originObj) == list:
			return originObj.count(destionationObj) > 0
		else:
			return False

	def leftBrackets(self):
		return "{"+self.newlineCharacter()
		
	def rightBrackets(self):
		return "}"+self.newlineCharacter()

	def newlineCharacter(self):
		return "\n"

	def addBlackCharacter(self):
		return "	"

	# 获取属性字段Tag值
	def attribViewTag(self, attribView):
		attribView = self.findAttribViewTagAndProperty(attribView)
		if attribView[0] == 'switch':
			return 'custom'+attribView[0]
		else:
			return attribView[0]
		pass
			
	# 获取属性的tag的attrib值
	def attribViewTagProperty(self, attribView):
		attribView = self.findAttribViewTagAndProperty(attribView)
		return attribView[1]
		
	def attribViewViewMethod(self, attribView):
		attribId = self.attribViewTagProperty(attribView)
		viewId = attribId.get('id', '')
		return self.attribViewTag(attribView)+"__"+viewId.replace('-', '_')

	def attribViewMethodPropertyId(self, viewMethodName):
		splits = viewMethodName.split('__')
		if len(splits) > 1:
			return splits[1]
		else:
			return ""
		pass

	def attribViewMethodTag(self, viewMethodName):
		splits = viewMethodName.split('__')
		return splits[0]

	def attribViewName(self, viewMethodNames, propertyId):
		# print 'viewMethodNames=',viewMethodNames, 'propertyId=',propertyId
		
		for viewMethodName in viewMethodNames:
			if type(viewMethodName) == list:
				return self.attribViewName(viewMethodName, propertyId)
			else:
				if propertyId.replace('-', '_') == self.attribViewMethodPropertyId(viewMethodName):
					return viewMethodName

			pass
		return ""

	def attribViewNameId(self, viewMethodNames, propertyId):
		for viewMethodName in viewMethodNames:
			if propertyId == self.attribViewMethodPropertyId(viewMethodName):
				return self.attribViewMethodPropertyId(viewMethodName)
			pass
		return ""
		
	def findAttribViewTagAndProperty(self, attribView):
		for (key,value) in attribView.items():
			if len(self.objcClassNameType(key)) > 0:
				return (key,value);
			pass
		pass
		return ("","")

	def objcClassNameType(self, tag):
		className = ''
		if tag == 'view' or tag == 'tableViewCellContentView':
			className = 'UIView'
			pass
		elif tag == 'label':
			className = 'UILabel'
			pass
		elif tag == 'segmentedControl':
			className = 'UISegmentedControl'
			pass
		elif tag == 'button':
			className = 'UIButton'
			pass
		elif tag == 'textField':
			className = 'UITextField'
			pass
		elif tag == 'slider':
			className = 'UISlider'
			pass
		elif tag == 'switch' or tag == 'customswitch':
			className = 'UISwitch'
			pass
		elif tag == 'activityIndicatorView':
			className = 'UIActivityIndicatorView'
			pass
		elif tag == 'progressView':
			className = 'UIProgressView'
			pass
		elif tag == 'pageControl':
			className = 'UIPageControl'
			pass
		elif tag == 'stepper':
			className = 'UIStepper'
			pass
		elif tag == 'datePicker':
			className = 'UIDatePicker'
			pass
		elif tag == 'pickerView':
			className = 'UIPickerView'
			pass
		elif tag == 'MTKView':
			className = 'MTKView'
			pass
		elif tag == 'searchBar':
			className = 'UISearchBar'
			pass
		elif tag == 'tabBar':
			className = 'UITabBar'
			pass
		elif tag == 'toolbar':
			className = 'UIToolBar'
			pass
		elif tag == 'navigationBar':
			className = 'UINavigationBar'
			pass
		elif tag == 'stackView':
			className = 'UIStackView'
			pass
		elif tag == 'tableView':
			className = 'UITableView'
			pass
		elif tag == 'tableViewCell':
			className = 'UITtableViewCell'
			pass
		elif tag == 'imageView':
			className = 'UIImageView'
			pass
		elif tag == 'collectionView':
			className = 'UICollectionView'
			pass
		elif tag == 'textView':
			className = 'UITextView'
			pass
		elif tag == 'scrollView':
			className = 'UIScrollView'
			pass
		elif tag == 'visualEffectView':
			className = 'UIVisualEffectView'
			pass
		elif tag == 'webView':
			className = 'UIWebView'
			pass
		elif tag == 'glkView':
			className = 'GLKView'
			pass
		elif tag == 'mapView':
			className = 'MKMapView'
			pass
		elif tag == 'sceneKitView':
			className = 'UISceneKitView'
			pass
		elif tag == 'constraint':
			className = 'NSLayoutConstraint'
			pass
		elif tag == 'collectionReusableView':
			className = 'UICollectionReusableView'
			pass
		elif tag == 'collectionViewCell':
			className = 'UICollectionViewCell'
			pass
		else:
			className = ''
		return className
		
	def constraintLayoutAttribute(self, layout):
		layoutAttribute = ''

		if layout == 'left':
			layoutAttribute = 'NSLayoutAttributeLeft'
			pass
		elif layout == 'top':
			layoutAttribute = 'NSLayoutAttributeTop'
			pass
		elif layout == 'bottom':
			layoutAttribute = 'NSLayoutAttributeBottom'
			pass
		elif layout == 'leading':
			layoutAttribute = 'NSLayoutAttributeLeading'
			pass
		elif layout == 'trailing':
			layoutAttribute = 'NSLayoutAttributeTrailing'
			pass
		elif layout == 'width':
			layoutAttribute = 'NSLayoutAttributeWidth'
			pass
		elif layout == 'height':
			layoutAttribute = 'NSLayoutAttributeHeight'
			pass
		elif layout == 'centerX':
			layoutAttribute = 'NSLayoutAttributeCenterX'
			pass
		elif layout == 'centerY':
			layoutAttribute = 'NSLayoutAttributeCenterY'
			pass
		elif layout == 'lastBaseline':
			layoutAttribute = 'NSLayoutAttributeLastBaseline'
			pass
		elif layout == 'baseline':
			layoutAttribute = 'NSLayoutAttributeBaseline'
			pass
		elif layout == 'firstBaseline':
			layoutAttribute = 'NSLayoutAttributeFirstBaseline'
			pass
		elif layout == 'leftMargin':
			layoutAttribute = 'NSLayoutAttributeLeftMargin'
			pass
		elif layout == 'rightMargin':
			layoutAttribute = 'NSLayoutAttributeRightMargin'
			pass
		elif layout == 'topMargin':
			layoutAttribute = 'NSLayoutAttributeTopMargin'
			pass
		elif layout == 'bottomMargin':
			layoutAttribute = 'NSLayoutAttributeBottomMargin'
			pass
		elif layout == 'leadingMargin':
			layoutAttribute = 'NSLayoutAttributeLeadingMargin'
			pass
		elif layout == 'trailingMargin':
			layoutAttribute = 'NSLayoutAttributeTrailingMargin'
			pass
		elif layout == 'centerXWithMargins':
			layoutAttribute = 'NSLayoutAttributeCenterXWithinMargins'
			pass
		elif layout == 'centerYWithMargins':
			layoutAttribute = 'NSLayoutAttributeCenterYWithinMargins'
			pass
		elif layout == 'notAnAttribute':
			layoutAttribute = 'NSLayoutAttributeNotAnAttribute'
			pass
		else:
			pass;
		return layoutAttribute
		
	def constraintLayoutRelation(self, relation):
		layoutRelation = ''

		if relation == 'lessThanOrEqual':
			layoutRelation = 'NSLayoutRelationLessThanOrEqual'
			pass
		elif relation == 'equal':
			layoutRelation = 'NSLayoutRelationEqual'
			pass
		elif relation == 'greaterThanOrEqual':
			layoutRelation = 'NSLayoutRelationGreaterThanOrEqual'
			pass
		else :
			pass
		return layoutRelation

	def constraintMake(self, firstItemView, secodeItemView, firstAttribute, secondAttribute, multiplier, relation, constant):
		return "[NSLayoutConstraint constraintWithItem:"+firstItemView+"\n\
											 attribute:"+self.constraintLayoutAttribute(firstAttribute)+"\n\
											 relatedBy:"+self.constraintLayoutRelation(relation)+"\n\
											    toItem:"+secodeItemView+"\n\
											 attribute:"+self.constraintLayoutAttribute(secondAttribute)+"\n\
											multiplier:"+multiplier+"\n\
											  constant:"+constant+"]"
