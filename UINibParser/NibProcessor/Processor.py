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

	def viewObjectType(self, instanceName, instanceProperty):
		
		if instanceName == "containerView":
			return eval("JHViewObject()")
		elif instanceName == "tableViewCellContentView":
			return eval("JHTableViewCellObject()")
		elif instanceName == "customswitch":
			return eval("JHSwitchObject()")
		elif instanceName == "view" and instanceProperty.get('key','') == "contentView":
			return eval("JHCollectionViewCellObject()")
		else:
			if len(instanceName) < 1:
				print "instanceTag=",instanceName
				return eval("JHViewObject()")
			else:
				return eval("JH"+instanceName[0].upper() + instanceName[1:]+"Object()")
			pass
		pass

	def processing(self):
		# print 'attribViews=',self.attribViews
		exceptionFlag = 0
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
			exceptionFlag = 1
			raise
		else:
			print "finish parsor " + self.classResourceFileDir()
			os.remove(self.classFileDir())
			os.rename(self.classTempFileDir(),self.classFileDir())
		finally:
			readFileHandle.close()
			writeFileHandle.close()
			pass
		return exceptionFlag

	def loadAllResourceView(self, attribViews, writeFileHandle):
		# print "attribViews=",attribViews
		mainInstanceTag = ""
		mainInstanceProperty = {}
		mainSubMethods = []
		self.writeSyntaxWithDoubleLineFeed("#pragma mark - lifeCycle",writeFileHandle)

		for attribView in attribViews:
			instanceTag = self.attribViewTag(attribView)
			instanceProperty = self.attribViewTagProperty(attribView)
			subViewMethods = self.loadAllSubViews(instanceProperty.get('subviews',[]), writeFileHandle)
			if instanceProperty.get('id', '') == self.viewId or self.parseType != "controller":
				mainInstanceTag = instanceTag
				mainInstanceProperty = instanceProperty
				mainSubMethods = mainSubMethods + subViewMethods
				pass
			else:
				mainSubMethods.append(self.loadOtherSubView(instanceTag, instanceProperty, subViewMethods, writeFileHandle))
				pass
			pass

		viewObject = self.viewObjectType(mainInstanceTag, mainInstanceProperty)

		if self.parseType == "controller":
			self.writeSyntaxWithSingleSpaceAndLineFeed(viewObject.loadView(mainInstanceProperty), writeFileHandle)
			pass
		else:
			self.loadRootView(mainInstanceProperty, writeFileHandle)
			pass

		self.writeSyntaxWithSingleSpaceAndLineFeed(viewObject.addSubViewOfContentView(), writeFileHandle)
		self.subViewOfContentView(mainInstanceTag, mainInstanceProperty, mainSubMethods, writeFileHandle)
		self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)

	def loadRootView(self, instanceProperty, writeFileHandle):

		if self.parseType == 'tableViewCell':
			self.writeSyntaxWithSingleLineFeed(JHTableViewCellObject().loadRootViewInit(self.needloadConfiguration, instanceProperty), writeFileHandle)
			pass
		elif self.parseType == 'collectionViewCell':
			self.writeSyntaxWithSingleLineFeed(JHCollectionViewCellObject().loadRootViewInit(self.needloadConfiguration, instanceProperty), writeFileHandle)
			pass
		else:
			self.writeSyntaxWithSingleLineFeed(JHViewObject().loadRootViewInit(self.needloadConfiguration, instanceProperty), writeFileHandle)
			pass
		pass

	def loadOtherSubView(self, instanceTag, instanceProperty, subViewMethods, writeFileHandle):
		# print "instanceProperty=", instanceProperty
		viewObject = self.viewObjectType(instanceTag, instanceProperty)
		instanceName = self.attribViewInstanceName(instanceTag, instanceProperty)
		classMethodName = self.attribViewMethodName(instanceTag, instanceProperty.get('id',""))
		
		describle = viewObject.addSubview(instanceTag, instanceProperty, classMethodName)
		self.writeSyntaxWithSingleSpaceAndLineFeed(describle, writeFileHandle)

		outletProperty = self.loadOutletProperty(self.outletViews, instanceProperty.get('id',''))
		if len(outletProperty) > 0:
			self.writeSyntaxWithSingleSpaceAndLineFeed(outletProperty + " = " +instanceName+ ";", writeFileHandle)
			pass
		
		self.loadAllSubViewMethod(instanceName, subViewMethods, writeFileHandle)
		self.loadViewConstranit(instanceName, subViewMethods, instanceProperty, writeFileHandle)
		
		self.writeSyntaxWithSingleSpaceAndLineFeed("return "+instanceName+";", writeFileHandle)
		self.writeSyntaxWithSingleLineFeed(self.rightBrackets(), writeFileHandle)
		
		otherMethodNames = {}
		otherMethodNames[classMethodName] = []
		return otherMethodNames

	def subViewOfContentView(self, instanceTag, instanceProperty, methodNames, writeFileHandle):
		# print 'instanceProperty=', instanceProperty, "methodNames=",methodNames

		if self.parseType == "tableViewCell":
			self.loadContentSubViewMethod(methodNames, writeFileHandle)
			pass
		elif self.parseType == "collectionViewCell":
			self.loadContentSubViewMethod(methodNames, writeFileHandle)
			pass
		else:
			if self.parseType == "controller":
				self.loadAllSubViewMethod("self.view", methodNames, writeFileHandle)
				self.loadViewConstranit("self.view", methodNames, instanceProperty, writeFileHandle)
				pass
			else:
				self.loadAllSubViewMethod("self", methodNames, writeFileHandle)
				self.loadViewConstranit("self", methodNames, instanceProperty, writeFileHandle)
			pass
		pass

	def loadAllSubViews(self, attribViews, writeFileHandle):
		methodNames = []
		for attribView in attribViews:
			instanceTag = self.attribViewTag(attribView)
			instanceProperty = self.attribViewTagProperty(attribView)
			subMethodeNames = []
			if len(instanceProperty.get('subviews', [])) > 0:
				subMethodeNames = self.loadAllSubViews(instanceProperty.get('subviews',[]), writeFileHandle)
				pass

			# print "instanceTag=",instanceTag
			methodName = self.loadSubView(instanceTag, instanceProperty, subMethodeNames, writeFileHandle)
			methods = {}
			methods[methodName] = subMethodeNames
			methodNames.append(methods);
			# print 'instanceProperty=', instanceProperty
			pass
		return methodNames

	def loadSubView(self, instanceTag, instanceProperty, subMethodNames, writeFileHandle):
		# print 'instanceProperty=',instanceProperty,' subMethodNames=',subMethodNames

		instanceName = self.attribViewInstanceName(instanceTag, instanceProperty)
		viewObject = self.viewObjectType(instanceTag, instanceProperty)
		classMethodName = self.attribViewMethodName(instanceTag, instanceProperty.get('id', ''))
		describle = viewObject.addSubview(instanceTag, instanceProperty, classMethodName)
		self.writeSyntaxWithSingleLineFeed(describle, writeFileHandle)

		self.loadAllSubViewMethod(instanceName, subMethodNames, writeFileHandle)
		self.loadViewConstranit(instanceName, subMethodNames, instanceProperty, writeFileHandle)
		
		outletProperty = self.loadOutletProperty(self.outletViews, instanceProperty.get('id',''))
		if len(outletProperty) > 0:
			self.writeSyntaxWithSingleSpaceAndLineFeed(outletProperty + " = " +instanceName+ ";", writeFileHandle)
			pass
		
		self.writeSyntaxWithSingleSpaceAndLineFeed("return "+instanceName+";",writeFileHandle)
		self.writeSyntaxWithSingleLineFeed(self.rightBrackets(),writeFileHandle)

		return classMethodName

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

	def loadViewConstranit(self, parentView, methodNames, instanceProperty, writeFileHandle):
		# print 'parentView=',parentView, ' methodNames=',methodNames 
		constraints = instanceProperty.get('constraints', [])

	 	for attribViewConstraint in list(constraints):
	 		# print 'attribViewConstraint=',attribViewConstraint
	 		constraintProperty = attribViewConstraint.get('constraint', {})
	 		firstItem = constraintProperty.get('firstItem', '')
	 		firstAttribute = constraintProperty.get('firstAttribute', '')
	 		secondItem = constraintProperty.get('secondItem', '')
	 		secondAttribute = constraintProperty.get('secondAttribute', '')
	 		multiplier = constraintProperty.get('multiplier', '1.0')
	 		priority = constraintProperty.get('priority', '1000')
	 		constant = constraintProperty.get('constant', '0')
	 		relation = constraintProperty.get('relation', 'equal')

	 		firstItemView = self.attribViewName(methodNames, firstItem)
	 		secodeItemView = self.attribViewName(methodNames, secondItem)
	 		if instanceProperty.get('id', '') == secondItem:
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

	 		constraintProperty = self.loadOutletProperty(self.outletViews, constraintProperty.get('id',''))
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


	def loadOutletProperty(self, outletViews, instancePropertyId):
		# print "instancePropertyId=", instancePropertyId

		for outView in outletViews:
			if outView.get('destination','') == instancePropertyId:
				return "self." + outView.get('property','')
			pass
		return ""

