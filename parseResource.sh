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

declare Project_Dir=`echo $PWD`
declare Parse_Resource="NibProcessor/parseResource.py"
declare File_Name=""
declare File_Dir=""
declare parseObjcType="objc"

while getopts ":osd:f:" option; do
	case $option in
		o)
			parseObjcType="objc"
			;;
		s)
			parseObjcType="swift"
			echo "exchange xib file to swift code is not accpted for the moment"
			;;
		f) 
			File_Name=${OPTARG}
			;;
		d)
			File_Dir=${OPTARG}
			;;
		\? )
			echo "Invalid option: -$OPTARG"
			;;
	esac
done

function deleteImplementOriginProperty()
{
	File_Property=`grep -n "IBOutlet" $1 | awk '{print $1}' | cut -d ':' -f 1`
	# echo "File_Property=${File_Property}, fileName=${1}"
	if [ ${#File_Property} != 0 ]
	then
		# echo "You has delete ${1}'s property:${File_Property}"
		sed -i "" "${File_Property}d" $1
	fi
}

function deleteResourceFileFromProject()
{
	projectFiles=`find ${Project_Dir} -name "*.pbxproj" -type f`
	for projectFile in ${projectFiles}; do
		echo "projectFile=${projectFile}, fileName=${1}"
		resoureFile=`grep -n $1 ${projectFile} | awk '{print $1}' | cut -d ':' -f 1`

		if [[ ${#resoureFile} -gt 0 ]]; then
			deleteResourceFileFromProject $1
		else
			sed -i "" "${resoureFile[0]}d" ${projectFile}
		fi
	done
}

function main()
{
	# 添加解析资源文件的可执行权限
	chmod +x ${Project_Dir}/${Parse_Resource}

	if [[ ${#File_Name} -gt 0 ]]; then
		file_extend=${File_Name##*.}
		if [[ ${file_extend} != 'xib' ]]; then
			echo "can't parse such extension ${file_extend}"
			return
		fi

		module_File_Name=${Project_Dir}/${File_Name}
		deleteImplementOriginProperty ${module_File_Name/%.xib/.m}
		python ${Parse_Resource} ${module_File_Name}
		deleteResourceFileFromProject ${module_File_Name##*/}
		rm -rf ${module_File_Name}
	else
		module_Dir=${Project_Dir}/${File_Dir}
		# 删除File_Dir目录下所有后缀名为(.m)文件中所包含的IBOutlet变量
		All_Implement_File=`find ${module_Dir} -name "*.m" -type f`
		for Implement_File in ${All_Implement_File}; do
			deleteImplementOriginProperty ${Implement_File}
		done

		# 解析File_Dir目录下所有的xib文件
		All_Resource_File=`find ${module_Dir} -name "*.xib" -type f`
		for Resource_File in $All_Resource_File; do
			python ${Parse_Resource} ${Resource_File}
			deleteResourceFile ${Resource_File##*/}
			rm -rf ${Resource_File}
		done
	fi

	# 将产生的中间代码删除
	find ${Project_Dir}/NibProcessor -name "*.pyc" | xargs rm -rf
}

# exec
main
