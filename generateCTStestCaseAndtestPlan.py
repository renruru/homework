#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhangteng

import xml.dom.minidom
import sys,os,re
import shutil

# 1.获取所有ModuleName。2.获取所有类名。3.获取类中的所有方法testCaseName。
def getModuleName_className_testCase(path):
    path = os.path.join(path, 'src\\com\\android\\function')
    moduleNames = os.listdir(path) #1.获取ModuleName。
    allClassNames = []  #二维数组[[模块一所有的类名], [模块二所有的类名]]
    testCase_dic = {}   #字典{class1：[所有的方法]，class2:[所有的方法]}
    for m in moduleNames:
        modulePath = os.path.join(path, m)
        files_java = os.listdir(modulePath)
        classInModule = []
        for f in files_java:
            name = f.split('.')[0]
            classInModule.append(name)   #获取className
            javaPath = os.path.join(modulePath, f)
            with open(javaPath, 'r') as fp:
                context = fp.read()
                testCase = re.findall(r'public void test(.*)\(', context)    #获取testCaseName
            testCase_dic[name] = testCase   #每个模块的类名不能一样，否则在添加字典时会覆盖前面已存在的key。
        allClassNames.append(classInModule)
    # print(moduleNames, allClassNames, testCase_dic)
    return moduleNames, allClassNames, testCase_dic

def generateTestCaseXml(packageName, classNames, testCase_dic, testCasesDir):
    packageNames_full = 'com.release.' + packageName
    doc = xml.dom.minidom.Document()
    root = doc.createElement('TestPackage')
    root.setAttribute('appPackageName', packageNames_full)
    root.setAttribute('name', packageName)
    root.setAttribute('testType', 'uiAutomator')
    root.setAttribute('jarPath', 'com.release.TestCases.jar')
    root.setAttribute('version', '1.0')
    doc.appendChild(root)

    TestSuite = doc.createElement('TestSuite')
    TestSuite.setAttribute('name', 'com')
    root.appendChild(TestSuite)
    TestSuite_sub = doc.createElement('TestSuite')
    TestSuite_sub.setAttribute('name', 'release')
    TestSuite.appendChild(TestSuite_sub)
    sub_code = doc.createElement('TestSuite')
    sub_code.setAttribute('name', packageName)
    TestSuite_sub.appendChild(sub_code)

    for c in classNames:
        TestCase = doc.createElement('TestCase')
        TestCase.setAttribute('name', c)
        sub_code.appendChild(TestCase)

        caseList = testCase_dic.get(c)
        for case in caseList:
            Test = doc.createElement('Test')
            Test.setAttribute('name', 'test'+case)
            TestCase.appendChild(Test)

    fp = open(testCasesDir+'\\'+packageNames_full+'.xml', 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')

def generateTestPlanXml(moduleNames, testCasesDir):
    doc = xml.dom.minidom.Document()
    root = doc.createElement('TestPlan')
    root.setAttribute('version', '1.0')
    doc.appendChild(root)
    for m in moduleNames:
        Entry = doc.createElement('Entry')
        Entry.setAttribute('uri', 'com.release.'+m)
        root.appendChild(Entry)
    fp = open(testCasesDir+'\\'+'releasePlan.xml', 'w')
    doc.writexml(fp, newl='\n', encoding='utf-8')

def modifyBuild(currentPath):
    buildXml = os.path.join(currentPath, 'build.xml')
    print(buildXml)
    with open(buildXml, 'r') as fp:
        context = fp.read()
    strinfo = re.compile('help')
    newContext = strinfo.sub('build', context)
    m = re.search('default="build"', newContext)
    if m is not None:
        print("---------修改build成功---------")
    else:
        print("---------修改build失败---------")
        sys.exit(1)
    with open(buildXml, 'w') as fp:
        fp.write(newContext)

if __name__ == '__main__':
    currentPath = sys.path[0]
    #os.chdir(currentPath)
    jarName = 'com.release.testCases'
    print('1.生成build.xml。')
    os.system('android create uitest-project -n %s -t 1 -p %s' % (jarName, currentPath))
    print('2.修改build.xml。')
    modifyBuild(currentPath)
    print('3.编译成jar包。')
    os.system('ant -buildfile %s\\build.xml' % currentPath)
    print('4.生成测试用例xml文件到testCase目录。')
    moduleNames, allClassNames, testCase_dic = getModuleName_className_testCase(currentPath)
    testCasesDir = os.path.join(currentPath, 'testCases')
    if os.path.exists(testCasesDir):
        shutil.rmtree(testCasesDir)
        os.makedirs(testCasesDir)
    else:
        os.mkdir(testCasesDir)
    #生成testCase.xml
    for i in range(len(moduleNames)):
        generateTestCaseXml(moduleNames[i], allClassNames[i], testCase_dic, testCasesDir)
    #生成plan.xml
    generateTestPlanXml(moduleNames, testCasesDir)

    print('5.拷贝jar包到testCases目录下。')
    os.system('copy %s\\bin\\com.release.*.jar  %s\\testCases' % (currentPath, currentPath))

