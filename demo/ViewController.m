//
//  ViewController.m
//  demo
//
//  Created by Jun on 16/10/13.
//  Copyright © 2016年 JunHg. All rights reserved.
//

#import "ViewController.h"
#import "TestViewController.h"

@interface ViewController ()
@property (nonatomic, strong) TestViewController *controller;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
//    TestViewController *controller = [[TestViewController alloc] initWithNibName:nil bundle:nil];
    TestViewController *controller = [[TestViewController alloc] init];
    self.controller = controller;
    [self addChildViewController:controller];
    [self.view addSubview:controller.view];
}

- (void)viewDidLayoutSubviews
{
    [super viewDidLayoutSubviews];
    
    [self.controller.view setFrame:self.view.frame];
    [self.controller.view layoutSubviews];

    [self.view layoutSubviews];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
