#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/21
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ScrollViewObject import JHScrollViewObject

class JHCollectionViewObject(JHScrollViewObject):

	def addSubview(self, instanceTag, instanceProperty, classMethodName):
		# print 'instanceProperty=',instanceProperty
		classViewName = self.attribViewInstanceName(instanceTag, instanceProperty)
		classType = self.instanceClassNameType(instanceTag, instanceProperty)
		
		flowlayout = instanceProperty.get('collectionViewFlowLayout',{})
		collectionFlowlayout = flowlayout.get('collectionViewFlowLayout',{})
		
		describle = self.addClassMethodName(classType, classMethodName)
		describle += self.loadSyntaxWithLineFeedAndSingleSpace("UICollectionViewFlowLayout *layout = [[UICollectionViewFlowLayout alloc] init];")
		if collectionFlowlayout.get('scrollDirection','horizontal') != 'horizontal':
			describle += self.loadSyntaxWithLineFeedAndSingleSpace("layout.scrollDirection = "+self.getCollectionViewScrollDirection(collectionFlowlayout.get('scrollDirection','vertical'))+";")
			pass
		if collectionFlowlayout.get('minimumLineSpacing','0') != '0':
			describle += self.loadSyntaxWithLineFeedAndSingleSpace("layout.minimumLineSpacing = "+collectionFlowlayout.get('minimumLineSpacing','0')+";")
			pass
		if collectionFlowlayout.get('minimumInteritemSpacing','0') != '0':
			describle += self.loadSyntaxWithLineFeedAndSingleSpace("layout.minimumInteritemSpacing = "+collectionFlowlayout.get('minimumInteritemSpacing','0')+";")
			pass
		if collectionFlowlayout.get('minimumInteritemSpacing','0') != '0':
			describle += self.loadSyntaxWithLineFeedAndSingleSpace("layout.minimumInteritemSpacing = "+collectionFlowlayout.get('minimumInteritemSpacing','0')+";")
			pass

		collectionFlowlayoutProperty = flowlayout.get('property',{})
		if collectionFlowlayoutProperty.has_key('size'):
			if type(collectionFlowlayoutProperty.get('size')) == list:
				for size in collectionFlowlayoutProperty.get('size',[]):
					if size.has_key('key'):
						sizeInfo = self.getClassSizeAndKey(size)
						describle += self.loadSyntaxWithLineFeedAndSingleSpace("layout."+sizeInfo[0]+" = "+sizeInfo[1]+";")
						pass
					pass
				pass
			elif type(collectionFlowlayoutProperty.get('size')) == dict:
				size = collectionFlowlayoutProperty.get('size',{})
				sizeInfo = self.getClassSizeAndKey(size)
				describle += self.loadSyntaxWithLineFeedAndSingleSpace("layout."+sizeInfo[0]+" = "+sizeInfo[1]+";")
				pass
			else:
				pass
		else:
			pass

		inset = collectionFlowlayoutProperty.get('inset',{})
		if inset.has_key('key'):
			sectionInsetInfo = self.getClassEdgementAndKey(inset)
			describle += self.loadSyntaxWithLineFeedAndSingleSpace("layout."+sectionInsetInfo[0]+" = "+sectionInsetInfo[1]+";")
			pass
			
		describle += self.loadSyntaxWithLineFeedAndSingleSpace(classType+"* "+classViewName+" = [["+classType+" alloc] initWithFrame:"+self.getClassFrame(instanceProperty.get('rect', {}))+" collectionViewLayout:layout];")
		describle += self.addViewAttribute(classViewName, instanceProperty)
		return describle

	def addViewAttribute(self, instanceTag, instanceProperty):
		# print 'instanceProperty=',instanceProperty

		describle = JHScrollViewObject.addViewAttribute(self, instanceTag, instanceProperty)
		return describle
