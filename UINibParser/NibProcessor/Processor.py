#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

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
from ViewObject.TextFieldObject import JHTextFieldObject
from ViewObject.TextViewObject import JHTextViewObject
from ViewObject.ToolBarObject import JHToolBarObject
from ViewObject.VisualEffectViewObject import JHVisualEffectViewObject
from ViewObject.WebViewObject import JHWebViewObject
from ViewObject.CollectionReusableView import JHCollectionReusableView
from ViewObject.CollectionViewCell import JHCollectionViewCell

class JHBaseProcessor(object):

	"define a common interface of reading JHNibParser class properties which will be \
	written for corresponding objc/swift related code"

	def __init__(self, nibParser):
		""" use the constructor to initialize properties of `JHBaseProcessor` class
		args:
			resourceDirname:absolute directory of resource file
			className:class name of resource file
			parseType:parse type of resource file
		"""
		self.resourceDirname = os.path.dirname(nibParser.resourceFileName)
		self.className = nibParser.className
		self.parseType = nibParser.parseType
		pass

	def classFileDir(self):
		return self.resourceDirname + "/" + self.className + '.m'

	def classTempFileDir(self):
		return self.resourceDirname + "/" + self.className + 'Temp.m'

	def readClassFile(self):
		return open(self.classFileDir(), "r")

	def readTempClassFile(self):
		return open(self.classTempFileDir(), "w")

	def writeSyntaxWithSingleLineFeed(self, syntax, writeFileHandle):
		writeFileHandle.write(syntax+self.newlineCharacter())
		pass

	def writeSyntaxWithDoubleLineFeed(self, syntax, writeFileHandle):
		writeFileHandle.write(self.newlineCharacter()+syntax+self.newlineCharacter())
		pass

	def writeSingleSpace(self, writeFileHandle):
		writeFileHandle.write(self.addBlackCharacter())
		pass

	def writeDoubleSpace(self, writeFileHandle):
		writeFileHandle.write(self.addBlackCharacter())
		pass

	def allViewObject(self):
		return ["view", "tableViewCellContentView", "label", "segmentedControl",
		"button", "textField", "slider", "switch", "customswitch", "activityIndicatorView",
		"progressView", "pageControl", "stepper", "datePicker", "pickerView", "MTKView",
		"searchBar", "tabBar", "toolBar", "navigationBar", "stackView", "tableView", 
		"tableViewCell", "imageView", "collectionView", "textView", "scrollView", "visualEffectView",
		"webView", "glkView", "mapView", "sceneKitView", "collectionReusableView", "collectionViewCell"]

	def viewObjectType(self, tag):
		viewObject = tag
		if tag == "tableViewCellContentView":
			viewObject = "view"
			pass
		elif tag == "customswitch":
			viewObject = "switch"
			pass
		else:
			pass

		return eval("JH"+viewObject[0].upper() + viewObject[1:]+"Object()")

