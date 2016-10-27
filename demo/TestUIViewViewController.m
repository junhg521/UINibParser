//
//  TestUIViewViewController.m
//  demo
//
//  Created by Jun on 2016/10/27.
//  Copyright © 2016年 JunHg. All rights reserved.
//

#import "TestUIViewViewController.h"

@interface TestUIViewViewController ()

@end

@implementation TestUIViewViewController

#pragma mark - lifeCycle

- (void)loadView
{
	self.view = [[UIView alloc] initWithFrame:CGRectMake(0.0,0.0,375,667)];
	self.view.tag = [@"i5M-Pr-FkT" hash];
	self.view.backgroundColor = [UIColor colorWithRed:1 green:1 blue:1 alpha:1];
	self.view.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;
}

#pragma mark - loadAllSubViews

- (UIView *)loadSubView_vLU_G6_5oz
{
	UIView* view = [[UIView alloc] init];
	view.tag = [@"vLU-G6-5oz" hash];
	view.backgroundColor = [UIColor colorWithRed:1 green:0.96811995110000004 blue:0.13862504310000001 alpha:1];
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
	return view;
}

#pragma mark - lifeCycle

- (void)loadView
{
	self.view = [[UIView alloc] initWithFrame:CGRectMake(0.0,0.0,375,667)];
	self.view.tag = [@"i5M-Pr-FkT" hash];
	self.view.backgroundColor = [UIColor colorWithRed:1 green:1 blue:1 alpha:1];
	self.view.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;
}

#pragma mark - loadAllSubViews

- (UIView *)loadSubView_vLU_G6_5oz
{
	UIView* view = [[UIView alloc] init];
	view.tag = [@"vLU-G6-5oz" hash];
	view.backgroundColor = [UIColor colorWithRed:1 green:0.96811995110000004 blue:0.13862504310000001 alpha:1];
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
	return view;
}

- (void)viewDidLoad {
    [super viewDidLoad];

	// add subviews
	[self.view addSubview:[self loadSubView_vLU_G6_5oz]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"vLU-G6-5oz" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeTop
															 multiplier:1.0
															   constant:151]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"vLU-G6-5oz" hash]]
															  attribute:NSLayoutAttributeLeading
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeLeading
															 multiplier:1.0
															   constant:31]];

	// add subviews
	[self.view addSubview:[self loadSubView_vLU_G6_5oz]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"vLU-G6-5oz" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeTop
															 multiplier:1.0
															   constant:151]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"vLU-G6-5oz" hash]]
															  attribute:NSLayoutAttributeLeading
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeLeading
															 multiplier:1.0
															   constant:31]];
    // Do any additional setup after loading the view from its nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
