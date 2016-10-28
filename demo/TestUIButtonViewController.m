//
//  TestUIButtonViewController.m
//  demo
//
//  Created by Jun on 2016/10/27.
//  Copyright © 2016年 JunHg. All rights reserved.
//

#import "TestUIButtonViewController.h"

@interface TestUIButtonViewController ()
@property (nonatomic, strong) UIButton *button;


@end

@implementation TestUIButtonViewController

- (void)viewDidLoad {
    [super viewDidLoad];

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

- (IBAction)buttonTap:(id)sender
{
    NSLog(@"you are tap here");
}

- (IBAction)buttonTapped:(id)sender
{
    
}

@end
