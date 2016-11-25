#!/usr/bin/python
# _*_ coding: UTF-8 _*_

# create: 2016/10/18
# version: 0.0.1
# author: Junhg
# contribute:
# 
__author__ = 'Junhg'

import os
from ViewObject.CommonObject import JHCommomObject
from ViewObject.ViewObject import JHViewObject
from ViewObject.BasicObject import JHBasicObject
from ViewObject.ActivityIndicatorObject import JHActivityIndicatorObject
from ViewObject.ButtonObject import JHButtonObject
from ViewObject.CollectionViewObject import JHCollectionViewObject
from ViewObject.DataPickerObject import JHDataPickerObject
from ViewObject.GLKViewObject import JHGLKViewObject
from ViewObject.ImageViewObject import JHImageViewObject
from ViewObject.LabelObject import JHLabelObject
from ViewObject.SliderObject import JHSliderObject
from ViewObject.MapViewObject import JHMapViewObject
from ViewObject.MTKViewObject import JHMTKViewObject
from ViewObject.NavigationObject import JHNavigationObject
from ViewObject.PageControlObject import JHPageControlObject
from ViewObject.PickerViewObject import JHPickerViewObject
from ViewObject.ProgressObject import JHProgressObject
from ViewObject.SceneKitViewObject import JHSceneKitViewObject
from ViewObject.ScrollViewObject import JHScrollViewObject
from ViewObject.SearchBarObject import JHSearchBarObject
from ViewObject.SegmentedControlObject import JHSegmentedControlObject
from ViewObject.StackObject import JHStackObject
from ViewObject.StepperObject import JHStepperObject
from ViewObject.SwitchObject import JHSwitchObject
from ViewObject.TabBarObject import JHTabBarObject
from ViewObject.TableViewCellObject import JHTableViewCellObject
from ViewObject.TableViewObject import JHTableViewObject
from ViewObject.TableViewObject import JHTableViewObject
from ViewObject.TextFieldObject import JHTextFieldObject
from ViewObject.TextViewObject import JHTextViewObject
from ViewObject.ToolBarObject import JHToolBarObject
from ViewObject.VisualEffectViewObject import JHVisualEffectViewObject
from ViewObject.WebViewObject import JHWebViewObject
from ViewObject.CollectionReusableView import JHCollectionReusableView
from ViewObject.CollectionViewCell import JHCollectionViewCell

