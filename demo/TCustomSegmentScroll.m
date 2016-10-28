//
//  TCustomSegmentScroll.m
//  demo
//
//  Created by Jun on 16/10/13.
//  Copyright © 2016年 JunHg. All rights reserved.
//

#import "TCustomSegmentScroll.h"

#define  SelectedColor = [UIColor colorWithRed:0.239 green:0.600 blue:0.914 alpha:1.000];
#define  scrollButtonWidht 150

@interface TCustomSegmentScroll ()

@property (nonatomic, strong) UIScrollView *scrollView;
@property (nonatomic, strong) UIView *slideView;
@property (nonatomic, strong) UIView *bottomLineView;
@property (nonatomic, strong) NSMutableArray<UIButton *> *btnArray;
@property (nonatomic, strong) NSMutableArray<UIView *> *seperatorArray;

@property (nonatomic, assign) int itemSpace;
@property (nonatomic, assign) float bottomLineRation;
@property (nonatomic, assign) BOOL isDisplaySepartorLine;
@end

@implementation TCustomSegmentScroll

#pragma mark - lifeCycle

- (instancetype)initWithTitles:(NSArray *)titles delegate:(id)delegate
{
    return [self initWithTitles:titles delegate:delegate bottomLineColor:[self segmentBottomSeperatorLineColor] itemSpace:10 bottomLineLengthPercent:0.5 displaySeparator:NO separatorLineColor:[self segmentSeperatorLineColor]];
}

- (instancetype)initWithTitles:(NSArray *)titles delegate:(id)delegate displaySeparator:(BOOL)displaySeparator
{
    return [self initWithTitles:titles delegate:delegate bottomLineColor:[self segmentBottomSeperatorLineColor] itemSpace:0 bottomLineLengthPercent:1 displaySeparator:displaySeparator separatorLineColor:[self segmentSeperatorLineColor]];
}

- (void)setScrollEnable:(BOOL)enable
{
    [self.scrollView setScrollEnabled:enable];
}

/**
 底部添加一条线
 
 @param bottomColor 底部线的颜色
 */
- (void)addLineWithColor:(UIColor*)bottomColor
{
    UIView *bottomLine = [[UIView alloc]initWithFrame:CGRectMake(0,CGRectGetHeight(self.frame)-1,CGRectGetWidth([UIScreen mainScreen].bounds), 1)];
    bottomLine.backgroundColor = bottomColor;
    [self addSubview:bottomLine];
    
}

- (instancetype)initWithTitles:(NSArray *)titles delegate:(id)delegate bottomLineColor:(UIColor *)bottomLineColor itemSpace:(int)itemSpace bottomLineLengthPercent:(float)lengthPercent displaySeparator:(BOOL)displaySeparator separatorLineColor:(UIColor *)separatorLineColor
{
    if (self = [super initWithFrame:CGRectMake(0, 20, CGRectGetWidth([UIScreen mainScreen].bounds), 45.0)]) {
        self.itemSpace = itemSpace;
        self.segmentScollEnabled = YES;
        self.bottomLineRation = lengthPercent > 1 ? 1 :lengthPercent;
        self.isDisplaySepartorLine = displaySeparator;
        
        self.delegate = delegate;
        self.btnArray = [NSMutableArray arrayWithCapacity:titles.count];
        self.seperatorArray = [NSMutableArray arrayWithCapacity:titles.count];
        
        UIScrollView *scrollView = [[UIScrollView alloc] initWithFrame:CGRectMake(0, 0, CGRectGetWidth([UIScreen mainScreen].bounds), 45.0)];
        scrollView.backgroundColor = [UIColor clearColor];
        [self setupScrollView:scrollView titles:titles];
        [self addSubview:scrollView];
        self.scrollView = scrollView;
        
        [self setSegmentBottomSeperatorLineColor:bottomLineColor];
        [self setSegmentSeperatorLineColor:separatorLineColor];
    }
    return self;
}

- (void)setupScrollView:(UIScrollView *)scrollView titles:(NSArray *)titles
{
    CGFloat width4btn = scrollButtonWidht;
    for (int i = 0; i<[titles count]; i++) {
        UIButton *btns = [UIButton buttonWithType:UIButtonTypeCustom];
        btns.backgroundColor = [UIColor clearColor];
        btns.frame = CGRectMake(self.itemSpace*(i+1)+i*width4btn, 0, width4btn, 43);
        [btns setTitle:[titles objectAtIndex:i] forState:UIControlStateNormal];
        [btns setTitleColor:[self segmentScrollTitleNormalColor] forState:UIControlStateNormal];
        [btns setTitleColor:[self segmentScrollTitleSelectedColor] forState:UIControlStateSelected];
        btns.titleLabel.font = [UIFont systemFontOfSize:[self titleFontSize]];
        btns.tag = i;
        [self.btnArray addObject:btns];
        [btns addTarget:self action:@selector(didBtnClicked:) forControlEvents:UIControlEventTouchUpInside];
        [scrollView addSubview:btns];
        if (i == 0) {
            btns.selected = YES;
        }
        
        if (self.isDisplaySepartorLine && (i < titles.count-1)) {
            UIView *seperatorLineView = [[UIView alloc] initWithFrame:CGRectMake(width4btn-1, 6, 1, 43*3/4)];
            seperatorLineView.backgroundColor = [self segmentSeperatorLineColor];
            [self.seperatorArray addObject:seperatorLineView];
            [btns addSubview:seperatorLineView];
        }
    }
    
    UIButton *firstBtn = [_btnArray objectAtIndex:0];
    self.slideView.frame = CGRectMake(firstBtn.frame.origin.x + firstBtn.frame.size.width*(1-self.bottomLineRation)/2, 42, firstBtn.frame.size.width*self.bottomLineRation, 2);
    [scrollView addSubview:self.slideView];
    
    self.bottomLineView.frame = CGRectMake(0, 44, width4btn * (titles.count + 1), 1);
    [scrollView addSubview:self.bottomLineView];

    scrollView.backgroundColor = [UIColor clearColor];
    scrollView.contentSize = CGSizeMake(width4btn * (titles.count + 1), scrollView.frame.size.height);
    scrollView.showsHorizontalScrollIndicator = NO;
    scrollView.showsVerticalScrollIndicator = NO;
}

