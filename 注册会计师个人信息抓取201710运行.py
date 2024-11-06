#-*-coding:utf-8-*-
from selenium import webdriver
import random
import time
import re
import os

# print(os.getcwd()) # 获取当前的工作目录，并显示出来
# os.chdir('D:/PythonProjects/中注协')  # 改变工作目录为当前目录，以便调用自编函数
# 
# from subProcess2017 import printX


# %%%%% %%%%% 定义读取本页面中审计师数据用的子函数
def getPageData(personNum, elementPerson, driverChrome,allData):
    # >>>>> >>>>> >>>>> 依次提取页面上的审计师信息
    for kk in range(0, personNum):
        print([kk, personNum])
        link = elementPerson[kk].get_attribute('href') # 取出个人页面的链接数据
        link = re.findall('\(\'(.*?)\'',link)[0] # 取出链接
        perUrl = 'http://cmispub.cicpa.org.cn/cicpa2_web/07/'+link+'.shtml' # 生成有效链接
        try:
            driverChrome.get(perUrl) # 用谷歌浏览器进入个人信息网页
            time.sleep(3) # 爬虫随机暂停
            # >>>>> 尝试提取第一条信息
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr[3]/td[2]') # 找出所在元素
            element = element[0] # 取出元素
            temp01Name = element.text  # 取出“姓名”
            # <<<<< 尝试提取第一条信息
        except:
            print('这个审计师的数据不存在')
        else:
            # >>>>> >>>>> 提取出其他信息
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"姓名")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp01Name = element.text  # 取出“姓名”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"性别")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp02Gender = element.text  # 取出“性别”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"所内职务")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp03Position = element.text  # 取出“所内职务”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"是否党员")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp04Party = element.text  # 取出“是否党员”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"学历")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp05Education = element.text  # 取出“学历”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"学位")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp06Degree = element.text  # 取出“学位”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"所学专业")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp07Major = element.text  # 取出“所学专业”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"毕业学校")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp08University = element.text  # 取出“毕业学校”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"资格取得方式")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp09Way = element.text  # 取出“资格取得方式（考试/考核）”
            
            if temp09Way=='考试':
                element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"全科合格证书号")]/following-sibling::td') # 找出所在元素
                element = element[0] # 取出元素
                temp10CertiNo = element.text  # 取出“全科合格证书号”
                
                element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"全科合格年份")]/following-sibling::td') # 找出所在元素
                element = element[0] # 取出元素
                temp11AllPassYear = element.text  # 取出“全科合格年份”
            elif temp09Way=='考核':
                element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"考核批准文号")]/following-sibling::td') # 找出所在元素
                element = element[0] # 取出元素
                temp10CertiNo = element.text  # 取出“考核批准文号”
                
                element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"批准时间")]/following-sibling::td') # 找出所在元素
                element = element[0] # 取出元素
                temp11AllPassYear = element.text  # 取出“批准时间”
            else:
                element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"全科合格证书号")]/following-sibling::td') # 找出所在元素
                element = element[0] # 取出元素
                temp10CertiNo = element.text  # 取出“全科合格证书号”
                
                element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"全科合格年份")]/following-sibling::td') # 找出所在元素
                element = element[0] # 取出元素
                temp11AllPassYear = element.text  # 取出“全科合格年份”
            #if End End End
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"注册会计师证书编号")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp12CpaNo = element.text  # 取出“注册会计师证书编号”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"是否合伙人")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp13Partner = element.text  # 取出“是否合伙人（股东）”
                        
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"批准注册文件号")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp14FileNo = element.text  # 取出“批准注册文件号”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"批准注册时间")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp15RegisterDate = element.text  # 取出“批准注册时间”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"所在事务所")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp16Firm = element.text  # 取出“所在事务所”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"本年度应完成学时")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp17DueTrain = element.text  # 取出“本年度应完成学时”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"本年度已完成学时")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp18RealTrain = element.text  # 取出“本年度已完成学时”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"惩戒及处罚信息")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp19Punish = element.text  # 取出“惩戒及处罚信息(披露时限:自2014年至今)”
            
            element = driverChrome.find_elements_by_xpath('//*[@id="detailtb"]/tbody/tr/td[contains(text(),"参加公益活动")]/following-sibling::td') # 找出所在元素
            element = element[0] # 取出元素
            temp20Public = element.text  # 取出“参加公益活动”
            
            element = driverChrome.find_elements_by_xpath('//td[contains(text(),"取得国内其他专业资格")]') # 找出所在元素
            if len(element)>0:
                element = driverChrome.find_elements_by_xpath('//*[@id="gntable"]/tbody/tr[2]') # 找出所在元素
                element = element[0] # 取出元素
                temp21OtherCerti = element.text  # 取出“其他证书信息”
            else:
                temp21OtherCerti = '' # 设为空内容
            # <<<<< <<<<< 提取出其他信息
            personData = [temp01Name, temp02Gender, temp03Position, temp04Party, temp05Education, temp06Degree, temp07Major, temp08University, temp09Way, temp10CertiNo, temp11AllPassYear, temp12CpaNo, temp13Partner, temp14FileNo, temp15RegisterDate, temp16Firm, temp17DueTrain, temp18RealTrain, temp19Punish, temp20Public, temp21OtherCerti] # 把个人的所有数据串成列表
            [allData[t].append(personData[t]) for t in range(0,len(personData))] # 把个人数据添加到总数据中
        #try End End
    #for End
    # <<<<< <<<<< <<<<< 依次提取页面上的审计师信息
    return allData
