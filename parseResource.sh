#!/bin/sh

# create: 2016/10/16
# version: 0.0.1
# author: Junhg
# contribute:
# 

# 主要功能：
# 1. 将工程中的资源文件中的资源信息加载到实现文件中
# 2. 删除所有的xib文件，优化工程的代码大小

export LC_CTYPE=C 
export LANG=C

Project_Dir=`echo $PWD`
Parse_Resource="NibProcessor/parseResource.py"

function deleteImplementOriginProperty()
{
	File_Property=`grep -n "IBOutlet" $1 | awk '{print $1}' | cut -d ':' -f 1`
	if [ ${#File_Property} != 0 ]
	then
		# echo "You has delete ${1}'s property:${File_Property}"
		sed -i "" "${File_Property}d" $1
	fi
}

function insertImplementOriginProperty()
{
	Implement_Extend_Line=`grep -n "@interface" $1 | awk '{print $1}' | cut -d ':' -f 1`
	
	if [ ${#Implement_Extend_Line} != 0 ]
	then
		echo ${Implement_Extend_Line}
		sed -i "" "${Implement_Extend_Line}a\ 
		@property (nonatomic, strong) UIView *bottomView;
		" $1
	fi
}

function main()
{
	# 添加解析资源文件的可执行权限
	chmod +x ${Project_Dir}/${Parse_Resource}

	File_Dir=${Project_Dir}/demo
	All_Implement_File=`find $File_Dir -name "*.m" -type f`
	for Implement_File in $All_Implement_File
	do
		deleteImplementOriginProperty ${Implement_File}
		# insertImplementOriginProperty ${Implement_File}
	done

	All_Resource_File=`find $File_Dir -name "*.xib" -type f`
	# for Resource_File in $All_Resource_File
	# do
	# 	echo "parse ${Resource_File}"
	# 	python ${Parse_Resource} ${Resource_File}
	# done
	python ${Parse_Resource} "demo/TestTableViewCell.xib"

	find ${Project_Dir}/NibProcessor -name "*.pyc" | xargs rm -rf
}

# exec
main