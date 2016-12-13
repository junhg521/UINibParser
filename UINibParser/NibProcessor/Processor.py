#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/18
# version: 0.0.1
# author: Junhg
# contribute:
#

import os

from objc.CommonObject import JHCommomObject
from objc.BasicObject import JHBasicObject
from objc.ViewObject import JHViewObject
from objc.ImageViewObject import JHImageViewObject
from objc.LabelObject import JHLabelObject
from objc.ButtonObject import JHButtonObject
from objc.ScrollViewObject import JHScrollViewObject
from objc.CollectionViewObject import JHCollectionViewObject
from objc.CollectionReusableView import JHCollectionReusableViewObject
from objc.CollectionViewCell import JHCollectionViewCellObject
from objc.TableViewCellObject import JHTableViewCellObject
from objc.TableViewObject import JHTableViewObject
from objc.TextFieldObject import JHTextFieldObject
from objc.TextViewObject import JHTextViewObject
from objc.ActivityIndicatorObject import JHActivityIndicatorObject
from objc.DatePickerObject import JHDatePickerObject
from objc.GLKViewObject import JHGLKViewObject
from objc.SliderObject import JHSliderObject
from objc.MapViewObject import JHMapViewObject
from objc.MTKViewObject import JHMTKViewObject
from objc.NavigationObject import JHNavigationObject
from objc.PageControlObject import JHPageControlObject
from objc.PickerViewObject import JHPickerViewObject
from objc.ProgressObject import JHProgressObject
from objc.SceneKitViewObject import JHSceneKitViewObject
from objc.SearchBarObject import JHSearchBarObject
from objc.SegmentedControlObject import JHSegmentedControlObject
from objc.StackObject import JHStackObject
from objc.StepperObject import JHStepperObject
from objc.SwitchObject import JHSwitchObject
from objc.TabBarObject import JHTabBarObject
from objc.ToolBarObject import JHToolBarObject
from objc.VisualEffectViewObject import JHVisualEffectViewObject
from objc.WebViewObject import JHWebViewObject

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

	def classResourceFileDir(self):
		return self.resourceDirname + "/" + self.className + '.xib'

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

	def writeSyntaxWithSingleSpaceAndLineFeed(self, syntax, writeFileHandle):
		writeFileHandle.write(self.addBlackCharacter()+syntax+self.newlineCharacter())
		pass

	def allViewObject(self):
		return ["view", "tableViewCellContentView", "label", "segmentedControl",
		"button", "textField", "slider", "switch", "customswitch", "activityIndicatorView",
		"progressView", "pageControl", "stepper", "datePicker", "pickerView", "MTKView",
		"searchBar", "tabBar", "toolBar", "navigationBar", "stackView", "tableView", 
		"tableViewCell", "imageView", "collectionView", "textView", "scrollView", "visualEffectView",
		"webView", "glkView", "mapView", "sceneKitView", "collectionReusableView", "collectionViewCell"]

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

	def attribViewInstanceName(self, attribView):
		classViewName = self.attribViewTag(attribView)
		attribViewProperty = self.attribViewTagProperty(attribView)

		if self.parseType == 'tableViewCell' and attribViewProperty.get('key','') == 'contentView':
			classViewName = "self.contentView"
			pass
		elif self.parseType == 'collectionViewCell' and attribViewProperty.get('key','') == 'contentView':
			classViewName = "self.contentView"
			pass
		else:
			pass
		return classViewName

	def viewObjectType(self, attribView):
		classViewName = self.attribViewTag(attribView)
		attribViewProperty = self.attribViewTagProperty(attribView)
		viewObject = classViewName
		if self.parseType == 'tableViewCell' and attribViewProperty.get('key','') == 'contentView':
			viewObject = "TableViewCell"
			pass
		elif self.parseType == 'collectionViewCell' and attribViewProperty.get('key','') == 'contentView':
			viewObject = "collectionViewCell"
			pass
		elif classViewName == "customswitch":
			viewObject = "switch"
			pass
		elif classViewName == "containerView":
			viewObject = "view"
			pass
		else:
			pass

		return eval("JH"+viewObject[0].upper() + viewObject[1:]+"Object()")

	def processing(self):
		# print 'attribViews=',self.attribViews
	
		try:
			readFileHandle = self.readClassFile()
			writeFileHandle = self.readTempClassFile()
			line = readFileHandle.readline()
			lineEdge = False
			while line !='':
				writeFileHandle.write(line)
				line = line.strip()
				if self.containObj(line, '@implementation') and self.containObj(line, self.className):
					lineEdge = True
					self.loadAllResourceView(self.attribViews, writeFileHandle)
					pass
				elif line.find("[super viewDidLoad];") >= 0 and lineEdge:
					self.writeSyntaxWithSingleSpaceAndLineFeed(self.loadContentSubView(), writeFileHandle)
					pass
				elif self.containObj(line, '@end'):
					lineEdge = False
					pass
				else:
					pass
				line = readFileHandle.readline()
				pass
		except Exception as e:
			print "crashed when parser " + self.classResourceFileDir()
			os.remove(self.classTempFileDir())
			raise
		else:
			print "finish parsor " + self.classResourceFileDir()
			os.remove(self.classFileDir())
			os.rename(self.classTempFileDir(),self.classFileDir())
		finally:
			readFileHandle.close()
			writeFileHandle.close()
			pass

	def loadAllResourceView(self, attribViews, writeFileHandle):
		# print "attribViews=",attribViews
		mainAttributeView = {}
		mainSubMethods = []
		self.writeSyntaxWithDoubleLineFeed("#pragma mark - lifeCycle",writeFileHandle)

		for attribView in attribViews:
			analyseAttrib = self.analyseAttribView(attribView)
			subViewMethods = self.loadAllSubViews(analyseAttrib[1], writeFileHandle)
			if self.attribViewTagProperty(analyseAttrib[0]).get('id', '') == self.viewId or self.parseType != "controller":
				mainAttributeView = analyseAttrib[0]
				mainSubMethods = mainSubMethods + subViewMethods
				pass
			else:
				mainSubMethods.append(self.loadOtherSubView(analyseAttrib[0], subViewMethods, writeFileHandle))
				pass
			pass

		viewObject = self.viewObjectType(mainAttributeView)

		if self.parseType == "controller":
			self.writeSyntaxWithSingleSpaceAndLineFeed(viewObject.loadView(analyseAttrib[0]), writeFileHandle)
			pass
		else:
			self.loadRootView(mainAttributeView, writeFileHandle)
			pass

		# print "parseType=",self.parseType
		if self.parseType == "controller":
			self.writeSyntaxWithSingleSpaceAndLineFeed(viewObject.addSubViewOfContentView("self.view", mainAttributeView), writeFileHandle)
			pass
		else:
			self.writeSyntaxWithSingleSpaceAndLineFeed(viewObject.addSubViewOfContentView("self", mainAttributeView), writeFileHandle)
			pass
		
		self.subViewOfContentView(mainAttributeView, mainSubMethods, writeFileHandle)
		self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)

	def loadRootView(self, attribView, writeFileHandle):
		if self.parseType == 'tableViewCell':
			self.writeSyntaxWithSingleLineFeed(JHTableViewCellObject().loadRootViewInit(self.needloadConfiguration, attribView), writeFileHandle)
			pass
		elif self.parseType == 'collectionViewCell':
			self.writeSyntaxWithSingleLineFeed(JHCollectionViewCellObject().loadRootViewInit(self.needloadConfiguration, attribView), writeFileHandle)
			pass
		else:
			self.writeSyntaxWithSingleLineFeed(JHViewObject().loadRootViewInit(self.needloadConfiguration, attribView), writeFileHandle)
			pass
		pass

	def loadOtherSubView(self, attribView, subViewMethods, writeFileHandle):
		# print "attribView=", attribView
		classMethodName = self.attribViewViewMethod(attribView)
		attribViewProperty = self.attribViewTagProperty(attribView)
		classViewName = self.attribViewInstanceName(attribView)
		viewObject = self.viewObjectType(attribView)
		self.writeSyntaxWithSingleSpaceAndLineFeed(viewObject.addSubview(classViewName, classMethodName, attribView), writeFileHandle)
		self.loadOutletProperty(classViewName, attribView, writeFileHandle)
		self.loadAllSubViewMethod(classViewName, subViewMethods, writeFileHandle)
		self.loadViewConstranit(classViewName, subViewMethods, attribViewProperty.get('id', ''), attribView.get('constraints', []), writeFileHandle)
		self.writeSyntaxWithSingleSpaceAndLineFeed("return "+classViewName+";", writeFileHandle)
		self.writeSyntaxWithSingleLineFeed(self.rightBrackets(), writeFileHandle)
		otherMethodNames = {}
		otherMethodNames[classMethodName] = []
		return otherMethodNames

	def subViewOfContentView(self, attribView, methodNames, writeFileHandle):
		# print 'attribView=', attribView, "methodNames=",methodNames

		attribId = self.attribViewTagProperty(attribView)
		if self.parseType == "tableViewCell":
			self.loadContentSubViewMethod(methodNames, writeFileHandle)
			pass
		elif self.parseType == "collectionViewCell":
			self.loadContentSubViewMethod(methodNames, writeFileHandle)
			pass
		else:
			if self.parseType == "controller":
				self.loadAllSubViewMethod("self.view", methodNames, writeFileHandle)
				self.loadViewConstranit("self.view", methodNames, attribId.get('id', ''), attribView.get('constraints', []), writeFileHandle)
				pass
			else:
				self.loadAllSubViewMethod("self", methodNames, writeFileHandle)
				self.loadViewConstranit("self", methodNames, attribId.get('id', ''), attribView.get('constraints', []), writeFileHandle)
			pass
		pass

	def loadAllSubViews(self, attribViews, writeFileHandle):
		methodNames = []
		for attribView in attribViews:
			analyseAttrib = self.analyseAttribView(attribView)
			subMethodeNames = []

			if len(analyseAttrib[1]) > 0:
				subMethodeNames = self.loadAllSubViews(analyseAttrib[1], writeFileHandle)
				pass

			methodName = self.loadSubView(analyseAttrib[0], subMethodeNames, writeFileHandle)
			methods = {}
			methods[methodName] = subMethodeNames
			methodNames.append(methods);
			# print 'attribView=', attribView
			pass
		return methodNames

	def loadSubView(self, attribView, methodNames, writeFileHandle):
		# print 'attribView=',attribView,' subMethodNames=',methodNames

		classViewName = self.attribViewInstanceName(attribView)
		viewObject = self.viewObjectType(attribView)
		# print "viewObject=",viewObject
		self.writeSyntaxWithSingleLineFeed(viewObject.addSubview(classViewName, self.attribViewViewMethod(attribView), attribView), writeFileHandle)
		self.loadAllSubViewMethod(classViewName, methodNames, writeFileHandle)
		self.loadViewConstranit(classViewName, methodNames, self.attribViewTagProperty(attribView).get('id', ''), attribView.get('constraints', []), writeFileHandle)
		self.loadOutletProperty(classViewName, attribView, writeFileHandle)
		self.writeSyntaxWithSingleSpaceAndLineFeed("return "+classViewName+";",writeFileHandle)
		self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)
		return self.attribViewViewMethod(attribView)

	def loadAllSubViewMethod(self, parentView, methodNames, writeFileHandle):
		# print 'parentView=',parentView, ' methodNames=',methodNames

		for subMethodNames in methodNames:
			for subMethod in subMethodNames.keys():
				viewTag = self.attribViewMethodTag(subMethod)
				classType = self.objcClassNameType(viewTag)
				self.writeSyntaxWithSingleSpaceAndLineFeed(classType+" *"+subMethod+" = [self "+subMethod+"];", writeFileHandle)
				self.writeSyntaxWithSingleSpaceAndLineFeed("["+parentView+" addSubview:"+subMethod+"];", writeFileHandle)
				pass
			pass
		pass

	def loadContentSubViewMethod(self, methodNames, writeFileHandle):

		for subMethodNames in methodNames:
			for subMethod in subMethodNames.keys():
				self.writeSyntaxWithSingleSpaceAndLineFeed("[self "+subMethod+"];", writeFileHandle)
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
	 			self.writeSyntaxWithSingleSpaceAndLineFeed(constraintProperty+" = "+describle+";", writeFileHandle)
	 			self.writeSyntaxWithSingleSpaceAndLineFeed("["+parentView+" addConstraint:"+constraintProperty+"];", writeFileHandle)
	 			pass
	 		else:
	 			self.writeSyntaxWithSingleSpaceAndLineFeed("["+parentView+" addConstraint:"+describle+"];", writeFileHandle)
	 			pass
	 		pass
	 	pass


	def loadOutletProperty(self, classViewName, attribView, writeFileHandle):
		# print "attribView=", attribView

		attribViewProperty = self.attribViewTagProperty(attribView)
		outletProperty = self.getClassOutletProperty(self.outletViews, attribViewProperty.get('id',''))
		if len(outletProperty) > 0:
			self.writeSyntaxWithSingleSpaceAndLineFeed(outletProperty+" = "+classViewName+";",writeFileHandle)
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