# %%%%% %%%%% 定义读取本页面中审计师数据用的子函数




# >>>>> >>>>> >>>>> >>>>> >>>>> 读取上交所公司代码列表
nameList = [] # 建立空列表用来存储读取的数据
fh = open('D:\全是数据\注册会计师个人信息抓取201710\注册会计师名单.txt', 'r')  # 建立用于读取的文件对象
lines = fh.readlines() # 逐行读取fh到列表
nameList = [k.strip() for k in lines ] # 逐行删除无用的空白和换行
fh.close() 
# <<<<< <<<<< <<<<< <<<<< <<<<< 读取上交所公司代码列表


# >>>>> >>>>> 设置列表，用来保存抓取的数据
allData = [['姓名'],['性别'],['所内职务'],['是否党员'],['学历'],['学位'],['所学专业'],['毕业学校'],['资格取得方式'],['全科合格证书号'],['全科合格年份'],['注册会计师证书编号'],['是否合伙人'],['批准注册文件号'],['批准注册时间'],['所在事务所'],['本年度应完成学时'],['本年度已完成学时'],['惩戒及处罚信息(披露时限:自2014年至今)'],['参加公益活动'], ['取得国内其他执业资格']]  # 设置用来保存数据的列表
# <<<<< <<<<< 设置列表，用来保存抓取的数据


# >>>>> >>>>> >>>>> >>>>> 启动浏览器，做好访问准备
ie_driver = os.path.abspath(r"D:\全是数据\注册会计师个人信息抓取201710\IEDriverServer.64") # 指定驱动的位置
os.environ["webdriver.ie.driver"] = ie_driver # 将驱动器位置设为环境变量

url = 'http://cmispub.cicpa.org.cn/cicpa2_web/public/query0/2/0.shtml' # 生成页面链接
time.sleep(3) # 等待5秒钟，让网页充分加载

driverChrome = webdriver.Chrome()   # 再开启一个谷歌浏览器用来显示个人数据
# <<<<< <<<<< <<<<< <<<<< 启动浏览器，做好访问准备 


