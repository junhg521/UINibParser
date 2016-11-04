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

	# 获取属性字段Tag值
	def attribViewTag(self, attribView):
		attribView = self.findAttribViewTagAndProperty(attribView)
		return attribView[0]
			

	# 获取属性的tag的attrib值
	def attribViewTagProperty(self, attribView):
		attribView = self.findAttribViewTagAndProperty(attribView)
		return attribView[1]

	def attribViewNameID(self, attribView):
		viewAttrIdValue = self.attribViewTagProperty(attribView)
		if len(viewAttrIdValue) > 0:
			return viewAttrIdValue.get('id', '')
		return ''

	def attribViewViewMethod(self, attribView):
		attribId = self.attribViewNameID(attribView)
		return "loadSubView_"+attribId.replace('-', '_')

	def attribViewMethodNameId(self, viewMethodName):
		length = len("loadSubView_")
		if len(viewMethodName) > length:
			nameId = viewMethodName[length:]
			viewId = nameId.replace('_', '-')
			return viewId
		pass
		return ''
		
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
		elif tag == 'switch':
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
			className = 'UIDataPicker'
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
			className = 'UICcollectionView'
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
		else:
			className = ''
		return className
		
	def layoutAttribute(self, layout):
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
		
	def layoutRelation(self, relation):
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
