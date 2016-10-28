//
//  ViewController.m
//  demo
//
//  Created by Jun on 16/10/13.
//  Copyright © 2016年 JunHg. All rights reserved.
//

#import "ViewController.h"
#import "TCustomSegmentScroll.h"
#import "TestUILabelViewController.h"
#import "TestUIViewViewController.h"
#import "TestUIButtonViewController.h"
#import "TestUIImageViewController.h"

@interface ViewController ()<TCustomSegmentScrollDelegate>

@property (nonatomic, strong) TCustomSegmentScroll *scrollSegmentControl;
@property (nonatomic, strong) NSMutableArray *controllers;

@end

@implementation ViewController

#pragma mark - lifeCycle

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    
    [self.view addSubview:self.scrollSegmentControl];
    
    BOOL isNibFile = NO;
    [self.controllers addObject:[self loadTestViewController:@"TestUILabelViewController" isNibFile:isNibFile]];
    [self.controllers addObject:[self loadTestViewController:@"TestUIViewViewController" isNibFile:isNibFile]];
    [self.controllers addObject:[self loadTestViewController:@"TestUIButtonViewController" isNibFile:isNibFile]];
    [self.controllers addObject:[self loadTestViewController:@"TestUIImageViewController" isNibFile:isNibFile]];
    
    
    [self addTestController:[self.controllers objectAtIndex:0]];
}

- (void)viewDidLayoutSubviews
{
    [super viewDidLayoutSubviews];
    
    for (UIViewController *controller in self.controllers) {
        [controller.view setFrame:CGRectMake(0, 65, CGRectGetWidth(self.view.frame), CGRectGetHeight(self.view.frame) - 65)];
        [controller.view layoutSubviews];
    }

    [self.view layoutSubviews];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - Property

- (TCustomSegmentScroll *)scrollSegmentControl
{
    if (!_scrollSegmentControl) {
        _scrollSegmentControl = [[TCustomSegmentScroll alloc] initWithTitles:@[@"UILabel脚本测试",@"UIView脚本测试",@"UIButton脚本测试",@"UIImage脚本测试"]
                                                                     delegate:self
                                                                displaySeparator:NO];
        [_scrollSegmentControl setBottomLineColor: [UIColor greenColor]];
        [_scrollSegmentControl setTitleFontSize:16];
    }
    return _scrollSegmentControl;
}

- (NSMutableArray *)controllers
{
    if (!_controllers) {
        _controllers = [NSMutableArray array];
    }
    return _controllers;
}

#pragma mark - TCustomSegmentScrollDelegate

- (void)didCustomSegmentScrollChangeValue:(NSInteger)index oldIndex:(NSInteger)oldIndex
{
    [self removeTestController:[self.controllers objectAtIndex:oldIndex]];
    [self addTestController:[self.controllers objectAtIndex:index]];
}

#pragma mark - private

- (void)addTestController:(UIViewController *)controller
{
    [self addChildViewController:controller];
    [self.view addSubview:controller.view];
    [controller didMoveToParentViewController:self];
}

- (void)removeTestController:(UIViewController *)controller
{
    [controller willMoveToParentViewController:nil];
    [controller.view removeFromSuperview];
    [controller removeFromParentViewController];
}

- (UIViewController *)loadTestViewController:(NSString *)className isNibFile:(BOOL)isNibFile
{
    if (isNibFile) {
        UIViewController *controller = [[NSClassFromString(className) alloc] initWithNibName:nil bundle:nil];
        return controller;
    }
    else {
        UIViewController *controller = [[NSClassFromString(className) alloc] init];
        return controller;
    }
}

@end

