//
//  TestUILabelViewController.m
//  demo
//
//  Created by Jun on 16/10/13.
//  Copyright © 2016年 JunHg. All rights reserved.
//

#import "TestUILabelViewController.h"

@interface TestUILabelViewController ()

@end

@implementation TestUILabelViewController

#pragma mark - lifeCycle

- (void)loadView
{
	self.view = [[UIView alloc] initWithFrame:CGRectMake(0.0,0.0,375,667)];
	self.view.tag = [@"i5M-Pr-FkT" hash];
	self.view.backgroundColor = [UIColor colorWithRed:1 green:1 blue:1 alpha:1];
	self.view.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;
}

#pragma mark - loadAllSubViews

- (UILabel *)loadSubView_o2C_Tq_mjs
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"o2C-Tq-mjs" hash];
	label.numberOfLines = 0;
	NSMutableAttributedString *attributeContent = [[NSMutableAttributedString alloc] init];
	[attributeContent beginEditing];

	NSMutableAttributedString *attribute0 = [[NSMutableAttributedString alloc] initWithString:@"11111"];
	[attribute0 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:17] range:NSMakeRange(0, [@"11111" length])];
	[attribute0 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:0.95750388687315058 green:1 blue:0.31427992668005555 alpha:1] range:NSMakeRange(0, [@"11111" length])];
	[attributeContent appendAttributedString:attribute0];

	NSMutableAttributedString *attribute1 = [[NSMutableAttributedString alloc] initWithString:@"dfasdfdsas"];
	[attribute1 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:21] range:NSMakeRange(0, [@"dfasdfdsas" length])];
	[attribute1 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:1 green:0.44442677365707706 blue:0.70589291901244677 alpha:1] range:NSMakeRange(0, [@"dfasdfdsas" length])];
	[attributeContent appendAttributedString:attribute1];

	NSMutableAttributedString *attribute2 = [[NSMutableAttributedString alloc] initWithString:@"dafdasfd"];
	[attribute2 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:8] range:NSMakeRange(0, [@"dafdasfd" length])];
	[attribute2 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:1 green:0.44442677365707706 blue:0.70589291901244677 alpha:1] range:NSMakeRange(0, [@"dafdasfd" length])];
	[attributeContent appendAttributedString:attribute2];

	NSMutableAttributedString *attribute3 = [[NSMutableAttributedString alloc] initWithString:@"1111"];
	[attribute3 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:17] range:NSMakeRange(0, [@"1111" length])];
	[attribute3 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:0.24029153002500503 green:1 blue:0.42583961730351372 alpha:1] range:NSMakeRange(0, [@"1111" length])];
	[attributeContent appendAttributedString:attribute3];

	[attributeContent endEditing];
	label.attributedText = attributeContent;
	label.translatesAutoresizingMaskIntoConstraints = NO;
	[label addConstraint:[NSLayoutConstraint constraintWithItem:label
															  attribute:NSLayoutAttributeWidth
															  relatedBy:NSLayoutRelationEqual
																 toItem:nil
															  attribute:NSLayoutAttributeNotAnAttribute
															 multiplier:1.0
															   constant:70]];
	return label;
}

- (UILabel *)loadSubView_d89_mR_M6E
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"d89-mR-M6E" hash];
	label.text = @"4444444444444";
	label.font = [UIFont italicSystemFontOfSize:17];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
}

- (UILabel *)loadSubView_hgB_KH_Ode
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"hgB-KH-Ode" hash];
	label.text = @"2222222222";
	label.font = [UIFont systemFontOfSize:26];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
}

- (UILabel *)loadSubView_MbM_EM_Ec6
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"MbM-EM-Ec6" hash];
	label.backgroundColor = [UIColor colorWithRed:0.4644442473 green:1 blue:0.25169882970000002 alpha:1];
	label.text = @"333333333333333";
	label.font = [UIFont systemFontOfSize:17];
	label.textColor = [UIColor colorWithRed:1 green:0.0 blue:0.0 alpha:1];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
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

