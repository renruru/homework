***Settings***
Library     Selenium2Library


***Variables***
${url}  http://www.baidu.com
${Keyword}      helllo


***Test Cases***
百度搜索
    [Setup]
        打开百度
        Maximize Browser Window
    输入关键字
    [Teardown]
        Close Browser
  
***Keywords***
打开百度
    Open Browser    ${url}  chrome
输入关键字
    Input Text      id:kw   ${Keyword}       