class JHBaseProcessor:

	'定义通用读取JHNibParser解析Objects属性的接口，主要将objects中的属性写入相应objc/swift相关的代码'

	def __init__(self, nibParser):
		self.resouce_file_dir = os.path.dirname(nibParser.resourceFileName)
		# print 'resouce_file_dir=',self.resouce_file_dir
		self.className = nibParser.className
		self.parseType = nibParser.parseType
		pass

	def classFileDir(self):
		return self.resouce_file_dir + "/" + self.className + '.m'

	def classTempFileDir(self):
		return self.resouce_file_dir + "/" + self.className + 'Temp.m'

	def readClassFile(self):
		return open(self.classFileDir(), "r")

	def readTempClassFile(self):
		return open(self.classTempFileDir(), "w")

	def allViewTags(self):
		viewTags = ['view', 'label', 'tableViewCellContentView','segmentedControl', 'button', 'textField', 'slider', 'switch', 'customswitch','activityIndicatorView', 'progressView', 'pageControl', 'stepper', 'datePicker', 'MTKView', 'searchBar', 'tabBar', 'toolBar', 'navigationBar', 'stackView', 'tableView', 'tableViewCell', 'imageView', 'collectionView', 'textView', 'scrollView', 'visualEffectView', 'collectionViewCell']
		pass

	def viewObjectType(self, tag):
		viewObject = JHBasicObject()
		if tag == 'view' or tag == 'tableViewCellContentView':
			viewObject = JHViewObject()
			pass
		elif tag == 'label':
			viewObject = JHLabelObject()
			pass
		elif tag == 'segmentedControl':
			viewObject = JHSegmentedControlObject()
			pass
		elif tag == 'button':
			viewObject = JHButtonObject()
			pass
		elif tag == 'textField':
			viewObject = JHTextFieldObject()
			pass
		elif tag == 'slider':
			viewObject = JHSliderObject()
			pass
		elif tag == 'switch' or tag == 'customswitch':
			viewObject = JHSwitchObject()
			pass
		elif tag == 'activityIndicatorView':
			viewObject = JHActivityIndicatorObject()
			pass
		elif tag == 'progressView':
			viewObject = JHProgressObject()
			pass
		elif tag == 'pageControl':
			viewObject = JHPageControlObject()
			pass
		elif tag == 'stepper':
			viewObject = JHStepperObject()
			pass
		elif tag == 'datePicker':
			viewObject = JHDataPickerObject()
			pass
		elif tag == 'pickerView':
			viewObject = JHPickerViewObject()
			pass
		elif tag == 'MTKView':
			viewObject = JHMTKViewObject()
			pass
		elif tag == 'searchBar':
			viewObject = JHSearchBarObject()
			pass
		elif tag == 'tabBar':
			viewObject = JHTabBarObject()
			pass
		elif tag == 'toolBar':
			viewObject = JHToolBarObject()
			pass
		elif tag == 'navigationBar':
			viewObject = JHNavigationObject()
			pass
		elif tag == 'stackView':
			viewObject = JHStackObject()
			pass
		elif tag == 'tableView':
			viewObject = JHTableViewObject()
			pass
		elif tag == 'tableViewCell':
			viewObject = JHTableViewCellObject()
			pass
		elif tag == 'imageView':
			viewObject = JHImageViewObject()
			pass
		elif tag == 'collectionView':
			viewObject = JHCollectionViewObject()
			pass
		elif tag == 'textView':
			viewObject = JHTextViewObject()
			pass
		elif tag == 'scrollView':
			viewObject = JHScrollViewObject()
			pass
		elif tag == 'visualEffectView':
			viewObject = JHVisualEffectViewObject()
			pass
		elif tag == 'webView':
			viewObject = JHWebViewObject()
			pass
		elif tag == 'glkView':
			viewObject = JHGLKViewObject()
			pass
		elif tag == 'mapView':
			viewObject = JHMapViewObject()
			pass
		elif tag == 'sceneKitView':
			viewObject = JHSceneKitViewObject()
			pass
		elif tag == 'collectionReusableView':
			viewObject = JHCollectionReusableView()
			pass
		elif tag == 'collectionViewCell':
			viewObject = JHCollectionViewCell()
			pass
		else:
			print 'tag=',tag
			pass
		return viewObject