# >>>>> >>>>> >>>>> >>>>> 依次取出审计师名字，查询个人信息
nameCount = 0 # 名字计数器，设置初值0
for k in range(3618,len(nameList)): # 依次读取审计师名字
    # >>>>> >>>>> >>>>> 如果这个名字还没有被查询过，下面就查询
    print([str(k),nameList[k],str(len(nameList))])
    if nameList[k] not in allData[0]: 
        nameCount = nameCount + 1 # 名字计数器加1
        driver = webdriver.Ie(ie_driver) # 启动IE浏览器
        time.sleep(2)
        driver.get(url) # 前往查询网页
        time.sleep(3) # 等待，让网页充分加载
        driver.switch_to_frame('mainbody') # 跳进框架内
        element = driver.find_element_by_xpath('//input[@name = "perName"]')# 找到输入证券代码的元素
        element.clear()  # 清空
        element.send_keys(nameList[k]) # 填写审计师名字
        time.sleep(2)
        element = driver.find_element_by_xpath('//img[@onclick="return doQuery()"]')# 找到查询按钮
        element.click() # 点击查询
        time.sleep(2)
        
        driver.switch_to_default_content() # 返回主页面框架
    
        driver.switch_to_frame('mainbody') # 跳进框架内
        element = driver.find_elements_by_xpath('//tr/td/div/div[contains(text(),"没有任何信息")]') # 抓取没有任何信息的标志
        if len(element)==0:
            # >>>>> 找总页数
            element = driver.find_elements_by_xpath('//tr/td/div/div[contains(text(),"条记录")]')
            text = element[0].text # 取出文字内容
            pageAll = int(re.findall('/ 共(.*?)页 /',text)[0]) # 取出总页数
            # <<<<< 找总页数
            pageCount = 1 # 设置页数计数器初值1          
            while pageCount <= pageAll:
                elementPerson = driver.find_elements_by_xpath('//tbody/tr/td/a[contains(text(),nameList[k])]')  # 找出所有审计师名字的链接元素
                personNum = len(elementPerson)-1 # 取出页面的人数
                allData = getPageData(personNum, elementPerson, driverChrome,allData) # 采集该页面上的所有审计师的个人信息
                # >>>>> 执行翻页
                if pageCount<pageAll:
                    element = driver.find_elements_by_xpath('//tr/td/div/div/table/tbody/tr/td/div/a[contains(text(),"下一页")]') # 找到翻页按钮
                    js = element[0].get_attribute("href") # 找到翻页按钮
                    js = re.findall('javascript:(.*?)\;',js)[0] # 提取翻页的脚本命令
                    driver.execute_script(js) # 执行翻页js代码
                    time.sleep(2)
                    driver.switch_to_default_content() # 返回主页面框架
                    driver.switch_to_frame('mainbody') # 跳进框架内
                #if End
                pageCount = pageCount + 1 # 页面计数器加1
                # <<<<< 执行翻页
            # while End End End End
        else:
            pass
        driver.quit() # 关闭IE浏览器
        #if End End End
        
        
        
        # >>>>> >>>>> 每查了20个名字就保存依次
        if nameCount==20:
            nameCount = 0 # 把人名计数器置为0
            fh = open('D:\全是数据\注册会计师个人信息抓取201710\抓取结果保存\注册会计师信息抓取'+str(k)+'.txt', 'w') 
            for i in range(len(allData[0])):
                fh.write(allData[0][i] + '^' + allData[1][i] + '^' + allData[2][i] + '^' + allData[3][i] + '^' + allData[4][i] + '^' + allData[5][i] + '^' + allData[6][i] + '^' + allData[7][i] + '^' + allData[8][i] + '^' + allData[9][i] + '^' + allData[10][i] + '^' + allData[11][i] + '^' + allData[12][i] + '^' + allData[13][i] + '^' + allData[14][i] + '^' + allData[15][i] + '^' + allData[16][i] + '^' + allData[17][i] + '^' + allData[18][i] + '^' + allData[19][i] + allData[20][i]+'\n') # 列表中间间隔^号)   
            fh.close()
            # >>>>> 清空列表
            allData = [['姓名'],['性别'],['所内职务'],['是否党员'],['学历'],['学位'],['所学专业'],['毕业学校'],['资格取得方式'],['全科合格证书号'],['全科合格年份'],['注册会计师证书编号'],['是否合伙人'],['批准注册文件号'],['批准注册时间'],['所在事务所'],['本年度应完成学时'],['本年度已完成学时'],['惩戒及处罚信息(披露时限:自2014年至今)'],['参加公益活动'], ['取得国内其他执业资格']]  # 设置用来保存数据的列表
            # <<<<< 清空列表
            print('执行了一次保存')
        else:
            pass
        # if End End End End
        # <<<<< <<<<< 每查了30个名字就保存依次
    else:
        pass
    #if End End 
    # <<<<< <<<<< <<<<< 如果这个名字还没有被查询过，下面就查询
#for End
# <<<<< <<<<< <<<<< <<<<< 依次取出审计师名字，查询个人信息
    




