# Feasibility-only surname dict (Stage 0 trial). Final baseline MUST come from ChineseNames (frozen).
# key=hanzi(surname) value=pinyin (lowercase, for alphabetical key). Longest-match at position 0.
SURNAMES = {
"欧阳":"ouyang","太史":"taishi","上官":"shangguan","司马":"sima","东方":"dongfang","独孤":"dugu",
"呼延":"huyan","皇甫":"huangfu","尉迟":"yuchi","公孙":"gongsun","令狐":"linghu","诸葛":"zhuge",
"司徒":"sitang","慕容":"murong","长孙":"changsun","夏侯":"xiahou","端木":"duanmu","百里":"baili",
"东门":"dongmen","西门":"ximen","南宫":"nangong","第五":"diwu","宇文":"yuwen","赫连":"helian",
"万俟":"wanqi","纳兰":"nalan","鲜于":"xianyu","澹台":"tantai","东方朔":"dongfang",
"王":"wang","李":"li","张":"zhang","刘":"liu","陈":"chen","杨":"yang","黄":"huang","赵":"zhao",
"吴":"wu","周":"zhou","徐":"xu","孙":"sun","马":"ma","朱":"zhu","胡":"hu","郭":"guo","何":"he",
"林":"lin","罗":"luo","高":"gao","郑":"zheng","梁":"liang","谢":"xie","宋":"song","唐":"tang",
"许":"xu","邓":"deng","冯":"feng","韩":"han","曹":"cao","彭":"peng","曾":"zeng","萧":"xiao",
"田":"tian","董":"dong","袁":"yuan","潘":"pan","蒋":"jiang","蔡":"cai","余":"yu","杜":"du",
"叶":"ye","程":"cheng","苏":"su","魏":"wei","吕":"lv","丁":"ding","沈":"shen","任":"ren",
"姚":"yao","卢":"lu","傅":"fu","钟":"zhong","姜":"jiang","崔":"cui","谭":"tan","廖":"liao",
"范":"fan","汪":"wang","金":"jin","石":"shi","戴":"dai","贾":"jia","韦":"wei","方":"fang",
"于":"yu","段":"duan","肖":"xiao","白":"bai","秦":"qin","熊":"xiong","孟":"meng","章":"zhang",
"尹":"yin","薛":"xue","闫":"yan","雷":"lei","侯":"hou","龙":"long","史":"shi","陶":"tao",
"黎":"li","贺":"he","顾":"gu","毛":"mao","郝":"hao","龚":"gong","邵":"shao","万":"wan",
"钱":"qian","严":"yan","祁":"qi","武":"wu","莫":"mo","孔":"kong","向":"xiang","汤":"tang",
"文":"wen","牛":"niu","樊":"fan","温":"wen","芦":"lu","尹":"yin","龚":"gong","路":"lu",
"裴":"pei","康":"kang","伍":"wu","余":"yu","惠":"hui","屈":"qu","鲁":"lu","翁":"weng",
"荀":"xun","羊":"yang","於":"yu","惠":"hui","甄":"zhen","曲":"qu","家":"jia","封":"feng",
"芮":"rui","羿":"yi","储":"chu","靳":"jin","汲":"ji","邴":"bing","糜":"mi","松":"song",
"井":"jing","段":"duan","游":"you","阴":"yin","翟":"zhai","唐":"tang","符":"fu","别":"bie",
"慕":"mu","冼":"xian","祖":"zu","公":"gong","栾":"luan","危":"wei","咸":"xian","修":"xiu",
"亢":"kang","越":"yue","农":"nong","仲":"zhong","仉":"zhang","督":"du","岳":"yue","帅":"shuai",
"缑":"gou","邬":"wu","敖":"ao","恽":"yun","乐":"yue","夔":"kui","侨":"qiao","箪":"dan",
"敖":"ao","黑":"hei","都":"du","尉":"yu","澹":"tan","墨":"mo","哈":"ha","谯":"qiao",
# special-pronunciation (duoyin) surnames, evidence-based standard readings
"单":"shan","解":"xie","仇":"qiu","区":"ou","查":"zhang","缪":"miao","柏":"bai","种":"zhong",
"朴":"piao","繁":"fan","盖":"ge","冼":"xian","员":"yun","句":"ju","麻":"ma","武":"wu",
}
def parse5a(name):
    """Longest-match surname at position 0. Returns (hanzi_surname, pinyin) or (None, None)."""
    if not name:
        return (None, None)
    name = name.strip()
    best = None
    for k, v in SURNAMES.items():
        if name.startswith(k):
            if best is None or len(k) > len(best[0]):
                best = (k, v)
    return best
