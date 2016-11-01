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


class JHBaseProcessor:
	'定义通用的接口'

	def __init__(self,nibParser):
		self.resouce_file_dir = nibParser.resourceFileDir()
		self.className = nibParser.className
		pass

	def __del__(self):
		pass

	def classFileDir(self):
		resource_file = self.resouce_file_dir+self.className+'.m'
		return resource_file
		pass

	def classTempFileDir(self):
		resource_Temp_file = self.resouce_file_dir+self.className+'Temp.m'
		return resource_Temp_file
		pass

	def readClassFile(self):
		read_Class_file = open(self.classFileDir(), "r")
		return read_Class_file
		pass

	def readTempClassFile(self):
		read_Temp_Class_file = open(self.classTempFileDir(), "w")
		return read_Temp_Class_file
		pass

	def viewObjectType(self, tag):
		viewObject = JHBasicObject()
		if tag == 'view':
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
		elif tag == 'switch':
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
		elif tag == 'toolbar':
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
		return viewObject

class JHObjcProcessor(JHBaseProcessor,JHCommomObject):
	'将parseResourceManager解析后的文件保存到实现文件中'
	def __init__(self, nibParser):
		JHBaseProcessor.__init__(self,nibParser)
		self.outletViews = nibParser.outletViews
		self.attribViews = nibParser.attribViews
		pass

	def __del__(self):
		pass

	def processing(self):
		analyseAttrib = self.analyseAttribView(self.attribViews)
		attribView = analyseAttrib[0]
		subView = analyseAttrib[1]
		# print 'attribView=', attribView, 'subView=',subView
		
		try:
			subMethodNames = []
			readFileHandle = self.readClassFile()
			writeFileHandle = self.readTempClassFile()
			line = readFileHandle.readline()
			lineEdge = False
			while line !='':
				if line.find("@interface") >= 0 and line.find(self.className) >= 0:
					lineEdge = True
					writeFileHandle.write(line)
				elif line.count('IBOutlet') > 0 && lineEdge:
					self.loadIBOutletProperty(self.outletViews,subView,writeFileHandle)
					pass
				elif line.find("@implementation") >= 0 and line.find(self.className) >= 0:
					lineEdge = True
					writeFileHandle.write(line)
					self.loadView(attribView, writeFileHandle)
					if len(subView) > 0:
						writeFileHandle.write("\n\
#pragma mark - loadAllSubViews\n")
						subMethodNames = self.loadAllSubView(subView, writeFileHandle)
						pass
					pass
				elif line.find("[super viewDidLoad]") >= 0 and lineEdge:
					writeFileHandle.write(line)
					if len(subMethodNames) > 0:
						writeFileHandle.write("\n\
	// add subviews\n")
						self.loadAllSubViewOfView('self.view',subMethodNames,writeFileHandle)
						view = self.attribViewTagProperty(attribView)
						self.loadViewConstranit('self.view',view.get('id', ''),attribView.get('constraints', []),writeFileHandle)
						pass
					pass
				elif line.find("@end") >= 0:
					writeFileHandle.write(line)
					lineEdge = False
					pass
				else:
					writeFileHandle.write(line)
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
			print "finish parsor "+self.resouce_file_dir+self.className+".xib"
			readFileHandle.close()
			writeFileHandle.close()
			pass

	def loadIBOutletProperty(self, attribView, subView,writeFileHandle):
		for attrib in attribView:
			if attrib.get('property','') == 'view':
				continue
				pass
			else:
				classType = self.findSubViewWithTag(subView,attrib.get('destination',''))
				if len(classType) > 0:
					writeFileHandle.write("\
	@property (nonatomic, strong) "+classType+" *"+attrib.get('property','')+";\n")
					pass
				pass
		pass

	def findSubViewWithTag(self, attribViews, attributeProperty):
		for subAttribView in attribViews:
			attribView = {}
			subViews = []
			for (tag,attrib) in subAttribView.items():
				# print 'tag=',tag,' attrib=',attrib
				if tag == 'subviews':
					return self.findSubViewWithTag(attrib,attributeProperty)
				else:
					if type(attrib) == dict:
						if attrib.get('id','') == attributeProperty:
							return self.objcClassNameType(tag)	
					else:
						pass
					pass
				pass
			pass
		return ''

	def loadView(self, attribView, writeFileHandle):
		viewName = self.attribViewTag(attribView)
		className = self.objcClassNameType(viewName)
		if len(className) > 0:
			viewObject = self.viewObjectType(viewName)
			writeFileHandle.write("\n#pragma mark - lifeCycle\n")
			writeFileHandle.write(viewObject.loadView(attribView))
			pass
		pass

	def loadAllSubView(self, attribViews, writeFileHandle):
		methodNames = []
		subMethodNames = []
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

			if len(subViews):
				subMethodNames = self.loadAllSubView(subViews, writeFileHandle)
				pass
			# print 'attribView=', attribView
			methodName = self.loadSubView(attribView, subMethodNames, writeFileHandle)
			methodNames.append(methodName);
			pass
		return methodNames

	def loadSubView(self, attribView, subMethodNames, writeFileHandle):
		classViewName = self.attribViewTag(attribView)
		viewObject = self.viewObjectType(classViewName)
		attribViewib = self.attribViewTagProperty(attribView)

		writeFileHandle.write(viewObject.addSubview(attribView))
		self.loadAllSubViewOfView(classViewName, subMethodNames, writeFileHandle);
		self.loadViewConstranit(classViewName,self.attribViewNameID(attribView),attribView.get('constraints', []),writeFileHandle)
		self.setClassViewProperty(self.outletViews, attribViewib.get('id',''), classViewName, writeFileHandle)
		writeFileHandle.write("\
	return "+classViewName+";\n}\n")

		return self.attribViewViewMethod(attribView)

	def loadAllSubViewOfView(self,parentView,subMethodNames,writeFileHandle):
		for subMethod in subMethodNames:
			writeFileHandle.write("\
	["+parentView+" addSubview:[self "+subMethod+"]];\n")
			pass
		pass

	def setClassViewProperty(self, IBoutViews, classViewId, classViewName,writeFileHandle):
		for proprtyView in IBoutViews:
			if proprtyView.get('destination','') == classViewId and len(proprtyView.get('property','')) > 0:
				writeFileHandle.write("\
	self. "+proprtyView.get('property','')+" = "+classViewName+";\n")
				pass
			pass
		pass

	def loadViewConstranit(self, parentView, viewId, attribViews, writeFileHandle):
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
	 		subView = "["+parentView+" viewWithTag:[@"+"\""+firstItem+"\""+" hash]]"
	 		if viewId == secondItem:
	 			writeFileHandle.write("\
	["+parentView+" addConstraint:[NSLayoutConstraint constraintWithItem:"+subView+"\n\
															  attribute:"+self.layoutAttribute(firstAttribute)+"\n\
															  relatedBy:"+self.layoutRelation(relation)+"\n\
																 toItem:"+parentView+"\n\
															  attribute:"+self.layoutAttribute(secondAttribute)+"\n\
															 multiplier:"+multiplier+"\n\
															   constant:"+constant+"]];\n");
	 			pass
	 		elif len(firstItem) == 0 and len(secondItem) > 0:
	 			secodeItemView =  "["+parentView+" viewWithTag:[@"+"\""+secondItem+"\""+" hash]]"
	 			writeFileHandle.write("\
	["+parentView+" addConstraint:[NSLayoutConstraint constraintWithItem:"+parentView+"\n\
															  attribute:"+self.layoutAttribute(firstAttribute)+"\n\
															  relatedBy:"+self.layoutRelation(relation)+"\n\
																 toItem:"+secodeItemView+"\n\
															  attribute:"+self.layoutAttribute(secondAttribute)+"\n\
															 multiplier:"+multiplier+"\n\
															   constant:"+constant+"]];\n");
	 			pass
	 		elif len(secondItem) == 0:
	 			writeFileHandle.write("\
	["+parentView+" addConstraint:[NSLayoutConstraint constraintWithItem:"+parentView+"\n\
															  attribute:"+self.layoutAttribute(firstAttribute)+"\n\
															  relatedBy:"+self.layoutRelation(relation)+"\n\
																 toItem:nil\n\
															  attribute:NSLayoutAttributeNotAnAttribute\n\
															 multiplier:"+multiplier+"\n\
															   constant:"+constant+"]];\n");
	 		else :
	 			secodeItemView =  "["+parentView+" viewWithTag:[@"+"\""+secondItem+"\""+" hash]]"
	 			writeFileHandle.write("\
	["+parentView+" addConstraint:[NSLayoutConstraint constraintWithItem:"+subView+"\n\
															  attribute:"+self.layoutAttribute(firstAttribute)+"\n\
															  relatedBy:"+self.layoutRelation(relation)+"\n\
																 toItem:"+secodeItemView+"\n\
															  attribute:"+self.layoutAttribute(secondAttribute)+"\n\
															 multiplier:"+multiplier+"\n\
															   constant:"+constant+"]];\n");
	 		pass
	 	pass
	 	

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
