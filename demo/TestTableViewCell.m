//
//  TestTableViewCell.m
//  demo
//
//  Created by Jun on 2016/11/1.
//  Copyright © 2016年 JunHg. All rights reserved.
//

#import "TestTableViewCell.h"

@interface TestTableViewCell ()<UITextFieldDelegate>

@property (nonatomic, weak) IBOutlet UILabel *titleLabel2;
@property (nonatomic, weak) UIControl *button;
@property (nonatomic, weak) UIView *sview;
@property (nonatomic, weak) UIImageView *image;
@end

@implementation TestTableViewCell


- (void)awakeFromNib {
    [super awakeFromNib];
    // Initialization code
    
    self.titleLabel2.adjustsFontSizeToFitWidth = NO;
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