class JHObjcProcessor(JHBaseProcessor, JHCommomObject):
	'将parseResourceManager解析后的文件保存到实现文件中'

	def __init__(self, nibParser):
		JHBaseProcessor.__init__(self, nibParser)
		self.outletViews = nibParser.outletViews
		self.attribViews = nibParser.attribViews
		self.needloadConfiguration = int(nibParser.needloadConfiguration)
		self.allMethodNames = []
		pass

	def writeSyntaxWithSingleLineFeed(self, syntax, writeFileHandle):
		writeFileHandle.write(syntax+self.newlineCharacter())
		pass

	def writeSyntaxWithDoubleLineFeed(self, syntax, writeFileHandle):
		writeFileHandle.write(self.newlineCharacter()+syntax+self.newlineCharacter())
		pass

	def writeSingleBackCharacter(self, writeFileHandle):
		writeFileHandle.write(self.addBlackCharacter())
		pass

	def writeDoubleBackCharacter(self, writeFileHandle):
		writeFileHandle.write(self.addBlackCharacter())
		pass 

	def processing(self):
		# print 'attribViews=',self.attribViews
		analyseAttrib = self.analyseAttribView(self.attribViews)
		attribView = analyseAttrib[0]
		subViews = analyseAttrib[1]
		# print 'attribView=', attribView, 'subViews=',subViews
		
		try:
			subMethodNames = []
			readFileHandle = self.readClassFile()
			writeFileHandle = self.readTempClassFile()
			line = readFileHandle.readline()
			lineEdge = False
			while line !='':
				writeFileHandle.write(line)
				line = line.strip()
				if self.containObj(line,'@interface') and self.containObj(line,self.className):
					lineEdge = True
					# self.loadIBOutletProperty(self.outletViews,subViews,writeFileHandle)
				elif self.containObj(line,'@implementation') and self.containObj(line,self.className):
					lineEdge = True
					if len(subViews) > 0:
						self.writeSyntaxWithDoubleLineFeed("#pragma mark - loadAllSubViews",writeFileHandle)
						subMethodNames = self.loadAllSubView(subViews, writeFileHandle)
					self.loadView(attribView, subMethodNames, subViews, writeFileHandle)
					pass
				elif line.find("[super viewDidLoad];") >= 0 and lineEdge:
					if len(subMethodNames) > 0:
						self.loadAllSubViewProperty('self.view', subMethodNames, writeFileHandle) 
						if type(self.attribViewTagProperty(attribView)) == dict:
							self.loadViewConstranit('self.view', subMethodNames, self.attribViewTagProperty(attribView).get('id', ''),attribView.get('constraints', []),writeFileHandle)
							pass
						pass
					pass
				elif self.containObj(line,'@end'):
					lineEdge = False
					pass
				else:
					pass

				line = readFileHandle.readline()
				pass
		except Exception as e:
			print "crashed when parser "+self.resouce_file_dir+self.className+".xib"
			os.remove(self.classTempFileDir())
			raise
		else:
			os.remove(self.classFileDir())
			os.rename(self.classTempFileDir(),self.classFileDir())
		finally:
			print "finish parsor "+self.resouce_file_dir+"/"+self.className+".xib"
			readFileHandle.close()
			writeFileHandle.close()
			pass

	# def loadIBOutletProperty(self, attribView, subView,writeFileHandle):
	# 	# print 'subView=',subView
	# 	for attrib in attribView:
	# 		if attrib.get('property','') == 'view':
	# 			continue
	# 		else:
	# 			classType = self.findSubViewWithTag(subView,attrib.get('destination',''))
	# 			if len(classType) > 0:
	# 				self.writeSyntaxWithSingleLineFeed("@property (nonatomic, strong) "+classType+" *"+attrib.get('property','')+";", writeFileHandle)
	# 				pass
	# 			pass
	# 		pass
	# 	pass

	# def findSubViewWithTag(self, attribViews, attributeProperty):
	# 	for subAttribView in attribViews:
	# 		for (tag,attrib) in subAttribView.items():
	# 			# print 'tag=',tag,' attrib=',attrib
	# 			if type(attrib) == list:
	# 				propertyTag = self.findSubViewWithTag(attrib,attributeProperty)
	# 				if len(propertyTag) > 0:
	# 					return propertyTag
	# 			elif type(attrib) == dict and attrib.get('id','') == attributeProperty:
	# 				return self.objcClassNameType(tag)
	# 			pass
	# 		pass
	# 	return ''

	def loadView(self, attribView, subMethodNames, subViews, writeFileHandle):
		# print 'attribView=', attribView
		# print "subMethodNames=",subMethodNames, 'subViews=', subViews

		classViewName = self.attribViewTag(attribView)
		viewObject = self.viewObjectType(classViewName)
		classMethodName = self.attribViewViewMethod(attribView)

		if self.parseType == 'tableViewCell' or self.parseType == 'collectionViewCell':
			self.writeSyntaxWithDoubleLineFeed("#pragma mark - lifeCycle",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(viewObject.loadView(self.needloadConfiguration, attribView), writeFileHandle)

			if len(subMethodNames) > 0:
				self.writeSyntaxWithDoubleLineFeed("#pragma mark - loadContentViewSubviews",writeFileHandle)
				self.writeSyntaxWithSingleLineFeed("- (void)loadAllContentSubView",writeFileHandle)
				self.writeSyntaxWithSingleLineFeed(self.leftBrackets(),writeFileHandle)
				for subMethod in subMethodNames:
					self.writeSingleBackCharacter(writeFileHandle)
					self.writeSyntaxWithSingleLineFeed("[self "+subMethod+"];",writeFileHandle)
					pass
				# contentAttrib = self.analyseAttribView(subViews)
				# if type(self.attribViewTagProperty(contentAttrib[0])) == dict:
				# 	self.loadViewConstranit('self.contentView', subMethodNames, self.attribViewTagProperty(contentAttrib[0]).get('id', ''), attribView.get('constraints', []), writeFileHandle)
				# 	pass
				self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)
				pass
			pass
		elif self.parseType == 'collectionReusableView':
			self.writeSyntaxWithSingleLineFeed(self.newlineCharacter(),writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("#pragma mark - lifeCycle",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(viewObject.loadView(self.needloadConfiguration, attribView), writeFileHandle)
			self.loadAllSubViewProperty('self', subMethodNames, writeFileHandle)
			if type(self.attribViewTagProperty(attribView)) == dict:
				self.loadViewConstranit('self', subMethodNames, self.attribViewTagProperty(attribView).get('id', ''), attribView.get('constraints', []), writeFileHandle)
				pass
			self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("return self;",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)
			pass
		elif self.parseType == 'parseOther':
			self.writeSyntaxWithSingleLineFeed(self.newlineCharacter(),writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("#pragma mark - lifeCycle",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(viewObject.loadInitialization(self.needloadConfiguration, attribView), writeFileHandle)

			self.writeSyntaxWithSingleLineFeed("#pragma mark - load contentView subviews", writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("- (void)loadAllContentSubView", writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(self.leftBrackets(), writeFileHandle)
			self.loadAllSubViewProperty('self', subMethodNames, writeFileHandle)
			if type(self.attribViewTagProperty(attribView)) == dict:
				self.loadViewConstranit('self', subMethodNames, self.attribViewTagProperty(attribView).get('id', ''), attribView.get('constraints', []), writeFileHandle)
				pass
			self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)
			pass
		else:
			self.writeSyntaxWithDoubleLineFeed("#pragma mark - lifeCycle",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(viewObject.loadView(self.needloadConfiguration, attribView), writeFileHandle)
			pass
		pass

	def loadAllSubView(self, attribViews, writeFileHandle):
		methodNames = []
		for subAttribView in attribViews:
			attribView = {}
			subViews = []
			for (tag,attrib) in subAttribView.items():
				if tag == 'subviews':
					subViews = attrib
					pass
				else:
					attribView[tag] = attrib
					pass
				pass

			if len(subViews) > 0:
				methodName = self.loadSubView(attribView, self.loadAllSubView(subViews, writeFileHandle), writeFileHandle)
				pass
			else:
				methodName = self.loadSubView(attribView, [], writeFileHandle)
				pass

			methodNames.append(methodName);
			self.allMethodNames.append(methodName)
			# print 'attribView=', attribView
			pass
		return methodNames

	def loadSubView(self, attribView, subMethodNames, writeFileHandle):
		# print 'attribView=',attribView ' subMethodNames=',subMethodNames

		classViewName = self.loadViewProperty(attribView, writeFileHandle)
		self.loadAllSubViewProperty(classViewName, subMethodNames, writeFileHandle)
		self.loadViewConstranit(classViewName, subMethodNames, self.attribViewTagProperty(attribView).get('id', ''), attribView.get('constraints', []), writeFileHandle)
		self.loadOutletProperty(classViewName, attribView, writeFileHandle)
		self.writeSingleBackCharacter(writeFileHandle)
		self.writeSyntaxWithSingleLineFeed("return "+classViewName+";",writeFileHandle)
		self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)

		return self.attribViewViewMethod(attribView)

	def loadViewProperty(self, attribView, writeFileHandle):
		# print 'attribView=',attribView

		classViewName = self.attribViewTag(attribView)
		viewObject = self.viewObjectType(classViewName)
		classMethodName = self.attribViewViewMethod(attribView)

		if self.parseType == 'tableViewCell' and attribView.has_key('tableViewCellContentView'):
			self.writeSyntaxWithSingleLineFeed(viewObject.addClassMethodName(self.objcClassNameType(classViewName), classMethodName), writeFileHandle)
			classViewName = "self.contentView"
			pass
		elif self.parseType == 'collectionViewCell' and self.attribViewTagProperty(attribView).get('key','') == 'contentView':
			self.writeSyntaxWithSingleLineFeed(viewObject.addClassMethodName(self.objcClassNameType(classViewName), classMethodName), writeFileHandle)
			classViewName = "self.contentView"
			pass
		else:
			# print 'viewObject=',viewObject, 'classMethodName=',classMethodName
			self.writeSyntaxWithSingleLineFeed(viewObject.addSubview(classViewName, classMethodName, attribView), writeFileHandle)
			pass

		self.writeSyntaxWithSingleLineFeed(viewObject.addViewAttribute(classViewName, attribView), writeFileHandle)
		pass
		return classViewName

	def loadAllSubViewProperty(self, parentView, subMethodNames, writeFileHandle):
		# print 'parentView=',parentView, ' subMethodNames=',subMethodNames

		for subMethod in subMethodNames:
			self.writeSingleBackCharacter(writeFileHandle)
			viewTag = self.attribViewMethodTag(subMethod)
			classType = self.objcClassNameType(viewTag)
			self.writeSyntaxWithSingleLineFeed(classType+" *"+subMethod+" = [self "+subMethod+"];", writeFileHandle)
			self.writeSingleBackCharacter(writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("["+parentView+" addSubview:"+subMethod+"];", writeFileHandle)
			pass
		pass

	def loadViewConstranit(self, parentView, subMethodNames, viewId, attribViews, writeFileHandle):
		# print 'parentView=',parentView, ' subMethodNames=',subMethodNames

	 	for attribViewConstraint in list(attribViews):
	 		# print 'attribViewConstraint=',attribViewConstraint
	 		attribView = attribViewConstraint.get('constraint', {})
	 		firstItem = attribView.get('firstItem', '')
	 		firstAttribute = attribView.get('firstAttribute', '')
	 		secondItem = attribView.get('secondItem', '')
	 		secondAttribute = attribView.get('secondAttribute', '')
	 		multiplier = attribView.get('multiplier', '1.0')
	 		priority = attribView.get('priority', '1000')
	 		constant = attribView.get('constant', '0')
	 		relation = attribView.get('relation', 'equal')

	 		firstItemView = self.attribViewName(self.allMethodNames, firstItem)
	 		secodeItemView = self.attribViewName(self.allMethodNames, secondItem)
	 		if viewId == secondItem:
	 			secodeItemView = parentView
	 			pass

	 		if len(firstItem) == 0 and len(secondItem) > 0:
	 			firstItemView = parentView
	 			pass

	 		if len(secondItem) == 0:
	 			firstItemView = parentView
	 			secodeItemView = "nil"
	 			secondAttribute = "notAnAttribute"
	 			pass

	 		print 'firstItem=', firstItem, 'secondItem=', secondItem, ' subMethodNames=',self.allMethodNames

	 		constraintProperty = self.getClassOutletProperty(self.outletViews, attribView.get('id',''))
	 		describle = self.constraintMake(firstItemView, secodeItemView, firstAttribute, secondAttribute, multiplier, relation, constant)
	 		if len(constraintProperty) > 0:
	 			self.writeSingleBackCharacter(writeFileHandle)
	 			self.writeSyntaxWithSingleLineFeed(constraintProperty+" = "+describle+"];", writeFileHandle)
	 			self.writeSingleBackCharacter(writeFileHandle)
	 			self.writeSyntaxWithSingleLineFeed("["+parentView+" addConstraint:"+constraintProperty+"];", writeFileHandle)
	 			pass
	 		else:
	 			self.writeSingleBackCharacter(writeFileHandle)
	 			self.writeSyntaxWithSingleLineFeed("["+parentView+" addConstraint:"+describle+"];", writeFileHandle)
	 			pass
	 		pass
	 	pass

	def loadOutletProperty(self, classViewName, attribView, writeFileHandle):
		# print "attribView=", attribView

		attribViewProperty = self.attribViewTagProperty(attribView)
		outletProperty = self.getClassOutletProperty(self.outletViews, attribViewProperty.get('id',''))
		if len(outletProperty) > 0:
			self.writeSingleBackCharacter(writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(outletProperty+" = "+classViewName+";",writeFileHandle)
			pass
		pass

	def getClassOutletProperty(self, IBoutViews, classViewId):
		outletProperty=""
		for proprtyView in IBoutViews:
			if proprtyView.get('destination','') == classViewId:
				outletProperty = "self."+proprtyView.get('property','')
				break
			pass
		return outletProperty

	def analyseAttribView(self, attribViews):
		attribView = {}
		subView = []
		for subAttribView in attribViews:
			for (tag,attrib) in subAttribView.items():
				if tag == 'subviews':
					subView = attrib
					pass
				else:
					attribView[tag] = attrib
					pass
			pass
		return (attribView, subView)
