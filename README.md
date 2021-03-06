#UINibParser
[![Build Status](https://travis-ci.org/junhg521/UINibParser.svg?branch=master)](https://travis-ci.org/junhg521/UINibParser)
[![apm](https://img.shields.io/apm/l/vim-mode.svg)](https://github.com/junhg521/UINibParser/blob/master/LICENSE)

[中文文档](https://github.com/junhg521/UINibParser/README_CN.md)
> this document describles how to use UINibParser，it just convert xib or storyboard file into to **Objective-C/swift code**, including all the properties of instance（such as title、 color、constraint 、target and so on). also it's function is similar to [nib2objc](https://github.com/akosma/nib2objc), but it only add parsed instance and the view hierarchy instand of modify origin source file.

## Usage
put the utility in you project path, and then called this in terminal:

```
./parseResource -d ../demo/
./parseResource -f ../demo/TestTableViewCell.xib
```
it supports the following parameter calls:

```
-d :specific directory name，it contains all files with the extion xib or storyboard and convert them
-f :specific file name, just parse the resourece data
```
After the command is run, it will delete resouce files with extension **xib** or **storyboard**, This will add the output of the conversion to file with different file extions, similar to *.m, as follows: 

```
- (void)viewDidLoad {
    [super viewDidLoad];
	UIView *view__vLU_G6_5oz = [self view__vLU_G6_5oz];
	[self.view addSubview:view__vLU_G6_5oz];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:view__vLU_G6_5oz
											 attribute:NSLayoutAttributeTop
											 relatedBy:NSLayoutRelationEqual
											    toItem:self.view
											 attribute:NSLayoutAttributeTop
											multiplier:1.0
											  constant:151]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:view__vLU_G6_5oz
											 attribute:NSLayoutAttributeLeading
											 relatedBy:NSLayoutRelationEqual
											    toItem:self.view
											 attribute:NSLayoutAttributeLeading
											multiplier:1.0
											  constant:31]];
    // Do any additional setup after loading the view from its nib.
}
```
in addition, all of the subviews of the xib file are added as follows:

```
#pragma mark - loadAllSubViews
- (UIView *)view__vLU_G6_5oz
{
	UIView* view = [[UIView alloc] init];

	view.backgroundColor = [UIColor colorWithRed:1 green:0.96811995110000004 blue:0.13862504310000001 alpha:1];
	view.translatesAutoresizingMaskIntoConstraints = NO;

	[view addConstraint:[NSLayoutConstraint constraintWithItem:view
											 attribute:NSLayoutAttributeHeight
											 relatedBy:NSLayoutRelationEqual
											    toItem:nil
											 attribute:NSLayoutAttributeNotAnAttribute
											multiplier:1.0
											  constant:128]];
	[view addConstraint:[NSLayoutConstraint constraintWithItem:view
											 attribute:NSLayoutAttributeWidth
											 relatedBy:NSLayoutRelationEqual
											    toItem:nil
											 attribute:NSLayoutAttributeNotAnAttribute
											multiplier:1.0
											  constant:240]];
	self.bottomView = view;
	return view;
}
```
##Language

* xcode 7.0 
* python 2.7.0
* bash 3.2