- (UILabel *)loadSubView_o2C_Tq_mjs
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"o2C-Tq-mjs" hash];
	label.numberOfLines = 0;
	NSMutableAttributedString *attributeContent = [[NSMutableAttributedString alloc] init];
	[attributeContent beginEditing];

	NSMutableAttributedString *attribute0 = [[NSMutableAttributedString alloc] initWithString:@"11111"];
	[attribute0 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:17] range:NSMakeRange(0, [@"11111" length])];
	[attribute0 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:0.95750388687315058 green:1 blue:0.31427992668005555 alpha:1] range:NSMakeRange(0, [@"11111" length])];
	[attributeContent appendAttributedString:attribute0];

	NSMutableAttributedString *attribute1 = [[NSMutableAttributedString alloc] initWithString:@"dfasdfdsas"];
	[attribute1 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:21] range:NSMakeRange(0, [@"dfasdfdsas" length])];
	[attribute1 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:1 green:0.44442677365707706 blue:0.70589291901244677 alpha:1] range:NSMakeRange(0, [@"dfasdfdsas" length])];
	[attributeContent appendAttributedString:attribute1];

	NSMutableAttributedString *attribute2 = [[NSMutableAttributedString alloc] initWithString:@"dafdasfd"];
	[attribute2 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:8] range:NSMakeRange(0, [@"dafdasfd" length])];
	[attribute2 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:1 green:0.44442677365707706 blue:0.70589291901244677 alpha:1] range:NSMakeRange(0, [@"dafdasfd" length])];
	[attributeContent appendAttributedString:attribute2];

	NSMutableAttributedString *attribute3 = [[NSMutableAttributedString alloc] initWithString:@"1111"];
	[attribute3 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:17] range:NSMakeRange(0, [@"1111" length])];
	[attribute3 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:0.24029153002500503 green:1 blue:0.42583961730351372 alpha:1] range:NSMakeRange(0, [@"1111" length])];
	[attributeContent appendAttributedString:attribute3];

	[attributeContent endEditing];
	label.attributedText = attributeContent;
	label.translatesAutoresizingMaskIntoConstraints = NO;
	[label addConstraint:[NSLayoutConstraint constraintWithItem:label
															  attribute:NSLayoutAttributeWidth
															  relatedBy:NSLayoutRelationEqual
																 toItem:nil
															  attribute:NSLayoutAttributeNotAnAttribute
															 multiplier:1.0
															   constant:70]];
	return label;
}

- (UILabel *)loadSubView_d89_mR_M6E
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"d89-mR-M6E" hash];
	label.text = @"4444444444444";
	label.font = [UIFont italicSystemFontOfSize:17];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
}

- (UILabel *)loadSubView_hgB_KH_Ode
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"hgB-KH-Ode" hash];
	label.text = @"2222222222";
	label.font = [UIFont systemFontOfSize:26];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
}

- (UILabel *)loadSubView_MbM_EM_Ec6
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"MbM-EM-Ec6" hash];
	label.backgroundColor = [UIColor colorWithRed:0.4644442473 green:1 blue:0.25169882970000002 alpha:1];
	label.text = @"333333333333333";
	label.font = [UIFont systemFontOfSize:17];
	label.textColor = [UIColor colorWithRed:1 green:0.0 blue:0.0 alpha:1];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
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

- (UILabel *)loadSubView_o2C_Tq_mjs
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"o2C-Tq-mjs" hash];
	label.numberOfLines = 0;
	NSMutableAttributedString *attributeContent = [[NSMutableAttributedString alloc] init];
	[attributeContent beginEditing];

	NSMutableAttributedString *attribute0 = [[NSMutableAttributedString alloc] initWithString:@"11111"];
	[attribute0 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:17] range:NSMakeRange(0, [@"11111" length])];
	[attribute0 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:0.95750388687315058 green:1 blue:0.31427992668005555 alpha:1] range:NSMakeRange(0, [@"11111" length])];
	[attributeContent appendAttributedString:attribute0];

	NSMutableAttributedString *attribute1 = [[NSMutableAttributedString alloc] initWithString:@"dfasdfdsas"];
	[attribute1 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:21] range:NSMakeRange(0, [@"dfasdfdsas" length])];
	[attribute1 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:1 green:0.44442677365707706 blue:0.70589291901244677 alpha:1] range:NSMakeRange(0, [@"dfasdfdsas" length])];
	[attributeContent appendAttributedString:attribute1];

	NSMutableAttributedString *attribute2 = [[NSMutableAttributedString alloc] initWithString:@"dafdasfd"];
	[attribute2 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:8] range:NSMakeRange(0, [@"dafdasfd" length])];
	[attribute2 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:1 green:0.44442677365707706 blue:0.70589291901244677 alpha:1] range:NSMakeRange(0, [@"dafdasfd" length])];
	[attributeContent appendAttributedString:attribute2];

	NSMutableAttributedString *attribute3 = [[NSMutableAttributedString alloc] initWithString:@"1111"];
	[attribute3 addAttribute:NSFontAttributeName value:[UIFont systemFontOfSize:17] range:NSMakeRange(0, [@"1111" length])];
	[attribute3 addAttribute:NSForegroundColorAttributeName value:[UIColor colorWithRed:0.24029153002500503 green:1 blue:0.42583961730351372 alpha:1] range:NSMakeRange(0, [@"1111" length])];
	[attributeContent appendAttributedString:attribute3];

	[attributeContent endEditing];
	label.attributedText = attributeContent;
	label.translatesAutoresizingMaskIntoConstraints = NO;
	[label addConstraint:[NSLayoutConstraint constraintWithItem:label
															  attribute:NSLayoutAttributeWidth
															  relatedBy:NSLayoutRelationEqual
																 toItem:nil
															  attribute:NSLayoutAttributeNotAnAttribute
															 multiplier:1.0
															   constant:70]];
	return label;
}

- (UILabel *)loadSubView_d89_mR_M6E
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"d89-mR-M6E" hash];
	label.text = @"4444444444444";
	label.font = [UIFont italicSystemFontOfSize:17];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
}

