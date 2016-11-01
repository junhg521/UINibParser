#!/usr/bin/python
# _*_ coding: UTF-8 _*_

__author__ = 'Junhg'

# create: 2016/10/25
# version: 0.0.1
# author: Junhg
# contribute:
# 

from ViewObject import JHViewObject

class JHTextFieldObject(JHViewObject):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def addSubview(self, attribView):
		# print 'attribView=', attribView
		classViewName = self.attribViewTag(attribView)
		classViewAttrib = self.attribViewTagProperty(attribView)
		describle = JHViewObject.addSubview(self,attribView)
		connections = attribView.get('connections', {})

		if classViewAttrib.has_key('background'):
			describle +="	"+classViewName+".background = [UIImage imageNamed:@"+"\""+classViewAttrib.get('background','')+"\""+"];\n"
			pass

		if classViewAttrib.has_key('disabledBackground'):
			describle +="	"+classViewName+".disabledBackground = [UIImage imageNamed:@"+"\""+classViewAttrib.get('disabledBackground','')+"\""+"];\n"
			pass

		if classViewAttrib.has_key('placeholder'):
			describle +="	"+classViewName+".placeholder = @"+"\""+classViewAttrib.get('placeholder','')+"\""+";\n"
			pass

		if classViewAttrib.has_key('text'):
			describle +="	"+classViewName+".text = @"+"\""+classViewAttrib.get('text','')+"\""+";\n"
			pass

		if attribView.has_key('fontDescription'):
			describle +="	"+classViewName+".font = "+self.getTextFont(attribView.get('fontDescription'))+';\n'
			pass

		if attribView.has_key('clipsSubviews'):
			if attribView.get('clipsSubviews') == 'YES':
				describle +="	"+classViewName+".clipsSubviews = "+attribView.get('clipsSubviews')+';\n'
				pass
			pass

		if classViewAttrib.has_key('borderStyle'):
			describle +="	"+classViewName+".borderStyle = "+self.getTextBorderStyle(classViewAttrib.get('borderStyle'))+';\n'
			pass

		if classViewAttrib.has_key('clearButtonMode'):
			describle +="	"+classViewName+".clearButtonMode = "+self.getTextFieldViewMode(classViewAttrib.get('clearButtonMode'))+';\n'
			pass
		
		if classViewAttrib.has_key('leftViewMode'):
			describle +="	"+classViewName+".leftViewMode = "+self.getTextFieldViewMode(classViewAttrib.get('leftViewMode'))+';\n'
			pass

		if classViewAttrib.has_key('rightViewMode'):
			describle +="	"+classViewName+".rightViewMode = "+self.getTextFieldViewMode(classViewAttrib.get('rightViewMode'))+';\n'
			pass
		
		for connection in connections:
			if connection.has_key('action'):
				action = connection.get('action', {})
				if action.has_key('selector') and action.has_key('eventType'):
					describle +="	["+classViewName+" addTarget:self action:@selector("+action.get('selector','')+") forControlEvents:+"+self.getControlEvent(action.get('eventType', 'touchUpInside'))+"];\n"
					pass
				pass
			pass
		return describle
		