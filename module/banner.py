#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author : mhtsec
# @Github : https://github.com/mhtsec

from module.argParse import parseArgs

def banner():
    parseClass = parseArgs()
    args = parseClass.parse_args()
    logo = f"""
                  _________
                      |
                      |
                     _|_
                ///\(\033[0m\033[31mo\033[0m\033[92m_\033[0m\033[31mo\033[0m\033[92m)/\\\\\\
                |||  ` '  |||
     ip2domain                25.1.25 棉花糖修复增强版 公众号:棉花糖fans
                    v1.4
    """
    msg = f"""  ip2domain：IP反查域名，查询备案信息、查询百度等引擎权重
            
 (由于接口对请求频率有限制，故查询速率较慢，请耐心等待)
    """
    match args.model:
        case 1:
            msg1 = f""" 您当前选择的接口为1，提供百度PC、百度移动、360、神马、搜狗权重"""           
        case 2:
            msg1 = f""" 您当前选择的接口为2，提供百度PC、百度移动权重，其他会显示为n"""    


    print("\033[92m" + logo + "\033[0m")
    print(msg)
    print(msg1)
if __name__ == "__main__":
    pass
