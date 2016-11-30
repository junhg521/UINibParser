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
	def __init__(self):
		pass

	def __del__(self):
		pass

	def addSubview(self, classViewName, classMethodName, attribView):
		# print 'attribView=',attribView

		classType = self.objcClassNameType(classViewName)
		flowlayout = attribView.get('collectionViewFlowLayout',{})
		collectionFlowlayout = flowlayout.get('collectionViewFlowLayout',{})
		
		describle = self.addClassMethodName(classType, classMethodName)
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax("UICollectionViewFlowLayout *layout = [[UICollectionViewFlowLayout alloc] init];")
		if collectionFlowlayout.get('scrollDirection','horizontal') != 'horizontal':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("layout.scrollDirection = "+self.getCollectionViewScrollDirection(collectionFlowlayout.get('scrollDirection','vertical'))+";")
			pass
		if collectionFlowlayout.get('minimumLineSpacing','0') != '0':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("layout.minimumLineSpacing = "+collectionFlowlayout.get('minimumLineSpacing','0')+";")
			pass
		if collectionFlowlayout.get('minimumInteritemSpacing','0') != '0':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("layout.minimumInteritemSpacing = "+collectionFlowlayout.get('minimumInteritemSpacing','0')+";")
			pass
		if collectionFlowlayout.get('minimumInteritemSpacing','0') != '0':
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("layout.minimumInteritemSpacing = "+collectionFlowlayout.get('minimumInteritemSpacing','0')+";")
			pass

		collectionFlowlayoutProperty = flowlayout.get('property',{})
		if collectionFlowlayoutProperty.has_key('size'):
			if type(collectionFlowlayoutProperty.get('size')) == list:
				for size in collectionFlowlayoutProperty.get('size',[]):
					if size.has_key('key'):
						sizeInfo = self.getClassSizeAndKey(size)
						describle += self.addBlackCharacter()
						describle += self.writeDescribleSyntax("layout."+sizeInfo[0]+" = "+sizeInfo[1]+";")
						pass
					pass
				pass
			elif type(collectionFlowlayoutProperty.get('size')) == dict:
				size = collectionFlowlayoutProperty.get('size',{})
				sizeInfo = self.getClassSizeAndKey(size)
				describle += self.addBlackCharacter()
				describle += self.writeDescribleSyntax("layout."+sizeInfo[0]+" = "+sizeInfo[1]+";")
				pass
			else:
				pass
		else:
			pass

		inset = collectionFlowlayoutProperty.get('inset',{})
		if inset.has_key('key'):
			sectionInsetInfo = self.getClassEdgementAndKey(inset)
			describle += self.addBlackCharacter()
			describle += self.writeDescribleSyntax("layout."+sectionInsetInfo[0]+" = "+sectionInsetInfo[1]+";")
			pass
			
		describle += self.addBlackCharacter()
		describle += self.writeDescribleSyntax(classType+"* "+classViewName+" = [["+classType+" alloc] initWithFrame:"+self.getClassFrame(attribView.get('rect', {}))+" collectionViewLayout:layout];")
		
		return describle

	def addViewAttribute(self, classViewName, attribView):
		# print 'attribView=',attribView

		describle = JHScrollViewObject.addViewAttribute(self, classViewName, attribView)
		return describle