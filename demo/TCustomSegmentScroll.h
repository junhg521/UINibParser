//
//  TCustomSegmentScroll.h
//  demo
//
//  Created by Jun on 16/10/13.
//  Copyright © 2016年 JunHg. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol TCustomSegmentScrollDelegate <NSObject>

- (void)didCustomSegmentScrollChangeValue:(NSInteger)index oldIndex:(NSInteger)oldIndex;

@end

@protocol TCustomSegmentScrollDataProtocol <NSObject>

@optional

/**
 segment的文字颜色，默认为darkGrayColor
 */
@property (strong) UIColor *segmentScrollTitleNormalColor;

/**
 segment的文字颜色，默认为[UIColor colorWithRed:0.239 green:0.600 blue:0.914 alpha:1.000]
 */
@property (strong) UIColor *segmentScrollTitleSelectedColor;

/**
 每个segment之间的颜色，默认为[UIColor colorWithRed:0.890 green:0.890 blue:0.941 alpha:1.000]
 */
@property (strong) UIColor *segmentSeperatorLineColor;

/**
 底部的seperatorLine颜色，默认为clearColor
 */
@property (strong) UIColor *segmentBottomSeperatorLineColor;

@property (strong) UIColor *bottomLineColor;

@property (assign) NSInteger titleFontSize;

@end

@interface TCustomSegmentScroll : UIView<TCustomSegmentScrollDataProtocol>

@property (nonatomic, weak) id<TCustomSegmentScrollDelegate>delegate;
@property (nonatomic, assign) NSInteger selectedIndex;
@property (nonatomic, assign, getter=isSegmentScollEnabled) BOOL segmentScollEnabled;

- (instancetype)initWithTitles:(NSArray *)titles delegate:(id)delegate displaySeparator:(BOOL)displaySeparator;

@end
