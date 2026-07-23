import flet as ft
import webbrowser
categories = {
    "地理信息介绍":["位置与范围与区划"],
    "古建筑·遗迹·自然景点":["永乐宫","圣寿寺","广仁王庙","大禹渡","清凉寺","石佛寺","城隍庙","风陵渡古渡口","西侯度遗址","圣天湖","连三舞台"],
    "美食":["卤肉与饼夹肉","麻片","东风点心","泡泡油糕","石子馍"],
    "农产品":["花椒","苹果","硕黄瓜","芦笋","香椿"],
    "现代活动聚集点":["芮城县县城"],
    "交通线路":["盐湖区到芮城","芮城县内交通线"]
}
spot_info = {
    "永乐宫":{
        "简介":"有客问朝元，我言永乐宫。\n碧瓦绕雕梁，如入神仙洞。\n朝来见吕祖，曾闻迁徙风。\n笑邀云来客，彩工灼其华。\n时不待兮七百年，留此仙容越流年。\n纷纷繁繁未蹉跎，只待今日得见君。",
        "B站链接":"https://www.bilibili.com/video/BV1xEf7BgE1y?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"34.720687°N,110.693119°E",
        "图片":"sucai/永乐宫.jpg"
     },
    "圣寿寺":{
        "简介":"始建于北宋熙宁八年（约1075年），因寺内藏有舍利也称舍利塔，实话讲我没进去看过。",
        "图片":"sucai/圣寿寺.jpg",
        "B站链接":"",
        "定位坐标":"芮城县亚宝北路70号"
     },
    "广仁王庙":{
        "简介":"是我国现存仅存的几座唐代木结构建筑之一，正殿建于唐大和五年（831年），也是现存唯一的唐代道教木构建筑。",
        "B站链接":"https://www.bilibili.com/video/BV1jZ421T78v?vd_source=11048c0dfceac13621bf4b3f9acac6f4https://www.bilibili.com/video/BV1xEf7BgE1y?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"34.729243°N,110.687379°E",
        "图片":"sucai/广仁王庙.jpg"
     },
    "大禹渡":{
        "简介":"饱览长江君无数，畅游黄河有风人。\n近距离接触黄河，饱览大河两岸壮丽景致。\n看水扬三千滋沃土，讲功著大禹不嫌多。",
        "B站链接":"https://www.bilibili.com/video/BV1qMFJeuE2c?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"34.65752°N,110.764363°E",
        "图片":"sucai/大禹渡.jpg"
     },
    "清凉寺":{
        "简介":"元代名刹（寺院），感受脱离凡尘的安宁。旁边的古墓群是2025年西北卷历史卷第一道选择题的材料出处。",
        "B站链接":"https://www.bilibili.com/video/BV1ax4y1L7GZvd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"https://surl.amap.com/bqXESGI1s5CR",
        "图片":"sucai/清凉寺.jpg"
     },
    "石佛寺":{
        "简介":"山顶上的荒废寺庙，纯属景好，顺带可以爬山。",
        "B站链接":"",
        "定位坐标":"https://surl.amap.com/liRkvBYHgqE",
        "图片":""
     },
    "风陵渡古渡口":{
        "简介":"黄河在这里完成了最后的大几字形转弯，将自己温柔的目光两度投向了这片与她朝夕的土地，这其中一度便是风陵渡。\n这是风后长眠的地方，是黄河上的古老渡口，是书中承载了仙人之恋的地方，是雄鸡晓唱三省的交界。\n风陵渡，她顾望着潼关，瞭望着三门峡，感受着此地千年的兴衰，鼓动着自己年轻的生命。",
        "B站链接":"https://www.bilibili.com/video/BV1xc41167f8?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"https://surl.amap.com/477vZxg1a96t",
        "图片":"sucai/风陵渡.jpg"
     },   
    "城隍庙":{
        "定位坐标":"https://surl.amap.com/dzM6HiaB0gP",
        "图片":"sucai/城隍庙.jpg",
        "简介":"中国现存最古老的城隍庙，在这里感受宋元明清四个朝代的交汇，探访国人悠久的城池历史",
        "B站链接":"https://www.bilibili.com/video/BV1aN5v6oESs?vd_source=11048c0dfceac13621bf4b3f9acac6f4"
     },
    "连三舞台":{
        "简介":"山西运城芮城县东吕村的元代连三古戏台，始建于1328年，距今698年。\n是全国罕见的三台连体同基共建式元代建筑遗存中台祈愿（对玉皇大帝殿）、东台求子还愿（对送子观音殿）、西台献戏，庙会时三台可同时开演，观众自由穿梭，被称为<元代的沉浸式剧场>。\n是电视剧《主角》剧中<破蒙戏>关键场景的取景地",
        "B站链接":"https://www.bilibili.com/video/BV1pj7B6oEYs?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"https://surl.amap.com/dKarqjoo84r",
        "图片":"sucai/连三舞台.jpg"
     },
    "西侯度遗址":{
        "简介":"位于山西芮城县风陵渡镇，距今约180万年（最新测年达243万年），\n是中国境内已知最早的旧石器时代文化遗存之一，也是迄今发现的最早猿人用火遗址。\n2019年国家第二届全国青年运动会的圣火采集地。",
        "B站链接":"https://www.bilibili.com/video/BV1vGjGzDEUo?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"https://surl.amap.com/fwBd16t1837f",
        "图片":"sucai/西侯度.jpg"
     },
    "圣天湖":{
        "简介":"芮城县陌南镇的国家级湿地保护区，地处秦晋豫三省交界处黄河岸边，是集生态观光、休闲度假为一体的国家4A级景区（非常大，玩的东西很多，要注意自己的体力）。\n是黄河即将告别山西时留下的最后一份礼物，在冬季时会有天鹅飞来客居越冬。",
        "定位坐标":"https://surl.amap.com/eCRWDQEffV",
        "B站链接":"https://www.bilibili.com/video/BV1jw411e7Ha?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "图片":"sucai/圣天湖.jpg"
     },
    "卤肉与饼夹肉":{
        "简介":"好吃的很，比较知名的几家店就是：阳城镇：东娃卤肉；风陵渡：亮亮中餐馆；县城：熟肉店，建宏卤肉店。",
        "B站链接":"https://www.bilibili.com/video/BV1er421j7oG?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"",
        "图片":"sucai/卤肉.jpg"
    },
    "麻片":{
        "简介":"芮城的重磅甜食，很甜很脆，有点小齁，芝麻很香。",
        "B站链接":"https://www.bilibili.com/video/BV1tt411z7MZ?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"",
        "图片":"sucai/麻片.jpg"
    },
    "东风点心":{
        "简介":"芮城人的经典点心，很甜，风陵渡东风食品厂出品",
        "B站链接":"https://www.bilibili.com/video/BV1LT411Q7Sk?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"",
        "图片":"sucai/东风食品.jpg"
    },
    "泡泡油糕":{
        "简介":"夯爆了，吃到红糖馅云朵的感觉。",
        "B站链接":"",
        "定位坐标":"",
        "图片":"sucai/油糕.jpg"
    },
    "石子馍":{
        "简介":"历史悠久的硬面饼子，外酥里嫩，好吃，可以加点东西（酱、榨菜一类等）吃。",
        "B站链接":"https://www.bilibili.com/video/BV1Mj411d7TV?vd_source=11048c0dfceac13621bf4b3f9acac6f4",
        "定位坐标":"",
        "图片":"sucai/石子馍.jpg"
    },
    "花椒":{
        "简介":"椒块很大很稠，很麻，主要品种是：大红袍、狮子头、韩城椒，可以买些干椒回去做菜用。",
        "B站链接":"",
        "定位坐标":"",
        "图片":"sucai/花椒.jpg"
    },
    "硕黄瓜":{
        "简介":"很大的类黄瓜的作物，多用于凉拌，\n‘硕’是我取的近似风陵渡土话的化音，我们那边叫‘sou(三声)’黄瓜。",
        "B站链接":"",
        "定位坐标":"",
        "图片":"sucai/大黄瓜.jpg"
    },
    "苹果":{
        "简介":"国家地理标志保护产品，颜值高，营养更丰富，优秀的口感。\n永乐牌红富士有‘中华名果’之称。",
        "B站链接":"",
        "定位坐标":"",
        "图片":"sucai/苹果.jpg"
    },
    "芦笋":{
        "简介":"个体饱满，顶鳞不易开散，清爽脆口，营养丰富。",
        "B站链接":"",
        "定位坐标":"",
        "图片":"sucai/芦笋.jpg"
    },
    "香椿":{
        "简介":"国家农产品地理标志产品，芮城拥有原产品种‘条山红’叶厚芽嫩，色泽鲜红，味香浓郁（不过吃多容易上火），多参与面食制作。",
        "B站链接":"",
        "定位坐标":"",
        "图片":"sucai/香椿.jpg"
    },
    "芮城县县城":{
        "简介":"半山腰之城，医院等基础设施完善，蜜雪冰城、电影院等皆备，芮城最繁华的地方，东茂广场消费价格有些高，不适合买衣服，买衣服建议去对面。\n县城内路网发达，交通比较好（县城外就不一定了），路面整齐宽广，环境质量较好。",
        "B站链接":"",
        "定位坐标":"https://surl.amap.com/4gQCUCjS8c6",
        "图片":"sucai/县城.jpg"
    },
    "盐湖区到芮城":{
        "简介":"公路：S87运风高速（盐湖——风陵渡），G59呼北高速与曹风线（盐湖——芮城县县城）（更近一些，但在盐湖区内绕的路较多）；\n铁路：运城站——风陵渡站（K237，8165（所谓的水上列车），K2665），\n公交:109路（运城北站——芮城县县城）。",
        "B站链接":"",
        "定位坐标":"https://surl.amap.com/hgisOFc13blm",
        "图片":"sucai/路线1.JPG" 
    },
    "芮城县内交通线":{
        "简介":"有‘沿河’，沿山‘’，‘中线’三路，均由风陵渡——芮城县县城，基本旅游资源均在中线，芮城县也有景点交通，不过跟没有没啥差别。\nBut!!!芮城的公共交通做的很烂，候车半小时起步，一次拉的人还有些少，所以还是开车来吧。",
        "B站链接":"",
        "定位坐标":"",
        "图片":"sucai/公交.JPG"
    },
    "位置与范围与区划":{
        "简介":"芮城县是山西省运城市下辖的一个县，位于山西省最南端，地处晋、陕、豫三省交界处，地理位置独特,北依中条山，南临黄河，东西狭长，北高南低。\n总面积：约1176—1178.76平方公里，属黄土丘陵地区，沟壑纵横，多沟多涧。\n截至近年调整，芮城县辖8个镇、2个乡，县政府驻古魏镇大禹东街：古魏镇、风陵渡镇、陌南镇、西陌镇、永乐镇、大王镇、阳城镇、南磑镇（南卫乡）、东垆乡、学张乡。\n芮城县还设有山西风陵渡经济开发区。",
        "B站链接":"",
        "定位坐标":"",
        "图片":"sucai/地图.jpg"
    }   
}
def main(page:ft.Page):
    page.title = "山西省运城市芮城县全境旅游攻略端"
    page.add(ft.Text("黄河明珠，景秀芮城，欢迎到来"))
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20  
    def show_home():
        page.controls.clear()
        page.add(ft.Text("分类导航索引",size = 24 )) 
        for category_name in categories:
            page.add(ft.Text(category_name,size = 20))
            for item in categories[category_name]:
                page.add(ft.Button(item , data = item ,on_click = show_detail_page , style = ft.ButtonStyle(text_style = ft.TextStyle(size = 16))))
            page.add(ft.Divider())
        page.update()
    def show_detail_page(e):
        spot_name = e.control.data
        info = spot_info.get(spot_name,{"简介":"暂无信息","B站链接":"","定位坐标":""})
        page.controls.clear()
        page.add(ft.Text(spot_name,size = 24))
        page.add(ft.Text("简介", size = 18))
        if "图片" in info:
            page.add(ft.Image(src = info["图片"] , width = 400 , height = 250))
        page.add(ft.Text(info["简介"]))
        page.add(ft.Divider())
        if info["B站链接"]:
            page.add(ft.Button("看B站相关视频", on_click = lambda _: webbrowser.open(info["B站链接"])))
        if info["定位坐标"]:
            page.add(ft.Button("高德导航", on_click = lambda _: webbrowser.open(f"https://url.amap.com/navigation?to = {info['定位坐标']},{spot_name}&mode = car")))
        page.add(ft.Button("返回首页", on_click = lambda _: show_home()))
        page.update()    
    show_home()    
ft.app(target=main)
