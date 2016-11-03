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

@end

@implementation TestTableViewCell


- (void)awakeFromNib {
    [super awakeFromNib];
    // Initialization code
    
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