class JHObjcProcessor(JHBaseProcessor, JHCommomObject):

	"set parsed resourece data written as objective-c code, and attempts to insert all \
	resourece files(including initialization、constarints definiton、attributes assignment、\
	add all subviews etc) to the corresponding implementation file"

	def __init__(self, nibParser):
		""" use the constructor to initialize properties of `JHObjcProcessor` class 
		args:
			outletViews:gets all node vaules of `outlet` node in xib file.
				(such as [{'destination':'','property':'','id':''},{...},...])
			attribViews:gets all node values of all `view` node in xib file.
				(such as [{'subviews':[{...}...]},{...},...])
			resources:gets all node values of `resource` node in xib file.(such as {{...},...})
			needloadConfiguration:indicates whether an alternate function for awakeFromNib neends to be loaded
			parseType:xib file type, default value is controller
			viewId: it's controller main view identify
		"""
		JHBaseProcessor.__init__(self, nibParser)
		self.outletViews = nibParser.outletViews
		self.attribViews = nibParser.attribViews
		self.needloadConfiguration = int(nibParser.needloadConfiguration)
		self.viewId = nibParser.viewId
		pass

	def processing(self):
		# print 'attribViews=',self.attribViews
	
		try:
			resourceInfos = ()
			readFileHandle = self.readClassFile()
			writeFileHandle = self.readTempClassFile()
			line = readFileHandle.readline()
			lineEdge = False
			while line !='':
				writeFileHandle.write(line)
				line = line.strip()
				if self.containObj(line, '@implementation') and self.containObj(line, self.className):
					lineEdge = True
					resourceInfos = self.loadAllResourceView(self.attribViews, writeFileHandle)
					pass
				elif line.find("[super viewDidLoad];") >= 0 and lineEdge:
					self.loadAllSubViewProperty('self.view', resourceInfos[0], writeFileHandle) 
					self.loadViewConstranit('self.view', resourceInfos[0], self.viewId, resourceInfos[1], writeFileHandle)
					for methodName in resourceInfos[2]:
						self.writeSingleSpace(writeFileHandle)
						self.writeSyntaxWithSingleLineFeed("[self "+methodName+"];", writeFileHandle)
						pass
					pass
				elif self.containObj(line, '@end'):
					lineEdge = False
					pass
				else:
					pass
				line = readFileHandle.readline()
				pass
		except Exception as e:
			print "crashed when parser "+self.resourceDirname+self.className+".xib"
			os.remove(self.classTempFileDir())
			raise
		else:
			os.remove(self.classFileDir())
			os.rename(self.classTempFileDir(),self.classFileDir())
		finally:
			print "finish parsor "+self.resourceDirname+"/"+self.className+".xib"
			readFileHandle.close()
			writeFileHandle.close()
			pass

	def loadAllResourceView(self, attribViews, writeFileHandle):
		subMethodNames = []
		constraints = []
		addSubViews = []

		if len(attribViews):
			self.writeSyntaxWithDoubleLineFeed("#pragma mark - loadAllSubViews",writeFileHandle)
			pass

		for attribView in attribViews:
			analyseAttrib = self.analyseAttribView(attribView)
			viewPropety = self.attribViewTagProperty(analyseAttrib[0])
			methodNames = self.loadAllSubView(analyseAttrib[1], writeFileHandle)
			if (viewPropety.get('id', '') == self.viewId and self.parseType == 'controller') or self.parseType != 'controller':
				subMethodNames = methodNames
				constraints = analyseAttrib[0].get('constraints', [])
				self.loadView(analyseAttrib[0], methodNames, analyseAttrib[1], writeFileHandle)
			else:
				methodName = self.loadSubView(analyseAttrib[0], methodNames, writeFileHandle)
				addSubViews.append(methodName)
			pass

		return (subMethodNames, constraints, addSubViews)

	def loadView(self, attribView, methodNames, subViews, writeFileHandle):
		# print 'attribView=', attribView
		# print "methodNames=",methodNames, 'subViews=', subViews

		classViewName = self.attribViewTag(attribView)
		viewObject = self.viewObjectType(classViewName)
		classMethodName = self.attribViewViewMethod(attribView)

		if self.parseType == 'tableViewCell' or self.parseType == 'collectionViewCell':
			self.writeSyntaxWithDoubleLineFeed("#pragma mark - lifeCycle",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(viewObject.loadView(self.needloadConfiguration, attribView), writeFileHandle)

			if len(methodNames) > 0:
				self.writeSyntaxWithDoubleLineFeed("#pragma mark - loadContentViewSubviews",writeFileHandle)
				self.writeSyntaxWithSingleLineFeed("- (void)loadAllContentSubView",writeFileHandle)
				self.writeSyntaxWithSingleLineFeed(self.leftBrackets(),writeFileHandle)
				for subMethodNames in methodNames:
					for subMethod in subMethodNames:
						self.writeSingleSpace(writeFileHandle)
						self.writeSyntaxWithSingleLineFeed("[self "+subMethod+"];",writeFileHandle)
						pass
					pass
				self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)
				pass
			pass
		elif self.parseType == 'collectionReusableView':
			self.writeSyntaxWithSingleLineFeed(self.newlineCharacter(),writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("#pragma mark - lifeCycle",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(viewObject.loadView(self.needloadConfiguration, attribView), writeFileHandle)
			self.loadAllSubViewProperty('self', methodNames, writeFileHandle)
			if type(self.attribViewTagProperty(attribView)) == dict:
				self.loadViewConstranit('self', methodNames, self.attribViewTagProperty(attribView).get('id', ''), attribView.get('constraints', []), writeFileHandle)
				pass
			self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("return self;",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)
			pass
		elif self.parseType == 'view':
			self.writeSyntaxWithSingleLineFeed(self.newlineCharacter(),writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("#pragma mark - lifeCycle",writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(viewObject.loadInitialization(self.needloadConfiguration, attribView), writeFileHandle)

			self.writeSyntaxWithSingleLineFeed("#pragma mark - load contentView subviews", writeFileHandle)
			self.writeSyntaxWithSingleLineFeed("- (void)loadAllContentSubView", writeFileHandle)
			self.writeSyntaxWithSingleLineFeed(self.leftBrackets(), writeFileHandle)
			self.loadAllSubViewProperty('self', methodNames, writeFileHandle)
			if type(self.attribViewTagProperty(attribView)) == dict:
				self.loadViewConstranit('self', methodNames, self.attribViewTagProperty(attribView).get('id', ''), attribView.get('constraints', []), writeFileHandle)
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
		for attribView in attribViews:
			analyseAttrib = self.analyseAttribView(attribView)
			subMethodeNames = []

			if len(analyseAttrib[1]) > 0:
				subMethodeNames = self.loadAllSubView(analyseAttrib[1], writeFileHandle)
				pass

			methodName = self.loadSubView(analyseAttrib[0], subMethodeNames, writeFileHandle)
			methods = {}
			methods[methodName] = subMethodeNames
			methodNames.append(methods);
			# print 'attribView=', attribView
			pass
		return methodNames

	def loadSubView(self, attribView, methodNames, writeFileHandle):
		# print 'attribView=',attribView ' subMethodNames=',subMethodNames

		classViewName = self.loadViewProperty(attribView, writeFileHandle)
		self.loadAllSubViewProperty(classViewName, methodNames, writeFileHandle)
		self.loadViewConstranit(classViewName, methodNames, self.attribViewTagProperty(attribView).get('id', ''), attribView.get('constraints', []), writeFileHandle)
		self.loadOutletProperty(classViewName, attribView, writeFileHandle)
		self.writeSingleSpace(writeFileHandle)
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

	def loadAllSubViewProperty(self, parentView, methodNames, writeFileHandle):
		# print 'parentView=',parentView, ' methodNames=',methodNames

		for subMethodNames in methodNames:
			for subMethod in subMethodNames.keys():
				self.writeSingleSpace(writeFileHandle)
				viewTag = self.attribViewMethodTag(subMethod)
				classType = self.objcClassNameType(viewTag)
				self.writeSyntaxWithSingleLineFeed(classType+" *"+subMethod+" = [self "+subMethod+"];", writeFileHandle)
				self.writeSingleSpace(writeFileHandle)
				self.writeSyntaxWithSingleLineFeed("["+parentView+" addSubview:"+subMethod+"];", writeFileHandle)
				pass
			pass	
		pass

	def loadViewConstranit(self, parentView, methodNames, viewId, attribViews, writeFileHandle):
		# print 'parentView=',parentView, ' methodNames=',methodNames

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

	 		firstItemView = self.attribViewName(methodNames, firstItem)
	 		secodeItemView = self.attribViewName(methodNames, secondItem)
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

	 		constraintProperty = self.getClassOutletProperty(self.outletViews, attribView.get('id',''))
	 		describle = self.constraintMake(firstItemView, secodeItemView, firstAttribute, secondAttribute, multiplier, relation, constant)
	 		if len(constraintProperty) > 0:
	 			self.writeSingleSpace(writeFileHandle)
	 			self.writeSyntaxWithSingleLineFeed(constraintProperty+" = "+describle+";", writeFileHandle)
	 			self.writeSingleSpace(writeFileHandle)
	 			self.writeSyntaxWithSingleLineFeed("["+parentView+" addConstraint:"+constraintProperty+"];", writeFileHandle)
	 			pass
	 		else:
	 			self.writeSingleSpace(writeFileHandle)
	 			self.writeSyntaxWithSingleLineFeed("["+parentView+" addConstraint:"+describle+"];", writeFileHandle)
	 			pass
	 		pass
	 	pass

	def loadOutletProperty(self, classViewName, attribView, writeFileHandle):
		# print "attribView=", attribView

		attribViewProperty = self.attribViewTagProperty(attribView)
		outletProperty = self.getClassOutletProperty(self.outletViews, attribViewProperty.get('id',''))
		if len(outletProperty) > 0:
			self.writeSingleSpace(writeFileHandle)
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
		""" attend view tag and  current view subviews
		args:
			attribViews:
		return:
			attribView:
			subView:
		"""
		attribView = {}
		subView = []
		for (tag, attrib) in attribViews.items():
			if tag == 'subviews':
				subView = attrib
				pass
			else:
				attribView[tag] = attrib
				pass
			pass
		return (attribView, subView)