- (void)didBtnClicked: (UIButton *)button
{
    [self changeButtonClicked:button.tag];
    
    if ([self.delegate respondsToSelector:@selector(didCustomSegmentScrollChangeValue:oldIndex:)]) {
        [self.delegate didCustomSegmentScrollChangeValue:button.tag oldIndex:self.selectedIndex];
    }
    self.selectedIndex = button.tag;
}

- (void)setSegmentScollEnabled:(BOOL)segmentScollEnabled
{
    self.scrollView.contentSize = CGSizeMake(CGRectGetWidth([UIScreen mainScreen].bounds), self.scrollView.frame.size.height);
}

#pragma mark -- 根据按钮id设置选中状态
- (void)changeButtonClicked:(NSInteger)btnIndex
{
    if (btnIndex < 0) return;
    if(self.btnArray.count == 0) return;
    
    UIButton *selectButton = self.btnArray[btnIndex];
    if (selectButton.selected == YES) return;
    
    for (UIButton *subBtn in self.btnArray) {
        if (subBtn == selectButton) {
            subBtn.selected = YES;
            [subBtn setTitleColor:[self segmentScrollTitleSelectedColor] forState:UIControlStateSelected];
        }
        else {
            subBtn.selected = NO;
            [subBtn setTitleColor:[self segmentScrollTitleNormalColor] forState:UIControlStateNormal];
        }
    }
    
    CGRect originFrame = selectButton.frame;
    [UIView animateWithDuration:0.2 animations:^{
        [_slideView setFrame:CGRectMake(originFrame.origin.x+originFrame.size.width*(1-self.bottomLineRation)/2, 42, originFrame.size.width*self.bottomLineRation, 2)];
    } completion:^(BOOL finished) {
        
    }];
}

#pragma mark - property

- (UIView *)bottomLineView
{
    if (!_bottomLineView) {
        _bottomLineView = [[UIView alloc]initWithFrame:CGRectMake(0, 44, CGRectGetWidth([UIScreen mainScreen].bounds), 1)];
        _bottomLineView.backgroundColor = [self bottomLineColor];
    }
    return _bottomLineView;
}

- (UIView *)slideView
{
    if (!_slideView) {
        _slideView = [[UIView alloc]initWithFrame:CGRectMake(0, 42, 60, 2)];
        _slideView.backgroundColor = [self segmentBottomSeperatorLineColor];
    }
    return _slideView;
}
#pragma mark - BPCustomSegmentScrollDataProtocol

- (UIColor *)segmentScrollTitleNormalColor
{
    return [UIColor darkGrayColor];
}

- (void)setSegmentScrollTitleNormalColor:(UIColor *)segmentScrollTitleNormalColor
{
    for (UIButton *button in self.btnArray) {
        [button setTitleColor:segmentScrollTitleNormalColor forState:UIControlStateNormal];
    }
}

- (UIColor *)segmentScrollTitleSelectedColor
{
    return [UIColor colorWithRed:0.239 green:0.600 blue:0.914 alpha:1.000];
}

- (void)setSegmentScrollTitleSelectedColor:(UIColor *)segmentScrollTitleSelectedColor
{
    for (UIButton *button in self.btnArray) {
        [button setTitleColor:segmentScrollTitleSelectedColor forState:UIControlStateSelected];
    }
}

- (UIColor *)segmentSeperatorLineColor
{
    return [UIColor colorWithRed:0.890 green:0.890 blue:0.941 alpha:1.000];
}

- (void)setSegmentSeperatorLineColor:(UIColor *)segmentSeperatorLineColor
{
    for (UIView *seperatorView in self.seperatorArray) {
        seperatorView.backgroundColor = segmentSeperatorLineColor;
    }
}

- (UIColor *)segmentBottomSeperatorLineColor
{
    return [UIColor colorWithRed:0.239 green:0.600 blue:0.914 alpha:1.000];
}

- (void)setSegmentBottomSeperatorLineColor:(UIColor *)segmentBottomSeperatorLineColor
{
    self.slideView.backgroundColor = segmentBottomSeperatorLineColor;
}

- (UIColor *)bottomLineColor
{
    return [UIColor colorWithRed:0.890 green:0.890 blue:0.941 alpha:1.000];
}

- (void)setBottomLineColor:(UIColor *)bottomLineColor
{
    self.bottomLineView.backgroundColor = bottomLineColor;
}

- (NSInteger)titleFontSize
{
    return  15;
}

- (void)setTitleFontSize:(NSInteger)titleFontSize
{
    for (UIButton *button in self.btnArray) {
        button.titleLabel.font = [UIFont systemFontOfSize:16];
    }
}

@end
