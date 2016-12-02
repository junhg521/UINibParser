#NibParser
> 该文档主要描述如何使用UINibParser，它主要作用是将xib文件或storyboard文件解析成**Objective-c**代码（包含应用程序的所有属性、试图结构及属性描述、约束、修改UITableview的registerNib及UINib等）。
>

## 使用方法
首先进入UINibParser目录，然后在终端调用如下命令

```
./parseResource -d ../demo/
./parseResource -f ../demo/TestTableViewCell.xib
```
其中*parseResource*为调用的命令，在命令介绍后将会删除扩展名为xib的文件。它支持如下的参数调用

```
-d :其后跟具体的目录名，它会循环遍历目录下扩展名为xib的所有文件，并将其转化为Object-c代码
-f :其后跟具体的文件名，只解析该具体的文件
```
调用后的其相对应的(扩展名为.m)文件中将增加如下的代码，举例所示，比如在viewDidload函数下

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
此外还增加了所有xib文件所有的子view，如下所示：

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