- (UILabel *)loadSubView_hgB_KH_Ode
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"hgB-KH-Ode" hash];
	label.text = @"2222222222";
	label.font = [UIFont systemFontOfSize:26];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
}

- (UILabel *)loadSubView_MbM_EM_Ec6
{
	UILabel* label = [[UILabel alloc] init];
	label.tag = [@"MbM-EM-Ec6" hash];
	label.backgroundColor = [UIColor colorWithRed:0.4644442473 green:1 blue:0.25169882970000002 alpha:1];
	label.text = @"333333333333333";
	label.font = [UIFont systemFontOfSize:17];
	label.textColor = [UIColor colorWithRed:1 green:0.0 blue:0.0 alpha:1];
	label.translatesAutoresizingMaskIntoConstraints = NO;
	return label;
}

- (void)viewDidLoad {
    [super viewDidLoad];

	// add subviews
	[self.view addSubview:[self loadSubView_o2C_Tq_mjs]];
	[self.view addSubview:[self loadSubView_d89_mR_M6E]];
	[self.view addSubview:[self loadSubView_hgB_KH_Ode]];
	[self.view addSubview:[self loadSubView_MbM_EM_Ec6]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"MbM-EM-Ec6" hash]]
															  attribute:NSLayoutAttributeCenterY
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeCenterY
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"hgB-KH-Ode" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeTop
															 multiplier:1.0
															   constant:60]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"d89-mR-M6E" hash]]
															  attribute:NSLayoutAttributeLeading
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeLeading
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeTop
															 multiplier:1.0
															   constant:60]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"MbM-EM-Ec6" hash]]
															  attribute:NSLayoutAttributeCenterX
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeCenterX
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"d89-mR-M6E" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeBottom
															 multiplier:1.0
															   constant:44]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:self.view
															  attribute:NSLayoutAttributeTrailing
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"hgB-KH-Ode" hash]]
															  attribute:NSLayoutAttributeTrailing
															 multiplier:1.0
															   constant:30]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeLeading
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeLeading
															 multiplier:1.0
															   constant:30]];

	// add subviews
	[self.view addSubview:[self loadSubView_o2C_Tq_mjs]];
	[self.view addSubview:[self loadSubView_d89_mR_M6E]];
	[self.view addSubview:[self loadSubView_hgB_KH_Ode]];
	[self.view addSubview:[self loadSubView_MbM_EM_Ec6]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"MbM-EM-Ec6" hash]]
															  attribute:NSLayoutAttributeCenterY
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeCenterY
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"hgB-KH-Ode" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeTop
															 multiplier:1.0
															   constant:60]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"d89-mR-M6E" hash]]
															  attribute:NSLayoutAttributeLeading
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeLeading
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeTop
															 multiplier:1.0
															   constant:60]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"MbM-EM-Ec6" hash]]
															  attribute:NSLayoutAttributeCenterX
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeCenterX
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"d89-mR-M6E" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeBottom
															 multiplier:1.0
															   constant:44]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:self.view
															  attribute:NSLayoutAttributeTrailing
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"hgB-KH-Ode" hash]]
															  attribute:NSLayoutAttributeTrailing
															 multiplier:1.0
															   constant:30]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeLeading
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeLeading
															 multiplier:1.0
															   constant:30]];

	// add subviews
	[self.view addSubview:[self loadSubView_o2C_Tq_mjs]];
	[self.view addSubview:[self loadSubView_d89_mR_M6E]];
	[self.view addSubview:[self loadSubView_hgB_KH_Ode]];
	[self.view addSubview:[self loadSubView_MbM_EM_Ec6]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"MbM-EM-Ec6" hash]]
															  attribute:NSLayoutAttributeCenterY
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeCenterY
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"hgB-KH-Ode" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeTop
															 multiplier:1.0
															   constant:60]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"d89-mR-M6E" hash]]
															  attribute:NSLayoutAttributeLeading
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeLeading
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeTop
															 multiplier:1.0
															   constant:60]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"MbM-EM-Ec6" hash]]
															  attribute:NSLayoutAttributeCenterX
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeCenterX
															 multiplier:1.0
															   constant:0]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"d89-mR-M6E" hash]]
															  attribute:NSLayoutAttributeTop
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeBottom
															 multiplier:1.0
															   constant:44]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:self.view
															  attribute:NSLayoutAttributeTrailing
															  relatedBy:NSLayoutRelationEqual
																 toItem:[self.view viewWithTag:[@"hgB-KH-Ode" hash]]
															  attribute:NSLayoutAttributeTrailing
															 multiplier:1.0
															   constant:30]];
	[self.view addConstraint:[NSLayoutConstraint constraintWithItem:[self.view viewWithTag:[@"o2C-Tq-mjs" hash]]
															  attribute:NSLayoutAttributeLeading
															  relatedBy:NSLayoutRelationEqual
																 toItem:self.view
															  attribute:NSLayoutAttributeLeading
															 multiplier:1.0
															   constant:30]];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
